# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:25:18 2021

@author: yazılım
"""



from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import utils





path = "uzaktan-ok.jpeg"

heightImg = 700
widthImg  = 700

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

"""

Matematik


"""


imgBiggestContours = img.copy()

#fen kısmı
biggestContour_3=utils.getCornerPoints(rectCon[2])
cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)





biggestContour=utils.reorder(biggestContour_3)


cv2.imshow("gosterme paper", imgBiggestContours)
cv2.waitKey(0) 




heightImg = 1363
widthImg  = 199
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[22:1363, 39:185]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)

"""


!!!!!!!! farklı yöntem kullanmak zorunda kaldım
eğer bir sorun olursa diğerlerinde de bu yöntemi kullanmak zorundayım !!!!!!!!


"""

docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_BINARY)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


cv2.imshow("gosterme", thresh)                            # Show image

#cv2.imshow("gosterme paper", imgBiggestContours)
cv2.waitKey(0) 





threshd = cv2.resize(thresh, (900, 1600)) 

cv2.imshow("gosterme", threshd)                            # Show image

#cv2.imshow("gosterme paper", imgBiggestContours)
cv2.waitKey(0) 


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
    rows = np.vsplit(threshd,40)    
    #cv2.imshow("split",rows[5])
    #cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,5)
        
        #cv2.imshow("split",cols[0])
        #cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            #cv2.imshow("split",box)
            #cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
#cv2.imshow("test",boxes[6])
#cv2.waitKey(0) 



#print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))






#cevap alma

myPixelVal=np.zeros((40,5))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(40,5)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]




sayac=0
cevap_kontrolcu=[]
for x in range (0,40):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 1700:
        #print("adanam")
        for i in range (0,5):
            kontrol=cevap_kontrolcu[i]
            #print(kontrol)
            i+=1
            if kontrol==kontrol_veri:
                #print("dogru")
                yeri=cevap_kontrolcu.index(kontrol)
                if yeri == 0:
                    gercek_cvp="a"
                elif yeri == 1:
                    gercek_cvp="b"
                elif yeri == 2:
                    gercek_cvp="c"
                elif yeri == 3:
                    gercek_cvp="d"
                elif yeri == 4:
                    gercek_cvp="e"
                
                print("%s Matematik %s sorunun cevabı:%s"%(sayac,(x+1),gercek_cvp))
                sayac+=1
    






