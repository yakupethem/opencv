import cv2

img=cv2.imread(("kaynak/lambo.png"))
print(img.shape)

imgresize=cv2.resize(img,(500,500))
print(imgresize.shape)

imgCropped=img[0:200,200:500]  #kırpılmış

cv2.imshow("lambo",img)
cv2.imshow("lamboResize",imgresize)
cv2.imshow("lamboCropped",imgCropped)

cv2.waitKey(0)