# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:25:54 2022

@author: okmen
"""
import glob
import json
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import utils



Hassaslik =100
Hassaslik=float(Hassaslik)

images = glob.glob('resimler/*.jpeg')

file = open("sonuclar.txt","w")


heightImg = 3500
widthImg  = 2500
resim_sayac=1


for ressim in images:
    
    path = "resimler/3.jpeg"
    
    heightImg = 800
    widthImg  = 800
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
        
    
        
        #ad-soyad kısmı
        biggestContour_1 = utils.getCornerPoints(rectCon[0])
        
        cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
    
        cv2.imshow("Sonuç",imgBiggestContours)
        cv2.waitKey(0) 
    
    except:
            
        pass
    

    
    
    try:
        imgBiggestContours = img.copy()
        
        
        biggestContour_1=biggestContour_1
        cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)
        
        
        
        
        biggestContour=utils.reorder(biggestContour_1)
        
        
        
        
        
        
        
        
        
        
        
        
        heightImg = 1600
        widthImg  = 1600
        #imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 
        
        
        
        
        pt1= np.float32(biggestContour)
        pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
        matrix = cv2.getPerspectiveTransform(pt1,pt2)
        imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))
        
      
        
        gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("Sonuç",gray)
        cv2.waitKey(0) 
        
        
        crop_img_1 = gray[560:1550, 130:360]
        
        
        crop_img_2 = gray[550:1550, 530:760]
        
        crop_img_3 = gray[550:1550, 910:1140]
        
        crop_img_4 = gray[550:1550, 1280:1510]
    except:
        pass
    
    
    """
    gosterme_Sil = cv2.resize(crop_img_1, (700, 700)) 
    cv2.imshow("Sonuç",gosterme_Sil)
    cv2.waitKey(0) 
    """
    
    
    try:
                
     
            """
            thresh = cv2.threshold(crop_img_1, 127, 255,
            	cv2.THRESH_BINARY_INV | cv2.THRESH_BINARY)[1]
            """
            thresh = cv2.threshold(crop_img_1, 0, 255,
            	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            
            
            
            
            
            
            threshd = cv2.resize(thresh, (1800, 1200)) 
            
            
            """
            
            #kontrolcüm
            for i in range (1,50):
                try:
                    
                    rows = np.vsplit(threshd,i)
                    print(i)
                except:
                    print("hata")
            
            """
            
            
            def splitBoxes(img):
                    
                
                #rows = np.hsplit(threshd,5)
                rows = np.vsplit(threshd,10)    
    
                boxes =[]
                for r in rows:
                    cols = np.hsplit(r,4)
    
                    for box in cols:
                        boxes.append(box)
    
                return boxes
            
            boxes=splitBoxes(threshd)
            
            
            
            #print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))
            
            
            
            
            
            
            #cevap alma
            
            myPixelVal=np.zeros((10,4))
            
            
            countC=0
            countR=0
            cvp_sil=[]
            for image in boxes:
                totalPixels = cv2.countNonZero(image)
                cvp_sil.append(totalPixels)
            
            cvp_sil=np.array(cvp_sil)
            cvp_sil=cvp_sil.reshape(10,4)
            #cvp_sil[27]
            myPixelVal=cvp_sil
            
            #TEST
            #İLK 1,2,3,4 VB 2. A,B,C,D
            
            #myPixelVal[26][2]
            
            try:
             sayac=0
             sinav_kodu_buldum=[]
             numara_kontrolcu=[]
             ekleme_listesi_deneme=[]
             ekleme_listesi_deneme_sonucu=0
             iki_Sik_isaretlenmis_mi=False
             Bos_mu=False
             
             
             
             
             
             
             
             
             
             try:
                     
                 for deneme in range(0,10):
                     for x in range (0,4):
                 
                     
                         
                         arr=myPixelVal[deneme][x]
                         ###print(arr)
                         
                 
                             
                         ekleme_listesi_deneme.append(arr)
                         
                         #deneme
                         
                         
                  
                 
                     ekleme_listesi_deneme.sort()
                     
                     ekleme_listesi_deneme_sonucu=ekleme_listesi_deneme[3]
                     
                     kebele=(ekleme_listesi_deneme[3]-ekleme_listesi_deneme[0])
                     hebele=(kebele/ekleme_listesi_deneme[0])  
                     if hebele*100 < Hassaslik:
                         Bos_mu=True
                     else:
                         Bos_mu=False
                                
                     ekleme_listesi_deneme=[]
                     for x in range(0,4):
                         arr=myPixelVal[deneme][x]
                         if arr == ekleme_listesi_deneme_sonucu:
                             if Bos_mu == False:
                
                                       if x==0:
                                           numara_kontrolcu.append("A")
                                           ""
                                           break
                                       elif x== 1:
                                           numara_kontrolcu.append("B")
                                           ""
                                           break
                                       elif x== 2:
                                           numara_kontrolcu.append("C")
                                           ""
                                           break
                                       elif x== 3:
                                           numara_kontrolcu.append("D")
                                           ""
                                           break
                                       elif x== 4:
                                           numara_kontrolcu.append("E")
                                           ""
                                           break
                                
                             else:
                                 numara_kontrolcu.append("BOS")
                                 Bos_mu=False
                                 break
             except Exception as e:
                  print("hata: ",e)
            
            
            except:
                pass
        
    except:
            pass
    print(numara_kontrolcu)
        




