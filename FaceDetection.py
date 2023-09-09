#run in terminal by writing python filename
#face detection in live video
import cv2
#create camera object
cam=cv2.VideoCapture(0)
#model
model=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
#read image from camera object
while True:
  success,img=cam.read()
  if not success:
    print("reading camera failed")
  faces=model.detectMultiScale(img,1.3,5)
  for f in faces:
    x,y,w,h=f
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

 
  cv2.imshow("imagewindow",img)
  key=cv2.waitKey(1)#between every two images there is a delay of one ms
  if key== ord('q'):#ord gives ascii value
    break
 #release camera and destroy the window
cam.release()
cv2.destroyAllWindows()