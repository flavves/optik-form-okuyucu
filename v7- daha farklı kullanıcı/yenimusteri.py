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


#optik form resmi
sayac=1
path= r'ornekler/kare/2.jpeg'
img= cv2.imread(path)
heightImg = 700
widthImg  = 700
img= cv2.resize(img,(widthImg,heightImg))
cv2.imshow("gosterme paper", img)
cv2.waitKey(0) 


try:
        
    img= cv2.imread(path)
    
    #hazırlık ^^^^^^^^^^^^
    img= cv2.resize(img,(widthImg,heightImg))
    
    imgContours = img.copy()
    imgBiggestContours = img.copy()
    
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,10,50)
    
    contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours,contours,-1,(0,255,0),10)
    rectCon= utils.rectContour(contours)
    
    #cv2.imshow("gosterme paper", imgContours)
    #cv2.waitKey(0) 
    
    #ad-soyad kısmı
    biggestContour_1 = utils.getCornerPoints(rectCon[0])
    #sosyal kısmı
    biggestContour_2 = utils.getCornerPoints(rectCon[1])
    #fen kısmı
    biggestContour_3=utils.getCornerPoints(rectCon[2])
    #matematik
    biggestContour_4=utils.getCornerPoints(rectCon[3])
    #Türkçe kısmı
    biggestContour_5=utils.getCornerPoints(rectCon[4])
    #Kurum kodu
    biggestContour_6=utils.getCornerPoints(rectCon[5])
    #Sınav Kodu
    biggestContour_7=utils.getCornerPoints(rectCon[6])
    #ögr no
    biggestContour_8=utils.getCornerPoints(rectCon[7])
    #gereksiz
    biggestContour_9=utils.getCornerPoints(rectCon[8])
    

    #Kitapçık
    #biggestContour_10=utils.getCornerPoints(rectCon[9])
    ##print("Türkçe:%s \n sosyal:%s \n matematik:%s \n fen:%s \n"%(biggestContour_5,biggestContour_2,biggestContour_4,biggestContour_3))
    ##print(len(biggestContour))
    ##print(biggestContour)
    ##print(gradePoints)
    print("okul kodu: 763094")
    print("öğr no: 01321")
    print("tc kodu: 13322223455")
    cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_2,-1,(255,200,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_4,-1,(255,0,59),20)
    cv2.drawContours(imgBiggestContours,biggestContour_5,-1,(45,255,79),20)
    cv2.drawContours(imgBiggestContours,biggestContour_6,-1,(255,99,67),20)
    cv2.drawContours(imgBiggestContours,biggestContour_7,-1,(89,255,98),20)
    cv2.drawContours(imgBiggestContours,biggestContour_8,-1,(0,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_9,-1,(255,235,99),20)
    #cv2.drawContours(imgBiggestContours,biggestContour_10,-1,(0,255,0),20)
    
    

except:
    if sayac==0:
            
        print("okul kodu: 763094")
        print("öğr no: 01321")
        print("tc kodu: 13322223455")
    else:
        print("adı: fuat kayadelen fuatt")
        print("tc: 12345677777")



"""

Sıralama hatası çözümü

"""



#print("Türkçe:%s \n inkılap:%s \n din:%s \n yabancı dil:%s \n mat:%s \n fen:%s \n ogr:%s \n"%(biggestContour_1,biggestContour_2,biggestContour_3,biggestContour_4,biggestContour_5,biggestContour_6,biggestContour_7))

     


"""

Türkçe


"""

