from operator import index
from sre_constants import SUCCESS
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path="C:\\Users\\91970\\Downloads\\Updated Attendence\\Online-Face-Attendance--master\\Online-Face-Attendance--master\\Attendance"
images=[]
classnames=[]
mylist=os.listdir(path)
print(mylist)
for cl in mylist:
  cur_img=cv2.imread(f'{path}/{cl}')
  images.append(cur_img)
  classnames.append(os.path.splitext(cl)[0])
print(classnames)

def findEncodings(images):
  encodelist=[]
  for img in images:
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    encode=face_recognition.face_encodings(img)[0]
    encodelist.append(encode)
  return encodelist

def markattendance(name):
    with open("C:\\Users\\91970\\Downloads\\Updated Attendence\\Online-Face-Attendance--master\\Online-Face-Attendance--master\\attendance.csv","r+") as f: #r+ is read and write
        mydatalist=f.readlines()
        namelist=[]
        for line in mydatalist:
            entry=line.split(",")
            namelist.append(entry[0]) #0 here is intial recognized image
        if name not in namelist:
            now = datetime.now()
            datestring=now.strftime("%Y-%m-%d %H:%M:%S") #hour min sec
            f.writelines(f"\n{name},{datestring}")

encodelistknown=findEncodings(images)
print(len(encodelistknown)) #number of images from the provided path

cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    imgs=cv2.resize(img,(0,0),None,0.25,0.25) #reducing the images size for scaling
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
    facecurframe=face_recognition.face_locations(imgs)
    encodecurframe=face_recognition.face_encodings(imgs,facecurframe)

    for encodeface,faceloc in zip(encodecurframe,facecurframe):
        matches=face_recognition.compare_faces(encodelistknown,encodeface)
        facedist=face_recognition.face_distance(encodelistknown,encodeface) #this uses svm regressor to get the distance between the orginal image and the one displayed now
                                                                            #minimum the distance represents faces are similar
        print(facedist)
        matchindex=np.argmin(facedist)

        if matches[matchindex]:
            name=classnames[matchindex].upper()
            print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4 #as we reduced the images to one-forth its size of it's original image we now multiply it with 4 to get the original image
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markattendance(name)

    cv2.imshow("Webcam",img)
    cv2.waitKey(1)