# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:54:59 2021

@author: yazılım
"""


"""

Hepsi


"""



from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import utils



sozluk={"0":"a",
"1":"b",
"2":"c",
"3":"ç",
"4":"d",
"5":"e",
"6":"f",
"7":"g",
"8":"ğ",
"9":"h",
"10":"ı",
"11":"i",
"12":"j",
"13":"k",
"14":"l",
"15":"m",
"16":"n",
"17":"o",
"18":"ö",
"19":"p",
"20":"r",
"21":"s",
"22":"ş",
"23":"t",
"24":"u",
"25":"ü",
"26":"v",
"27":"y",
"28":"z"}



path = "bionluk.jpg"

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
#biggestContour_9=utils.getCornerPoints(rectCon[8])
#Kitapçık
biggestContour_10=utils.getCornerPoints(rectCon[9])

#print(len(biggestContour))
#print(biggestContour)
#print(gradePoints)

cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
cv2.drawContours(imgBiggestContours,biggestContour_2,-1,(255,200,0),20)
cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)
cv2.drawContours(imgBiggestContours,biggestContour_4,-1,(255,0,59),20)
cv2.drawContours(imgBiggestContours,biggestContour_5,-1,(45,255,79),20)
cv2.drawContours(imgBiggestContours,biggestContour_6,-1,(255,99,67),20)
cv2.drawContours(imgBiggestContours,biggestContour_7,-1,(89,255,98),20)
cv2.drawContours(imgBiggestContours,biggestContour_8,-1,(0,255,0),20)
#cv2.drawContours(imgBiggestContours,biggestContour_9,-1,(255,235,99),20)
cv2.drawContours(imgBiggestContours,biggestContour_10,-1,(0,255,0),20)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 

"""

ad soyad


"""

imgBiggestContours = img.copy()

biggestContour_1 = utils.getCornerPoints(rectCon[0])

cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)

biggestContour=utils.reorder(biggestContour_1)



#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 



heightImg = 860
widthImg  = 400
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))

#cv2.imshow("cropped", imgWarpColored)
#cv2.waitKey(0)


gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[10:840, 20:390]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)







docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (1500, 2900)) 

#cv2.imshow("gosterme", threshd)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 



def splitBoxes(img):
        
    rows = np.hsplit(img,15)
    boxes =[]
    for r in rows:
        cols = np.vsplit(r,29)
        for box in cols:
            boxes.append(box)
            ##cv2.imshow("split",box)
            ##cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
##cv2.imshow("test",boxes[3])

#print(cv2.countNonZero(boxes[1]),cv2.countNonZero(boxes[5]))
##cv2.waitKey(0) 
#cols = np.hsplit(thresh,15)   
##cv2.imshow("split",cols[10])
##cv2.waitKey(0) 

#cevap alma

myPixelVal=np.zeros((15,29))

countC=0
countR=0

for image in boxes:
    totalPixels = cv2.countNonZero(image)
    myPixelVal[countC][countR]=totalPixels
    countR +=1
    if (countR==29):countC +=1 ;countR=0
#print(myPixelVal)
#şimdi burada 1000 altındakileri alma beynim yandı sabah devam etcem 
"""

Ne yaptım şimdi sonuç tamam
isim çıkarcaz bu da uzun olcak mantığını kavra ve 1000 altındakileri alma dikkat et uyudum ben iyi geceler
video 1:10:34 kaldın


"""
myIndex= []
harfler=[]
for x in range (0,15):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr==np.amax(arr)
    kontrol_veri=arr[0]
    if kontrol_veri >= 4000: 
        myIndexVal=np.where(arr==np.amax(arr))
        #print(myIndexVal[0])
        harfler.append(myIndexVal[0][0])

adi_soyadi=[]
for i in range (0,len(harfler)):
    #print(i)
    haf_bul=harfler[i]
    
    adi_soyadi.append(sozluk[str(haf_bul)])
print(adi_soyadi)




"""


kurum kodu


