import cv2
import numpy as np
import face_recognition

img_elon=face_recognition.load_image_file("Elon.png")
img_elon=cv2.cvtColor(img_elon,cv2.COLOR_BGR2RGB)
img_elon_musk=face_recognition.load_image_file("Elon Musk (2).png")
img_elon_musk=cv2.cvtColor(img_elon_musk,cv2.COLOR_BGR2RGB)

faceloc=face_recognition.face_locations(img_elon)[0]
encode_elon=face_recognition.face_encodings(img_elon)[0]
#print(faceloc) #this values are face location from  top right left and bottom 
cv2.rectangle(img_elon,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

faceloc1=face_recognition.face_locations(img_elon_musk)[0]
encode_elon_musk=face_recognition.face_encodings(img_elon_musk)[0]
cv2.rectangle(img_elon_musk,(faceloc1[3],faceloc1[0]),(faceloc1[1],faceloc1[2]),(255,0,255),2)
 #faceloc[3] represents how much rectangle should be croped for the top of the face and (255,0,255,2) here 2 is thicknees of the rectangle

cv2.imshow("Jack Ma",img_elon)
cv2.imshow("Elon Musk (2)",img_elon_musk)
cv2.waitKey(0)