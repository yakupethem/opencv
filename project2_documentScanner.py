import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

width=640
height=480


def preprocess(img):
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imggray,(5,5),1)
    imgcany=cv2.Canny(imgblur,200,200)
    kernel=np.ones((5,5))
    imgdial=cv2.dilate(imgcany,kernel,iterations=2)
    imgthres=cv2.erode(imgdial,kernel,iterations=1)

    return imgthres

def getcontours(img):  #dış çizgi
    biggest=np.array([])
    maxarea=0
    contours,hiyerarsi=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for ctn in contours:
        area=cv2.contourArea(ctn)

        if area>500:
            #cv2.drawContours(imgcontour,ctn,-1,(255,0,0),5)
            parameter=cv2.arcLength(ctn,True)
            aprox=cv2.approxPolyDP(ctn,0.02*parameter,True)
            if area>maxarea and len(aprox)==4:
                biggest=aprox
                maxarea=area
    cv2.drawContours(imgcontour, biggest, -1, (255, 0, 0), 20)
    return biggest

def reorder(mypoints):
    
    mypoints=mypoints.reshape((4,2))
    mypointsnew=np.zeros((4,1,2),np.int32)
    add =mypoints.sum(1)
    print(add)

    mypointsnew[0]=mypoints[np.argmin(add)]
    mypointsnew[3] = mypoints[np.argmax(add)]
    diff=np.diff(mypoints,axis=1)
    mypointsnew[1]=mypoints[np.argmin(diff)]
    mypointsnew[2] = mypoints[np.argmax(diff)]
    print(mypointsnew)
    return mypointsnew

def getwarp(img,biggest):
    #biggest=reorder(biggest)
    #print(biggest.shape)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    output = cv2.warpPerspective(img, matrix, (width, height))
    return output



while True:
    success,img=cap.read()
    img=cv2.resize(img,(width,height))
    imgcontour = img.copy()

    imgthres=preprocess(img)
    biggest=getcontours(imgthres)
    print(biggest)
    imgwarped=getwarp(img,biggest)

    cv2.imshow("video",imgwarped)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break