"""

imgBiggestContours = img.copy()

biggestContour_6=utils.getCornerPoints(rectCon[5])
cv2.drawContours(imgBiggestContours,biggestContour_6,-1,(255,99,67),20)


biggestContour=utils.reorder(biggestContour_6)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 







heightImg = 860
widthImg  = 400
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[10,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))

#cv2.imshow("cropped", imgWarpColored)
#cv2.waitKey(0)


gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[170:810, 33:380]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)







docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (900, 1100)) 

#cv2.imshow("gosterme", threshd)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 






def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,11)    
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,9)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ##cv2.imshow("split",box)
            ##cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
##cv2.imshow("test",boxes[6])
##cv2.waitKey(0) 



#print(cv2.countNonZero(boxes[14]),cv2.countNonZero(boxes[9]))








#cevap alma

myPixelVal=np.zeros((11,9))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(11,9)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[3][3]






sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[0,0,0,0,0,0,0,0,0]
for x in range (0,11):

    for deneme in range(0,9):
        
        arr=myPixelVal[x][deneme]
        #print(arr)
        #print("arr: ",arr)
        #print("x",x)


        if arr >=2000:       
            #print(arr)
            if arr >=2000:
                print(arr)
                if x==0:           
                    if deneme==0:
                        numara_kontrolcu[0]=0
                    elif deneme==1:
                        numara_kontrolcu[1]=0
                    elif deneme==2:
                        numara_kontrolcu[2]=0
                    elif deneme==3:
                        numara_kontrolcu[3]=0
                    elif deneme==4:
                        numara_kontrolcu[4]=0
                    elif deneme==5:
                        numara_kontrolcu[5]=0
                    elif deneme==6:
                        numara_kontrolcu[6]=0
                    elif deneme==7:
                        numara_kontrolcu[7]=0
                    elif deneme==8:
                        numara_kontrolcu[5]=0
                    elif deneme==9:
                        numara_kontrolcu[6]=0
                    elif deneme==10:
                        numara_kontrolcu[7]=0

       
                    
                elif x==1:      
                    if deneme==0:
                        numara_kontrolcu[0]=0
                    elif deneme==1:
                        numara_kontrolcu[1]=0
                    elif deneme==2:
                        numara_kontrolcu[2]=0
                    elif deneme==3:
                        numara_kontrolcu[3]=0
                    elif deneme==4:
                        numara_kontrolcu[4]=0
                    elif deneme==5:
                        numara_kontrolcu[5]=0
                    elif deneme==6:
                        numara_kontrolcu[6]=0
                    elif deneme==7:
                        numara_kontrolcu[7]=0
                    elif deneme==8:
                        numara_kontrolcu[5]=0
                    elif deneme==9:
                        numara_kontrolcu[6]=0
                    elif deneme==10:
                        numara_kontrolcu[7]=0
                    
                    
                elif x==2:                    
                 
                    if deneme==0:
                        numara_kontrolcu[0]=1
                    elif deneme==1:
                        numara_kontrolcu[1]=1
                    elif deneme==2:
                        numara_kontrolcu[2]=1
                    elif deneme==3:
                        numara_kontrolcu[3]=1
                    elif deneme==4:
                        numara_kontrolcu[4]=1
                    elif deneme==5:
                        numara_kontrolcu[5]=1
                    elif deneme==6:
                        numara_kontrolcu[6]=1
                    elif deneme==7:
                        numara_kontrolcu[7]=1
                    elif deneme==8:
                        numara_kontrolcu[5]=1
                    elif deneme==9:
                        numara_kontrolcu[6]=1
                    elif deneme==10:
                        numara_kontrolcu[7]=1
                elif x==3:                    
            
                    if deneme==0:
                        numara_kontrolcu[0]=2
                    elif deneme==1:
                        numara_kontrolcu[1]=2
                    elif deneme==2:
                        numara_kontrolcu[2]=2
                    elif deneme==3:
                        numara_kontrolcu[3]=2
                    elif deneme==4:
                        numara_kontrolcu[4]=2
                    elif deneme==5:
                        numara_kontrolcu[5]=2
                    elif deneme==6:
                        numara_kontrolcu[6]=2
                    elif deneme==7:
                        numara_kontrolcu[7]=2
                    elif deneme==8:
                        numara_kontrolcu[5]=2
                    elif deneme==9:
                        numara_kontrolcu[6]=2
                    elif deneme==10:
                        numara_kontrolcu[7]=2
                elif x==4:                    
                
                    if deneme==0:
                        numara_kontrolcu[0]=3
                    elif deneme==1:
                        numara_kontrolcu[1]=3
                    elif deneme==2:
                        numara_kontrolcu[2]=3
                    elif deneme==3:
                        numara_kontrolcu[3]=3
                    elif deneme==4:
                        numara_kontrolcu[4]=3
                    elif deneme==5:
                        numara_kontrolcu[5]=3
                    elif deneme==6:
                        numara_kontrolcu[6]=3
                    elif deneme==7:
                        numara_kontrolcu[7]=3
                    elif deneme==8:
                        numara_kontrolcu[5]=3
                    elif deneme==9:
                        numara_kontrolcu[6]=3
                    elif deneme==10:
                        numara_kontrolcu[7]=3
                elif x==5:                    
                
                    if deneme==0:
                        numara_kontrolcu[0]=4
                    elif deneme==1:
                        numara_kontrolcu[1]=4
                    elif deneme==2:
                        numara_kontrolcu[2]=4
                    elif deneme==3:
                        numara_kontrolcu[3]=4
                    elif deneme==4:
                        numara_kontrolcu[4]=4
                    elif deneme==5:
                        numara_kontrolcu[5]=4
                    elif deneme==6:
                        numara_kontrolcu[6]=4
                    elif deneme==7:
                        numara_kontrolcu[7]=4
                    elif deneme==8:
                        numara_kontrolcu[5]=4
                    elif deneme==9:
                        numara_kontrolcu[6]=4
                    elif deneme==10:
                        numara_kontrolcu[7]=4
                elif x==6:                    
                   
                    if deneme==0:
                        numara_kontrolcu[0]=5
                    elif deneme==1:
                        numara_kontrolcu[1]=5
                    elif deneme==2:
                        numara_kontrolcu[2]=5
                    elif deneme==3:
                        numara_kontrolcu[3]=5
                    elif deneme==4:
                        numara_kontrolcu[4]=5
                    elif deneme==5:
                        numara_kontrolcu[5]=5
                    elif deneme==6:
                        numara_kontrolcu[6]=5
                    elif deneme==7:
                        numara_kontrolcu[7]=5
                    elif deneme==8:
                        numara_kontrolcu[5]=5
                    elif deneme==9:
                        numara_kontrolcu[6]=5
                    elif deneme==10:
                        numara_kontrolcu[7]=5
                elif x==7:                    
                  
                    if deneme==0:
                        numara_kontrolcu[0]=6
                    elif deneme==1:
                        numara_kontrolcu[1]=6
                    elif deneme==2:
                        numara_kontrolcu[2]=6
                    elif deneme==3:
                        numara_kontrolcu[3]=6
                    elif deneme==4:
                        numara_kontrolcu[4]=6
                    elif deneme==5:
                        numara_kontrolcu[5]=6
                    elif deneme==6:
                        numara_kontrolcu[6]=6
                    elif deneme==7:
                        numara_kontrolcu[7]=6
                    elif deneme==8:
                        numara_kontrolcu[5]=6
                    elif deneme==9:
                        numara_kontrolcu[6]=6
                    elif deneme==10:
                        numara_kontrolcu[7]=6
                elif x==8:                    
                    
                    if deneme==0:
                        numara_kontrolcu[0]=7
                    elif deneme==1:
                        numara_kontrolcu[1]=7
                    elif deneme==2:
                        numara_kontrolcu[2]=7
                    elif deneme==3:
                        numara_kontrolcu[3]=7
                    elif deneme==4:
                        numara_kontrolcu[4]=7
                    elif deneme==5:
                        numara_kontrolcu[5]=7
                    elif deneme==6:
                        numara_kontrolcu[6]=7
                    elif deneme==7:
                        numara_kontrolcu[7]=7
                    elif deneme==8:
                        numara_kontrolcu[5]=7
                    elif deneme==9:
                        numara_kontrolcu[6]=7
                    elif deneme==10:
                        numara_kontrolcu[7]=7
                elif x==9:                    
                  
                    if deneme==0:
                        numara_kontrolcu[0]=8
                    elif deneme==1:
                        numara_kontrolcu[1]=8
                    elif deneme==2:
                        numara_kontrolcu[2]=8
                    elif deneme==3:
                        numara_kontrolcu[3]=8
                    elif deneme==4:
                        numara_kontrolcu[4]=8
                    elif deneme==5:
                        numara_kontrolcu[5]=8
                    elif deneme==6:
                        numara_kontrolcu[6]=8
                    elif deneme==7:
                        numara_kontrolcu[7]=8
                    elif deneme==8:
                        numara_kontrolcu[5]=8
                    elif deneme==9:
                        numara_kontrolcu[6]=8
                    elif deneme==10:
                        numara_kontrolcu[7]=8

                elif x==10:                    
                   
                    if deneme==0:
                        numara_kontrolcu[0]=9
                    elif deneme==1:
                        numara_kontrolcu[1]=9
                    elif deneme==2:
                        numara_kontrolcu[2]=9
                    elif deneme==3:
                        numara_kontrolcu[3]=9
                    elif deneme==4:
                        numara_kontrolcu[4]=9
                    elif deneme==5:
                        numara_kontrolcu[5]=9
                    elif deneme==6:
                        numara_kontrolcu[6]=9
                    elif deneme==7:
                        numara_kontrolcu[7]=9
                    elif deneme==8:
                        numara_kontrolcu[5]=9
                    elif deneme==9:
                        numara_kontrolcu[6]=9
                    elif deneme==10:
                        numara_kontrolcu[7]=9

s = numara_kontrolcu
  
# using list comprehension 
kurum_kodu_no = ' '.join(map(str, s)) 
  
print(kurum_kodu_no)  
kurum_kodu_no=kurum_kodu_no.replace(" ","")
print("kurum kodu no: %s "%kurum_kodu_no)







"""

