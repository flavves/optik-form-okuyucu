# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:56:07 2021

@author: yazılım
"""


import json
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2




import cv2
s_img = cv2.imread("ornekler/10.png")
s2_img = cv2.imread("ornekler/20.png")
s3_img = cv2.imread("ornekler/30.png")
s4_img = cv2.imread("ornekler/40.png")

turkce = cv2.imread("ornekler/turkce.png")
matematik = cv2.imread("ornekler/matematik.png")
fen = cv2.imread("ornekler/fen.png")
sosyal = cv2.imread("ornekler/sosyal.png")

l_img = cv2.imread("ornekler/optik_tekli.png")

y1_offset=200
x1_offset=50

y2_offset=200
x2_offset=450

y3_offset=200
x3_offset=850

y4_offset=200
x4_offset=1250



turkce_y=100
turkce_x=130

matematik_y=100
matematik_x=500

fen_y=100
fen_x=930

sosyal_y=100
sosyal_x=1330




l_img[y1_offset:y1_offset+s_img.shape[0], x1_offset:x1_offset+s_img.shape[1]] = s_img

l_img[y2_offset:y2_offset+s2_img.shape[0], x2_offset:x2_offset+s2_img.shape[1]] = s2_img

l_img[y3_offset:y3_offset+s3_img.shape[0], x3_offset:x3_offset+s3_img.shape[1]] = s3_img

l_img[y4_offset:y4_offset+s4_img.shape[0], x4_offset:x4_offset+s4_img.shape[1]] = s4_img



l_img[turkce_y:turkce_y+turkce.shape[0], turkce_x:turkce_x+turkce.shape[1]] = turkce

l_img[matematik_y:matematik_y+matematik.shape[0], matematik_x:matematik_x+matematik.shape[1]] = matematik

l_img[fen_y:fen_y+fen.shape[0], fen_x:fen_x+fen.shape[1]] = fen

l_img[sosyal_y:sosyal_y+sosyal.shape[0], sosyal_x:sosyal_x+sosyal.shape[1]] = sosyal



gostermelik = cv2.resize(l_img, (1500, 750)) 

cv2.imshow("Sonuç",gostermelik)
cv2.waitKey(0) 


cv2.imwrite("Sonuc.png", l_img)

