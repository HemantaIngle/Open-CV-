"""
Name-Hemanta Ingle, MSEE- San JOse State University, CA
Purpose of the program-Display an Image from your local files 
pdisplay.py
Demo read and display image
"""
import sys
import cv2
import numpy as np

#main(sys.argv[1:])
window_name = 'Display Image'
 
imageName = sys.argv[0] #get file name from command line 

src = cv2.imread(imageName, cv2.IMREAD_COLOR)

if src is None:
   print ('Error opening image!')
   print ('Usage: pdisplay.py image_name\n')
  
ind = 0
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
while True: 
    cv2.imshow("frame", src)

    c = cv2.waitKey(500)
    if c == 27:
       break

    ind += 1

 
