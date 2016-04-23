import cv2
import numpy as np
cap = cv2.VideoCapture(0) #using primary webcam

##write this captured video somewhere..
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc,20.0,(640,480))

#---------------------------------------------------------------------
while True:
    ret ,frame = cap.read()
    cv2.imshow('Frame',frame)     #show the frame captured currently
    out.write(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', gray)
    if cv2.waitKey(1)& 0xFF==ord('q'): # press "q" to quit
        break
###-------------------------------------------------------------------
cap.release()
out.release()
cv2.destroyAllWindows()