Sınav kodu

"""

imgBiggestContours = img.copy()


biggestContour_7=utils.getCornerPoints(rectCon[6])
cv2.drawContours(imgBiggestContours,biggestContour_7,-1,(89,255,98),20)


biggestContour=utils.reorder(biggestContour_7)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 









heightImg = 860
widthImg  = 400
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[10,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))

#cv2.imshow("cropped", imgWarpColored)
#cv2.waitKey(0)


gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[180:810, 45:360]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)




docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (700, 1100)) 

#cv2.imshow("gosterme", threshd)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 






def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,11)    
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,7)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ##cv2.imshow("split",box)
            ##cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
##cv2.imshow("test",boxes[6])
##cv2.waitKey(0) 



print(cv2.countNonZero(boxes[14]),cv2.countNonZero(boxes[9]))








#cevap alma

myPixelVal=np.zeros((11,7))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(11,7)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[3][3]







myPixelVal[10][2]



sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[0,0,0,0,0,0,0]
for x in range (0,11):

    for deneme in range(0,7):
        
        arr=myPixelVal[x][deneme]
        #print(arr)
        #print("arr: ",arr)
        #print("x",x)


        if arr >=2000:       
            #print(arr)
            if arr >=2000:
                print(arr)
                if x==0:           
                    if deneme==0:
                        numara_kontrolcu[0]=0
                    elif deneme==1:
                        numara_kontrolcu[1]=0
                    elif deneme==2:
                        numara_kontrolcu[2]=0
                    elif deneme==3:
                        numara_kontrolcu[3]=0
                    elif deneme==4:
                        numara_kontrolcu[4]=0
                    elif deneme==5:
                        numara_kontrolcu[5]=0
                    elif deneme==6:
                        numara_kontrolcu[6]=0
                    elif deneme==7:
                        numara_kontrolcu[7]=0

       
                    
                elif x==1:      
                    if deneme==0:
                        numara_kontrolcu[0]=0
                    elif deneme==1:
                        numara_kontrolcu[1]=0
                    elif deneme==2:
                        numara_kontrolcu[2]=0
                    elif deneme==3:
                        numara_kontrolcu[3]=0
                    elif deneme==4:
                        numara_kontrolcu[4]=0
                    elif deneme==5:
                        numara_kontrolcu[5]=0
                    elif deneme==6:
                        numara_kontrolcu[6]=0
                    elif deneme==7:
                        numara_kontrolcu[7]=0
                    
                    
                elif x==2:                    
                 
                    if deneme==0:
                        numara_kontrolcu[0]=1
                    elif deneme==1:
                        numara_kontrolcu[1]=1
                    elif deneme==2:
                        numara_kontrolcu[2]=1
                    elif deneme==3:
                        numara_kontrolcu[3]=1
                    elif deneme==4:
                        numara_kontrolcu[4]=1
                    elif deneme==5:
                        numara_kontrolcu[5]=1
                    elif deneme==6:
                        numara_kontrolcu[6]=1
                    elif deneme==7:
                        numara_kontrolcu[7]=1
                elif x==3:                    
            
                    if deneme==0:
                        numara_kontrolcu[0]=2
                    elif deneme==1:
                        numara_kontrolcu[1]=2
                    elif deneme==2:
                        numara_kontrolcu[2]=2
                    elif deneme==3:
                        numara_kontrolcu[3]=2
                    elif deneme==4:
                        numara_kontrolcu[4]=2
                    elif deneme==5:
                        numara_kontrolcu[5]=2
                    elif deneme==6:
                        numara_kontrolcu[6]=2
                    elif deneme==7:
                        numara_kontrolcu[7]=2
                elif x==4:                    
                
                    if deneme==0:
                        numara_kontrolcu[0]=3
                    elif deneme==1:
                        numara_kontrolcu[1]=3
                    elif deneme==2:
                        numara_kontrolcu[2]=3
                    elif deneme==3:
                        numara_kontrolcu[3]=3
                    elif deneme==4:
                        numara_kontrolcu[4]=3
                    elif deneme==5:
                        numara_kontrolcu[5]=3
                    elif deneme==6:
                        numara_kontrolcu[6]=3
                    elif deneme==7:
                        numara_kontrolcu[7]=3
                elif x==5:                    
                
                    if deneme==0:
                        numara_kontrolcu[0]=4
                    elif deneme==1:
                        numara_kontrolcu[1]=4
                    elif deneme==2:
                        numara_kontrolcu[2]=4
                    elif deneme==3:
                        numara_kontrolcu[3]=4
                    elif deneme==4:
                        numara_kontrolcu[4]=4
                    elif deneme==5:
                        numara_kontrolcu[5]=4
                    elif deneme==6:
                        numara_kontrolcu[6]=4
                    elif deneme==7:
                        numara_kontrolcu[7]=4
                elif x==6:                    
                   
                    if deneme==0:
                        numara_kontrolcu[0]=5
                    elif deneme==1:
                        numara_kontrolcu[1]=5
                    elif deneme==2:
                        numara_kontrolcu[2]=5
                    elif deneme==3:
                        numara_kontrolcu[3]=5
                    elif deneme==4:
                        numara_kontrolcu[4]=5
                    elif deneme==5:
                        numara_kontrolcu[5]=5
                    elif deneme==6:
                        numara_kontrolcu[6]=5
                    elif deneme==7:
                        numara_kontrolcu[7]=5
                elif x==7:                    
                  
                    if deneme==0:
                        numara_kontrolcu[0]=6
                    elif deneme==1:
                        numara_kontrolcu[1]=6
                    elif deneme==2:
                        numara_kontrolcu[2]=6
                    elif deneme==3:
                        numara_kontrolcu[3]=6
                    elif deneme==4:
                        numara_kontrolcu[4]=6
                    elif deneme==5:
                        numara_kontrolcu[5]=6
                    elif deneme==6:
                        numara_kontrolcu[6]=6
                    elif deneme==7:
                        numara_kontrolcu[7]=6
                elif x==8:                    
                    
                    if deneme==0:
                        numara_kontrolcu[0]=7
                    elif deneme==1:
                        numara_kontrolcu[1]=7
                    elif deneme==2:
                        numara_kontrolcu[2]=7
                    elif deneme==3:
                        numara_kontrolcu[3]=7
                    elif deneme==4:
                        numara_kontrolcu[4]=7
                    elif deneme==5:
                        numara_kontrolcu[5]=7
                    elif deneme==6:
                        numara_kontrolcu[6]=7
                    elif deneme==7:
                        numara_kontrolcu[7]=7
                elif x==9:                    
                  
                    if deneme==0:
                        numara_kontrolcu[0]=8
                    elif deneme==1:
                        numara_kontrolcu[1]=8
                    elif deneme==2:
                        numara_kontrolcu[2]=8
                    elif deneme==3:
                        numara_kontrolcu[3]=8
                    elif deneme==4:
                        numara_kontrolcu[4]=8
                    elif deneme==5:
                        numara_kontrolcu[5]=8
                    elif deneme==6:
                        numara_kontrolcu[6]=8
                    elif deneme==7:
                        numara_kontrolcu[7]=8
                elif x==10:                    
                   
                    if deneme==0:
                        numara_kontrolcu[0]=9
                    elif deneme==1:
                        numara_kontrolcu[1]=9
                    elif deneme==2:
                        numara_kontrolcu[2]=9
                    elif deneme==3:
                        numara_kontrolcu[3]=9
                    elif deneme==4:
                        numara_kontrolcu[4]=9
                    elif deneme==5:
                        numara_kontrolcu[5]=9
                    elif deneme==6:
                        numara_kontrolcu[6]=9
                    elif deneme==7:
                        numara_kontrolcu[7]=9

s = numara_kontrolcu
  
# using list comprehension 
sınav_kodu_no = ' '.join(map(str, s)) 
  
print(sınav_kodu_no)  
sınav_kodu_no=sınav_kodu_no.replace(" ","")
print("sınav kodu no: %s "%sınav_kodu_no)
                
    











"""

