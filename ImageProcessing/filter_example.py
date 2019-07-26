import cv2

dataset = cv2.CascadeClassifier('data.xml')
filter = cv2.imread('mask_1.png')

cap = cv2.VideoCapture(0)

while True:
    ret,img =  cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray, 1.3)
        for x,y,w,h in faces:
            # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)
            face = img[y:y+h,x:x+w,:]
            # print(face.shape)
            filter = cv2.resize(filter, (face.shape[0], face.shape[1]))
            img[y:y + h, x:x + w, :] = filter
        cv2.imshow('result',img)
        if cv2.waitKey(10) == 27:
            break
    else:
        print("Camera not working")

cap.release()
cv2.destroyAllWindows()