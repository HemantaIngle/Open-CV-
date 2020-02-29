"""
Name-Hemanta Ingle, MS EE- San Jose State University, CA
Purpose of the code- 2D Convolution in open CV
pdisplay.py
Demo read and display image
"""
import sys
import cv2
import numpy as np

#main(sys.argv[1:])
window_name = '2dconv'
 
imageName = sys.argv[0] #get file name from command line 

src = cv2.imread(imageName, cv2.IMREAD_COLOR)

if src is None:
   print ('Error opening image!')
   print ('Usage: pdisplay.py image_name\n')
  
  #2D Convolution 
  blur = cv.GaussianBlur(img,(5,5),0)
ind = 0
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
while True: 
    cv2.imshow("frame", blur)

    c = cv2.waitKey(500)
    if c == 27:
       break

    ind += 1

 