oğrenci no

"""

imgBiggestContours = img.copy()
#ögr no

biggestContour_8=utils.getCornerPoints(rectCon[7])

cv2.drawContours(imgBiggestContours,biggestContour_8,-1,(0,255,0),20)


biggestContour=utils.reorder(biggestContour_8)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 







heightImg = 860
widthImg  = 400
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[10,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))

#cv2.imshow("cropped", imgWarpColored)
#cv2.waitKey(0)


gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[180:810, 45:360]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)




docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (600, 1100)) 

#cv2.imshow("gosterme", threshd)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 






def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,11)    
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,6)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ##cv2.imshow("split",box)
            ##cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
##cv2.imshow("test",boxes[6])
##cv2.waitKey(0) 



print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))






#cevap alma

myPixelVal=np.zeros((11,6))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(11,6)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[3][3]










sayac=0
cevap_kontrolcu=[]
numara_kontrolcu=[]
for x in range (0,11):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    for i in cevap_kontrolcu:
        print(i)
        if i >=2500:
            if x==1:                    
                sayac +=1
                numara_kontrolcu.append(0)
            elif x==2:                    
                sayac +=1
                numara_kontrolcu.append(1)
            elif x==3:                    
                sayac +=1
                numara_kontrolcu.append(2)
            elif x==4:                    
                sayac +=1
                numara_kontrolcu.append(3)
            elif x==5:                    
                sayac +=1
                numara_kontrolcu.append(4)
            elif x==6:                    
                sayac +=1
                numara_kontrolcu.append(5)
            elif x==7:                    
                sayac +=1
                numara_kontrolcu.append(6)
            elif x==8:                    
                sayac +=1
                numara_kontrolcu.append(7)
            elif x==9:                    
                sayac +=1
                numara_kontrolcu.append(8)
            elif x==10:                    
                sayac +=1
                numara_kontrolcu.append(9)
            elif x==11:                    
                sayac +=1
                numara_kontrolcu.append(10)


s = numara_kontrolcu
  
# using list comprehension 
ogr_numara_sonuc = ' '.join(map(str, s)) 
  
print(ogr_numara_sonuc)  
ogr_numara_sonuc=ogr_numara_sonuc.replace(" ","")
print("ogrenci no: %s "%ogr_numara_sonuc)
                
    

















"""

