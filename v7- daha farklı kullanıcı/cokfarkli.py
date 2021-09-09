"""

LGS


"""
import json
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import utils



#isaret kısmı
##########################################################################333

path_isaret = r'ornekler/orijinal_optik_form.jpg'
   

image_isaret = cv2.imread(path_isaret)
   

window_name = 'image_isaret_isaret'
  




sayac_uzun=0
sayac_yatay=0


y=94

x_ler=[68,94,120,145,171]
x1_ler=[222,248,274,299,325]
x2_ler=[374,400,425,450,475]

##########################################################################333


#optik form resmi


path = "ornekler/kare/2.jpeg"

try:
        
    img= cv2.imread(path)
    
    #hazırlık ^^^^^^^^^^^^
    
    imgContours = img.copy()
    imgBiggestContours = img.copy()
    
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,10,50)
    
    contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours,contours,-1,(0,255,0),10)
    rectCon= utils.rectContour(contours)
    

    
    #ad-soyad kısmı
    biggestContour_1 = utils.getCornerPoints(rectCon[0])
    #sosyal kısmı
    biggestContour_2 = utils.getCornerPoints(rectCon[1])
    #fen kısmı
    biggestContour_3=utils.getCornerPoints(rectCon[2])
    biggestContour_3=utils.getCornerPoints(rectCon[3])
    biggestContour_4=utils.getCornerPoints(rectCon[4])
    biggestContour_5=utils.getCornerPoints(rectCon[5])
    biggestContour_6=utils.getCornerPoints(rectCon[6])
    biggestContour_7=utils.getCornerPoints(rectCon[7])
    biggestContour_8=utils.getCornerPoints(rectCon[8])
    biggestContour_9=utils.getCornerPoints(rectCon[9])
    biggestContour_10=utils.getCornerPoints(rectCon[10])
    biggestContour_11=utils.getCornerPoints(rectCon[11])
    biggestContour_12=utils.getCornerPoints(rectCon[12])
    biggestContour_13=utils.getCornerPoints(rectCon[12])
   
    
    cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_2,-1,(255,200,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_4,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_5,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_6,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_7,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_8,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_9,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_10,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_11,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_12,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_13,-1,(100,255,0),20)
   
    #cv2.drawContours(imgBiggestContours,biggestContour_10,-1,(0,255,0),20)

    cv2.imshow("Sonuç",imgContours)
    cv2.waitKey(0) 

except:
        
    pass


#############################################33

"""
Yöntem 2


"""

import cv2
import numpy as np

image = cv2.imread(path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

thresh = cv2.threshold(sharpen,160,255, cv2.THRESH_BINARY_INV)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

min_area = 100
max_area = 1500
image_number = 0
for c in cnts:
    area = cv2.contourArea(c)
    if area > min_area and area < max_area:
        x,y,w,h = cv2.boundingRect(c)
        ROI = image[y:y+h, x:x+h]
        cv2.imwrite('ROI_{}.png'.format(image_number), ROI)
        cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
        image_number += 1

cv2.imshow('sharpen', sharpen)
cv2.imshow('close', close)
cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey()


###############################################33
"""

Yöntem 3

"""
  
  
import cv2
import numpy as np


image = cv2.imread(path) 
image=image.resize(900,900)    
img= cv2.resize(img,(900,900))           
# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define blue color range
light_blue = np.array([63,71,204])
dark_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, light_blue, dark_blue)

# Bitwise-AND mask and original image
output = cv2.bitwise_and(image,image, mask= mask)
    
cv2.imshow("Color Detected", np.hstack((image,output)))
cv2.waitKey(0)
cv2.destroyAllWindows()