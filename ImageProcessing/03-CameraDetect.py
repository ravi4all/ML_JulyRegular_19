import cv2
dataset = cv2.CascadeClassifier('data.xml')
cap = cv2.VideoCapture(0)
while True:
    ret,img = cap.read()
    if ret:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,255),4)
        cv2.imshow('result',img)
        if cv2.waitKey(5) == 27:
            break
    else:
        print("Camera not working")

cap.release()
cv2.destroyAllWindows()