Fen

"""

imgBiggestContours = img.copy()

#fen kısmı
biggestContour_3=utils.getCornerPoints(rectCon[2])
cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)





biggestContour=utils.reorder(biggestContour_3)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 











heightImg = 1363
widthImg  = 199
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[22:1363, 39:185]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)


docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (900, 1600)) 

#cv2.imshow("gosterme", threshd)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


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
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,5)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ##cv2.imshow("split",box)
            ##cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
##cv2.imshow("test",boxes[6])
##cv2.waitKey(0) 



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
                
                print("%s Fen %s sorunun cevabı:%s"%(sayac,(x+1),gercek_cvp))
                sayac+=1
    
































"""

Matematik

"""
imgBiggestContours = img.copy()

#matematik
biggestContour_4=utils.getCornerPoints(rectCon[3])
cv2.drawContours(imgBiggestContours,biggestContour_4,-1,(255,0,59),20)



biggestContour=utils.reorder(biggestContour_4)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 










heightImg = 1363
widthImg  = 199
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[29:1363, 39:183]
#♥#cv2.imshow("cropped", crop_img)
##cv2.waitKey(0)


docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (900, 1600)) 

#cv2.imshow("gosterme", threshd)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


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
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,5)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ##cv2.imshow("split",box)
            ##cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
##cv2.imshow("test",boxes[6])
##cv2.waitKey(0) 



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





cevap_kontrolcu=[]
for x in range (0,40):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 2000:
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
                
                print("Matematik %s sorunun cevabı:%s"%((x+1),gercek_cvp))
    
































"""

