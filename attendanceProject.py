import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime


path='imagesAttendance'
images=[]
classNames=[]
myList=os.listdir(path)
#print(myList)

for cl in myList:
    currentImage=cv2.imread(f'{path}/{cl}')
    images.append(currentImage)
    classNames.append(os.path.splitext(cl)[0])
#print(classNames)

def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markattendance(name):
    with open("attendace.csv","r+") as f:
        mydatalist=f.readlines()
        namelist=[]
        for line in mydatalist:
            entry=line.split(",")
            namelist.append(entry[0])
        if name not in namelist:
            now=datetime.now()
            dtString=now.strftime("%H:%M:%S")
            f.writelines(f'\n{name},{dtString}')


encodelistKnown=findEncodings(images)
#print(len(encodelistKnown))

cap=cv2.VideoCapture(0)

while True:
    succces,img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    faceCur=face_recognition.face_locations(imgS)
    encodesCur=face_recognition.face_encodings(imgS,faceCur)

    for encode,faceloc in zip(encodesCur,faceCur):
        matches=face_recognition.compare_faces(encodelistKnown,encode)
        faceDis=face_recognition.face_distance(encodelistKnown,encode)
        #print(faceDis)
        matchIndex=np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1, x2, y2, x1 =y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,225,0),2)
            #cv2.rectangle(img,(x1,y1-35),(x2,y2),(0,255,0),2)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markattendance(name)

    cv2.imshow("webcam",img)
    cv2.waitKey(1)




