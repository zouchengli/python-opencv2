# -*- coding: UTF-8 -*-
import cv2  
import sys
img=cv2.imread("test1.jpg")
rectFile=open("test1.rects","r+")
print("---for start---")
for line in rectFile:
  line=line.strip()
  line=line.split(",")
  x=int(line[0])
  y=int(line[1])
  w=int(line[2])
  h=int(line[3])  
  ct=int(line[4])
  if ct == 1:
    font = cv2.FONT_HERSHEY_SIMPLEX
    str = '我';
    if not isinstance(str, unicode): 
     str = str.decode('utf8')
    cv2.putText(img,str,(50,159), font, 1,(0,255,0),2,1)
    cv2.rectangle(img,(x-6,y),(w,h+2),(0,255,0), 2)
  if ct == 2:
    cv2.rectangle(img,(x-6,y),(w,h+2),(255,0,0), 2)
  if ct == 3:
    cv2.rectangle(img,(x-6,y),(w,h+2),(0,0,255), 2)
  if ct == 4:
    cv2.rectangle(img,(x-6,y),(w,h+2),(0,0,255), 2)
  if ct == 5:
    cv2.rectangle(img,(x-6,y),(w,h+2),(0,0,255), 2)

  print("---for end---")
cv2.imwrite("/root/Desktop/test.jpg",img)
