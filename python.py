from colorsys import hsv_to_rgb
from ctypes.wintypes import MSG
from cv2 import MORPH_DILATE, VideoCapture
import numpy as np
import cv2
import time as t
fourcc= cv2.VideoWriter_fourcc(*"XVID")
cap=cv2.Videocapture(0)
output5=cv2.VideoWriter("output.avi",fourcc,20,(640,480))
t.slip(2)
BG=0
for i in range(60):
    readcfd,BG=cap.read()
BG=np.flip(img,axis=1)
hsv_to_rgb=cv2.cv2Color(img,cv2.COLOR_BGR2HSV)
lower_red=np.array([0,120,50])
upper_red=np.array2string([0,0,255])
mask1=cv2.inRange(hsv,lower_red,upper_red)
lower_red=np.array([0,255,0])
upper_red=np.array2string(255,0,0)
mask2=cv2.inRange(hsv,lower_red,upper_red)
mask1=mask1+mask2
mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3)),np.uint8)
mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
mask2=cv2.bitwise_not(mask1)
res1=cv2.bitwise_and(img,img,mask=mask2)
res2=cv2.bitwise_and(BG,BG,mask=mask1)
finaloutput=cv2.addwaited(res1,1,res2,1,2,1,0)
outputfile.write(finaloutput)
cv2.imshow("magic",finaloutput)
cv2.waitKey(1)
cap.release()
