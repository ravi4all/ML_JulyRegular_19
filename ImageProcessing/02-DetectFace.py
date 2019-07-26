import cv2

dataset = cv2.CascadeClassifier('data.xml')
img = cv2.imread('img_1.jpg')

faces = dataset.detectMultiScale(img,1.28)
# print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)

while True:
    cv2.imshow('result',img)
    if cv2.waitKey(2) == 27:
        break

cv2.destroyAllWindows()