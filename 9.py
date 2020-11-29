import cv2

img=cv2.imread("kaynak/lena.png")
faceCascade=cv2.CascadeClassifier("kaynak/haarcascade_frontalface_default.xml")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)



cv2.imshow("lena",img)
cv2.waitKey(0)