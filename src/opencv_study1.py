import cv2
import sys
img=cv2.imread("test2.jpg")
rectFile=open("test2.rects", "r+")
for line in rectFile:
  line=line.strip()
  line=line.split(",")
  x=int(line[0])
  y=int(line[1])
  w=int(line[2])
  h=int(line[3])
  cv2.rectangle(img, (x, y - 20), (w, h - 20), (0, 255, 0), 1)
cv2.imwrite("/root/Desktop/test2.jpg", img)
