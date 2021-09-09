# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:58:53 2021

@author: yazılım
"""


import os
import cv2
import numpy as np
image_path='5gercek.jpeg'
image=cv2.imread(image_path)


gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
th1,img_bin = cv2.threshold(gray_scale,150,225,cv2.THRESH_BINARY)
img_bin=~img_bin

cv2.imshow("split",img_bin)
cv2.waitKey(0) 


line_min_width = 15
kernal_h = np.ones((1,line_min_width), np.uint8)
kernal_v = np.ones((line_min_width,1), np.uint8)

img_bin_h = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_h)

cv2.imshow("split",img_bin_h)
cv2.waitKey(0) 


img_bin_v = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_v)

cv2.imshow("split",img_bin_v)
cv2.waitKey(0) 



img_bin_final=img_bin_h|img_bin_v

cv2.imshow("split",img_bin_final)
cv2.waitKey(0) 

_, labels, stats,_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)

for x,y,w,h,area in stats[2:]:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)



cv2.imshow("split",image)
cv2.waitKey(0) 


final_kernel = np.ones((3,3), np.uint8)
img_bin_final=cv2.dilate(img_bin_final,final_kernel,iterations=1)

cv2.imshow("split",img_bin_final)
cv2.waitKey(0) 


_, labels, stats,_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)


for x,y,w,h,area in stats[2:]:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)



cv2.imshow("split",img)
cv2.waitKey(0) 








