# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:26:55 2021

@author: yazılım
"""


"""

optik form okuyucu

"""

import cv2
import numpy as np
import utils

########################################################################

path = "bionluk.jpg"


heightImg = 700
widthImg  = 700

questions = 30
choices = 15


########################################################################

img= cv2.imread(path)

#hazırlık ^^^^^^^^^^^^
img= cv2.resize(img,(widthImg,heightImg))

imgContours = img.copy()
imgBiggestContours = img.copy()
imgBiggestContours_batu = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur,10,50)

#bütün contourleri bulma
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours,contours,-1,(0,255,0),10)

#köşe bulma
rectCon= utils.rectContour(contours)

biggestContour = utils.getCornerPoints(rectCon[0])
#print(biggestContour.shape)
gradePoints = utils.getCornerPoints(rectCon[1])
#print(len(biggestContour))
#print(biggestContour)
#print(gradePoints)

if biggestContour.size != 0 and gradePoints.size !=0:
    cv2.drawContours(imgBiggestContours,biggestContour,-1,(0,255,0),20)
    cv2.drawContours(imgBiggestContours,gradePoints,-1,(255,0,0),20)
    
    biggestContour=utils.reorder(biggestContour)
    gradePoints=utils.reorder(gradePoints)
    
    pt1= np.float32(biggestContour)
    pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix = cv2.getPerspectiveTransform(pt1,pt2)
    imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))

    ptG1= np.float32(gradePoints)
    ptG2 = np.float32([[0,0],[325,0],[0,150],[325,150]])
    matrixG = cv2.getPerspectiveTransform(ptG1,ptG2)
    imgGradeDisplay= cv2.warpPerspective(img,matrixG,(325,150))     
    #cv2.imshow("grade",imgGradeDisplay)
    
    #TRESHOLD ALMA
    
    imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
    imgTresh = cv2.threshold(imgWarpGray,170,255,cv2.THRESH_BINARY_INV)[1]  
    
    
    boxes= utils.splitBoxes(imgTresh)
    #cv2.imshow("test",boxes[2])
    
    #print(cv2.countNonZero(boxes[1]),cv2.countNonZero(boxes[3]))
    
    
    
    #cevaplar için pixel değerlerini alıyoruz
    myPixelVal = np.zeros((questions,choices))
    countC=0
    countR =0
    
    
    
    for image in boxes:
        totalPixels = cv2pixels = cv2.countNonZero(image)
        myPixelVal[countR][countC] = totalPixels
        countC +=1
        if (countC == choices):countR +=1 ;countC=0
    #print(myPixelVal)
    

    myIndex=[]
    
    for x in range (0,questions):
        arr= myPixelVal[x]
        #print("arr",arr)     
        myIndexVal = np.where(arr==np.amax(arr))
        print(myIndexVal[0])
        myIndex.append(myIndexVal[0][0])
    print(myIndex)
        
im_batu = imgWarpColored
imgray_batu = cv2.cvtColor(im_batu, cv2.COLOR_BGR2GRAY)
ret_batu, thresh_batu = cv2.threshold(imgray_batu, 127, 255, 0)
contours_batu, hierarchy_batu = cv2.findContours(thresh_batu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



cnt = contours_batu[4]
cv2.drawContours(im_batu, [cnt], 0, (0,255,0), 3)


imgBlank = np.zeros_like(img)
imageArray = ([img,imgGray,imgBlur,imgCanny],[imgContours,imgBiggestContours,imgWarpColored,imgTresh])

imgStacked = utils.stackImages(imageArray,0.5)

#cv2.imshow("orijinal boyut",img)

cv2.imshow("sıralı resimler",imgStacked)

cv2.waitKey(0)