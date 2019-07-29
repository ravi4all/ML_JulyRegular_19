import cv2
import numpy as np

face_1 = np.load('face_1.npy')
face_1 = face_1.reshape(200,-1)

face_2 = np.load('face_1.npy')
face_2 = face_2.reshape(200,-1)

names = {
    0 : "Ravi_1",
    1 : "Ravi_2"
}

labels = np.zeros((400,1))
labels[200:,:] = 1.0

faceData = np.concatenate([face_1,face_2])

def dist(x1,x2):
    return np.sqrt(sum((x2 - x1) ** 2))

def knn(x,faceData):
    n = faceData.shape[0]
    distance = []
    for i in range(n):
        # print(x.shape, faceData[i].shape)
        distance.append(dist(x,faceData[i]))
    distance = np.asarray(distance)
    sortedIndex = np.argsort(distance)
    lab = labels[sortedIndex][:5]
    count = np.unique(lab, return_counts=True)
    return count[0][np.argmax(count[1])]

dataset = cv2.CascadeClassifier('data.xml')

capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = dataset.detectMultiScale(img)
        for x,y,w,h in face:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),4)

            faceArray = gray[y:y+h, x:x+w]
            faceArray = cv2.resize(faceArray, (50,50))
            lab = knn(faceArray.flatten(),faceData)
            name = names[int(lab)]
            cv2.putText(img, name, (x, y), font, 1, (0, 0, 255), 2)

        cv2.imshow('result',img)
        if cv2.waitKey(10) == 27:
            break
    else:
        print("Camera not working")

capture.release()
cv2.destroyAllWindows()