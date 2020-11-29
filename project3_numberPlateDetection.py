import cv2

numberplateCascade = cv2.CascadeClassifier("kaynak/haarcascade_russian_plate_number.xml")
minarea=500
color=(0,0,255)
count=0

img=cv2.imread("kaynak/plaka1.jpg")

while True:
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberplates = numberplateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberplates:
        area=w*h
        if area>minarea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"number plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,1)
            imgRoi=img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)

    cv2.imshow("plaka",img)
    if cv2.waitKey(1) & 0xFF==ord("s"):
        cv2.imwrite("kaynak/scanned/plate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(255,0,0),cv2.FILLED)
        cv2.putText(img,"scanned",(150,165),cv2.FONT_HERSHEY_DUPLEX,2,
                    (0,0,255),2)
        cv2.imshow("result",img)
        cv2.waitKey(750)
        count += 1
        break