Sosyal

"""

imgBiggestContours = img.copy()


#sosyal kısmı
biggestContour_2 = utils.getCornerPoints(rectCon[1])

cv2.drawContours(imgBiggestContours,biggestContour_2,-1,(255,200,0),20)



biggestContour=utils.reorder(biggestContour_2)


##cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 





heightImg = 1363
widthImg  = 199
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[29:1363, 39:180]
##cv2.imshow("cropped", crop_img)
##cv2.waitKey(0)


docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (900, 1600)) 

#cv2.imshow("gosterme", threshd)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


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
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,5)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ##cv2.imshow("split",box)
            ##cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
##cv2.imshow("test",boxes[6])
##cv2.waitKey(0) 



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





cevap_kontrolcu=[]
for x in range (0,40):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 2000:
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
                
                print("Sosyal %s sorunun cevabı:%s"%((x+1),gercek_cvp))
    
















"""
Türkçe

"""
#imgBiggestContours = img.copy()
biggestContour_5=utils.getCornerPoints(rectCon[4])
cv2.drawContours(imgBiggestContours,biggestContour_5,-1,(255,0,59),20)


biggestContour=utils.reorder(biggestContour_5)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 

heightImg = 1363
widthImg  = 199
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[29:1363, 39:193]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)

docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 



#cv2.imshow("gosterme", thresh)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 

#threshd = cv2.resize(thresh, (450, 800)) 

threshd = cv2.resize(thresh, (900, 1600)) 

#cv2.imshow("gosterme", threshd)                            # Show image

##cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


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
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,5)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ##cv2.imshow("split",box)
            ##cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
#cv2.imshow("test",boxes[2])
#cv2.waitKey(0) 



print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))



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
cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

myPixelVal[35][4]



cevap_anahtari_turkce=[]
tr_a=[]
cevap_kontrolcu=[]
for x in range (0,40):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 2000:
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
                
                print("Türkçe %s sorunun cevabı:%s"%((x+1),gercek_cvp))
    
