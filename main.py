#Importing the libraries
import cv2
import numpy as np

#Setting up the video and variables
video = cv2.VideoCapture("video.mp4")
image = cv2.imread("image.jpg")

#Storing the video in the folder
result = cv2.VideoWriter('result.mp4', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         40, (640,480))
while True:
    ret, frame = video.read()
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_val = np.array([32,94,132])
    u_val = np.array([179,255,255])
    mask = cv2.inRange(hsv,l_val,u_val)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    f = frame-res
    green_screen=np.where(f==0, image, f)
    cv2.imshow("Final",green_screen)
    result.write(green_screen)
    k=cv2.waitKey(1) #Unicode value will be stored
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()