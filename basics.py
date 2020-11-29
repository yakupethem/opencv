import cv2
import numpy as np
import face_recognition

imgElon=face_recognition.load_image_file("imagesBasic/elon_musk.jpg")
imgTest=face_recognition.load_image_file("imagesBasic/elon_test.jpg")
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

facelocation=face_recognition.face_locations(imgElon)[0]
encodeElon=face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(facelocation[3],facelocation[0]),(facelocation[1],facelocation[2]),(255,0,255),2)

facelocationtest=face_recognition.face_locations(imgTest)[0]
encodeElontest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(facelocationtest[3],facelocationtest[0]),(facelocationtest[1],facelocationtest[2]),(255,0,255),2)

result=face_recognition.compare_faces([encodeElon],encodeElontest)
facedistance=face_recognition.face_distance([encodeElon],encodeElontest)
print(result,facedistance)
cv2.putText(imgTest,f"{result}{round(facedistance[0],2)}",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)


cv2.imshow("elon",imgElon)
cv2.imshow("elonTest",imgTest)
cv2.waitKey(0)