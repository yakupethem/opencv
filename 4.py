import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]=250,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2)
cv2.rectangle(img,(0,0),(250,300),(0,255,0),2)
cv2.circle(img,(300,50),50,(0,0,255),3)
cv2.putText(img,"yakocan40",(300,200),cv2.FONT_ITALIC,1,(255,255,0),2)


cv2.imshow("image",img)
cv2.waitKey(0)