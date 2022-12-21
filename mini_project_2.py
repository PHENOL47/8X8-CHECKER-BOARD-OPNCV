#MINI PROJECT 2

#NAME - AYUSH KUMAR SHARMA
#YEAR - 2ND  DEPT - ECE
#email - sharmaayushKv@gmail.com
#KALYANI GOVERNMENT ENGINEERING COLLEGE

#MAKING A 8X8 CHECKER BOARD


import cv2 #IMPORTING THE LIBARARIES

import numpy as np 

c=0
m=0

img = np.zeros((800,800,3))#TAKING A IMAGE OF DIMENSION 800X800 WITH SOLID COLOR BLACK

for i in range(0,800,100):
    c=c+1 #INCREMENTING WITH EACH CYCLE

    for j in range(0,800,100):
        m=m+1 #INCREAMENTING WITH EACH CYCLE

        if (c+m)%2 == 0: #WE NEED WHITES IN POSITIONS OF 1 , 3 , 5...UPTO 64 . SO, WE PUT THIS CONDITION TO CHECK FOR SUCH POSTION

            img[j:j+100,i:i+100]=255,255,255 #WHEN WE FIND SUCH POSITION WE WILL CHANGE COLOR TO WHITE
        

img1= cv2.resize(img,None,fx=0.75,fy=0.75) #resizing the image to fit in screen


cv2.imshow('8X8 CHECKERBOARD',img1) #displaying the image

cv2.waitKey(0)

cv2.destroyAllWindows()
