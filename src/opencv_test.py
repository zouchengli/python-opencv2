import cv2

image = cv2.imread("MonaLisa.jpeg")
 
cv2.imshow("Faces", image)
 
cv2.waitKey(0)
 
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
detector =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
 
rects = detector.detectMultiScale(gray,scaleFactor=1.05, minNeighbors=7, minSize=(30,30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
 
for (x, y, w, h) in rects:
         cv2.rectangle(image,(x, y), (x + w, y + h), (0, 255, 0), 2)
 
cv2.imshow("Faces", image)
 
cv2.waitKey(0)
