import cv2

img=cv2.imread("kaynak/lena.png")
cv2.imshow("lena",img)
cv2.waitKey(1000)

cap=cv2.VideoCapture("kaynak/test_video.mp4")
while True:
    success,img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap2=cv2.VideoCapture(0)
cap2.set(3,640)
cap2.set(4,480)
while True:
    success,img=cap2.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
