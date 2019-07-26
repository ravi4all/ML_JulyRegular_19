import cv2

img = cv2.imread('img_1.jpg')
# print(img.shape)
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    # img, (x,y), (w,h), color, border_width
    cv2.rectangle(img, (300,100),(450,250),(0,255,255),5)
    cv2.putText(img,"MS Dhoni",(300,100),font,1,(0,0,255),2)
    cv2.imshow('result',img)
    if cv2.waitKey(30) == 27:
        break
cv2.destroyAllWindows()