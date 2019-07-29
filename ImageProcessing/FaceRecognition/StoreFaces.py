import cv2
import numpy as np

dataset = cv2.CascadeClassifier('data.xml')

capture = cv2.VideoCapture(0)
faceData = []
while True:
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = dataset.detectMultiScale(img)
        for x,y,w,h in face:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),4)

            faceArray = gray[y:y+h, x:x+w]
            faceArray = cv2.resize(faceArray, (50,50))
            if len(faceData) < 200:
                faceData.append(faceArray)
                print(len(faceData))
        cv2.imshow('result',img)
        if cv2.waitKey(10) == 27 or len(faceData) >= 200:
            break
    else:
        print("Camera not working")

faceData = np.asarray(faceData)
np.save('face_1.npy',faceData)

capture.release()
cv2.destroyAllWindows()