import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getcontours(img):  #dış çizgi
    contours,hiyerarsi=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for ctn in contours:
        area=cv2.contourArea(ctn)
        print(area)
        if area>500:
            cv2.drawContours(imgcontour,ctn,-1,(255,0,0),5)
            parameter=cv2.arcLength(ctn,True)
            print(parameter)
            aprox=cv2.approxPolyDP(ctn,0.02*parameter,True)
            print(len(aprox))
            objcor=len(aprox)
            x,y,w,h=cv2.boundingRect(aprox)
            if objcor==3:
                otype="3gen"
            elif objcor==4:
                asp=w/float(h)
                if asp<1.05 and asp>0.95:
                    otype="kare"
                else:otype="dikdortgen"
            else: otype="cember"


            cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgcontour,otype,
                        (x+(w//2)-30,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.6,
                        (0,0,0),2)




img=cv2.imread("kaynak/shapes.png")
imgcontour=img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgcanny=cv2.Canny(imgBlur,50,50)
getcontours(imgcanny)
imgblack=np.zeros_like(img)

imgstack=stackImages(0.7,([img,imgcontour,imgGray],
                          [imgcanny,imgBlur ,imgblack]))

cv2.imshow("stack",imgstack)
#cv2.imshow("image",img)
#cv2.imshow("gray",imgGray)
#cv2.imshow("blur",imgBlur)

cv2.waitKey(0)