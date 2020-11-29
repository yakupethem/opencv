import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10,150)

mycolors=[[5,107,0,19,255,255],
          [133,56,0,159,156,255],
          [57,76,0,100,255,255],
          [90,48,0,118,255,255]]
mycolorsvalues=[[51,153,255],
                [255,0,255],
                [0,255,0],
                [255,0,0]]
mypoints=[] #[x,y,colorId]

def findcolor(img,mycolor,mycolorsvalues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    newpoints=[]
    for color in mycolor:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getcontours(mask)
        cv2.circle(imgresult,(x,y),10,mycolorsvalues[count],cv2.FILLED)
        if x!=0 and y !=0:
            newpoints.append([x,y,count])
        count+=1
        #cv2.imshow(str(color[0]),mask)
    return newpoints

def getcontours(img):  #dış çizgi
    contours,hiyerarsi=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for ctn in contours:
        area=cv2.contourArea(ctn)
        if area>500:
            #cv2.drawContours(imgresult,ctn,-1,(255,0,0),5)
            parameter=cv2.arcLength(ctn,True)
            aprox=cv2.approxPolyDP(ctn,0.02*parameter,True)
            x,y,w,h=cv2.boundingRect(aprox)
    return x+w//2,y

def drawoncanvas(mypoints,mycolorsvalues):
    for point in mypoints:
        cv2.circle(imgresult, (point[0], point[1]), 10, mycolorsvalues[point[2]], cv2.FILLED)




#success,img=cap.read()
#imgresult = img.copy()
while True:
    success,img=cap.read()
    imgresult = img.copy()
    newpoints=findcolor(img,mycolors,mycolorsvalues)
    if len(newpoints)!=0:
        for newp in newpoints:
            mypoints.append(newp)
    if len(mypoints)!=0:
        drawoncanvas(mypoints,mycolorsvalues)

    cv2.imshow("video",imgresult)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break