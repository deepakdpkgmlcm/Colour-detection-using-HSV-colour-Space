import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cv2.namedWindow('Trackbars')

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red=np.array([0,70,50])
    upper_red=np.array([10,255,255])
    mask=cv2.inRange(hsv,lower_red,upper_red)
    result_red=cv2.bitwise_and(frame,frame,mask=mask)


    lower_green=np.array([40,40,40])
    upper_green=np.array([70,255,255])
    mask=cv2.inRange(hsv,lower_green,upper_green)
    result_green=cv2.bitwise_and(frame,frame,mask=mask)

    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    result_blue=cv2.bitwise_and(frame,frame,mask=mask)

    #result=cv2.bitwise_and(frame,frame,mask=mask)  Does Not Works Will Show Only one result 

    cv2.imshow("frame",frame)
    
    cv2.imshow("mask",mask)
    cv2.imshow("result_red",result_red)

    cv2.imshow("mask",mask)
    cv2.imshow("result_blue",result_blue)

    cv2.imshow("mask",mask)
    cv2.imshow("result_green",result_green)

    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()