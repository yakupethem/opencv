import cv2

import numpy as np

kernel=np.ones((5,5),np.uint8)

img=cv2.imread("kaynak/lena.png")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),6)
imgCanny=cv2.Canny(img,100,200)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("gri Lena",imgGray)
cv2.imshow("blur Lena",imgBlur)
cv2.imshow("cany Lena",imgCanny)
cv2.imshow("dilate Lena",imgDialation)
cv2.imshow("erode Lena",imgEroded)
cv2.waitKey(0)