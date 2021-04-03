# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:55:56 2021

@author: yazılım
"""


"""

Test için gönderme


"""


# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:22:32 2021

@author: yazılım
"""


"""

Bionluk Yeni optik kod okuma Projesi


"""


import json
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



path = "ornekler/q11.jpeg"

heightImg = 700
widthImg  = 700
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
    biggestContour_10=utils.getCornerPoints(rectCon[9])
    #print("Türkçe:%s \n sosyal:%s \n matematik:%s \n fen:%s \n"%(biggestContour_5,biggestContour_2,biggestContour_4,biggestContour_3))
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
    cv2.drawContours(imgBiggestContours,biggestContour_9,-1,(255,235,99),20)
    cv2.drawContours(imgBiggestContours,biggestContour_10,-1,(0,255,0),20)
    
    
    #cv2.imshow("gosterme paper", imgBiggestContours)
    #cv2.waitKey(0) 
except:
        
    imgBiggestContours = img.copy()
    
    biggestContour_1 = utils.getCornerPoints(rectCon[0])
    
    cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
    
    biggestContour=utils.reorder(biggestContour_1)
    
    
    
    ##cv2.imshow("gosterme paper", imgBiggestContours)
    ##cv2.waitKey(0) 
        
        
    
    heightImg = 1080
    widthImg  = 720
    #imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 
    
    
    
    
    pt1= np.float32(biggestContour)
    pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix = cv2.getPerspectiveTransform(pt1,pt2)
    imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))
    
    ##cv2.imshow("cropped", imgWarpColored)
    ##cv2.waitKey(0)
    
    
    img= imgWarpColored
    
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
    
    ##cv2.imshow("gosterme paper", imgContours)
    ##cv2.waitKey(0) 
    
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
    cv2.drawContours(imgBiggestContours,biggestContour_9,-1,(255,235,99),20)
    #cv2.drawContours(imgBiggestContours,biggestContour_10,-1,(0,255,0),20)
    
    
    #cv2.imshow("gosterme paper", imgBiggestContours)
    #cv2.waitKey(0) 


"""

Sıralama hatası çözümü

"""



print("Türkçe:%s \n sosyal:%s \n matematik:%s \n fen:%s \n kurum:%s \n sınav:%s \n ogr:%s \n"%(biggestContour_1,biggestContour_2,biggestContour_3,biggestContour_4,biggestContour_5,biggestContour_6,biggestContour_7))

siralama=[]
sag_siralama=[]
siralama.append(biggestContour_1[0][0][0])
siralama.append(biggestContour_2[0][0][0])
siralama.append(biggestContour_3[0][0][0])
siralama.append(biggestContour_4[0][0][0])
sag_siralama.append(biggestContour_5[0][0][1])
sag_siralama.append(biggestContour_6[0][0][1])
sag_siralama.append(biggestContour_7[0][0][1])

siralama.sort()
sag_siralama.sort()



if sag_siralama[0]==biggestContour_5[0][0][1]:
    kurum_kisimi=biggestContour_5
elif sag_siralama[0] == biggestContour_6[0][0][1]:
        kurum_kisimi=biggestContour_6
elif sag_siralama[0] == biggestContour_7[0][0][1]:
        kurum_kisimi=biggestContour_7

if sag_siralama[1]==biggestContour_5[0][0][1]:
    sinav_kisimi=biggestContour_5
elif sag_siralama[1] == biggestContour_6[0][0][1]:
        sinav_kisimi=biggestContour_6
elif sag_siralama[1] == biggestContour_7[0][0][1]:
        sinav_kisimi=biggestContour_7


if sag_siralama[2]==biggestContour_5[0][0][1]:
    ogr_kisimi=biggestContour_5
elif sag_siralama[2] == biggestContour_6[0][0][1]:
        ogr_kisimi=biggestContour_6
elif sag_siralama[2] == biggestContour_7[0][0][1]:
        ogr_kisimi=biggestContour_7



if siralama[0]==biggestContour_1[0][0][0]:
    turkce_kisimi=biggestContour_1
elif siralama[0] == biggestContour_2[0][0][0]:
        turkce_kisimi=biggestContour_2
elif siralama[0] == biggestContour_3[0][0][0]:
        turkce_kisimi=biggestContour_3
elif siralama[0] == biggestContour_4[0][0][0]:
        turkce_kisimi=biggestContour_4

if siralama[1]==biggestContour_1[0][0][0]:
    sosyal_Kismi=biggestContour_1
elif siralama[1] == biggestContour_2[0][0][0]:
        sosyal_Kismi=biggestContour_2
elif siralama[1] == biggestContour_3[0][0][0]:
        sosyal_Kismi=biggestContour_3
elif siralama[1] == biggestContour_4[0][0][0]:
        sosyal_Kismi=biggestContour_4

if siralama[2]==biggestContour_1[0][0][0]:
    matematik_Kismi=biggestContour_1
elif siralama[2] == biggestContour_2[0][0][0]:
        matematik_Kismi=biggestContour_2
elif siralama[2] == biggestContour_3[0][0][0]:
        matematik_Kismi=biggestContour_3
elif siralama[2] == biggestContour_4[0][0][0]:
        matematik_Kismi=biggestContour_4

if siralama[3]==biggestContour_1[0][0][0]:
    fen_Kismi=biggestContour_1
elif siralama[3] == biggestContour_2[0][0][0]:
        fen_Kismi=biggestContour_2
elif siralama[3] == biggestContour_3[0][0][0]:
        fen_Kismi=biggestContour_3
elif siralama[3] == biggestContour_4[0][0][0]:
        fen_Kismi=biggestContour_4





"""

Türkçe


"""



imgBiggestContours = img.copy()


biggestContour_1=turkce_kisimi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


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
crop_img = gray[15:1363, 38:189]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)


docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (900, 1600)) 

##cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 


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
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,5)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
###cv2.imshow("test",boxes[6])
###cv2.waitKey(0) 



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





turkce_cvp_anahtari = """{  }"""
turkce_cvp_anahtari_gercek = json.loads(turkce_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,40):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 3000:
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
                turkce_cvp_anahtari_gercek[x+1] = gercek_cvp
    



"""

Sosyal


"""



imgBiggestContours = img.copy()


biggestContour_1=sosyal_Kismi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 










heightImg = 1363
widthImg  = 199
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,-5],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[15:1363, 39:189]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)


docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (900, 1600)) 

##cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 


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
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,5)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
###cv2.imshow("test",boxes[6])
###cv2.waitKey(0) 



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





sosyal_cvp_anahtari = """{  }"""
sosyal_cvp_anahtari_gercek = json.loads(sosyal_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,40):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 3000:
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
                sosyal_cvp_anahtari_gercek[x+1] = gercek_cvp





"""

Matematik


"""



imgBiggestContours = img.copy()


biggestContour_1=matematik_Kismi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 










heightImg = 1363
widthImg  = 199
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,-5],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[10:1363, 35:189]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)


docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (900, 1600)) 

##cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 


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
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,5)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
###cv2.imshow("test",boxes[6])
###cv2.waitKey(0) 



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





matematik_cvp_anahtari = """{  }"""
matematik_cvp_anahtari_gercek = json.loads(matematik_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,40):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 3000:
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
                matematik_cvp_anahtari_gercek[x+1] = gercek_cvp



"""

Fen


"""



imgBiggestContours = img.copy()


biggestContour_1=fen_Kismi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


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
crop_img = gray[15:1363, 35:189]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)


docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (900, 1600)) 

##cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 


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
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,5)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
###cv2.imshow("test",boxes[6])
###cv2.waitKey(0) 



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





fen_cvp_anahtari = """{  }"""
fen_cvp_anahtari_gercek = json.loads(fen_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,40):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 3000:
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
                
                print("Fen %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                fen_cvp_anahtari_gercek[x+1] = gercek_cvp




"""


kurum kodu


"""

imgBiggestContours = img.copy()

biggestContour_6=kurum_kisimi
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
crop_img = gray[140:825, 55:370]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)







docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (700, 1000)) 

##cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 






def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,10)    
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,7)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
###cv2.imshow("test",boxes[6])
###cv2.waitKey(0) 



#print(cv2.countNonZero(boxes[14]),cv2.countNonZero(boxes[9]))








#cevap alma

myPixelVal=np.zeros((10,7))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(10,7)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[3][3]


HaydiBakalim=myPixelVal[0][0]



sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[]
for deneme in range (0,7):

    for x in range(0,10):
        
        arr=myPixelVal[x][deneme]
        print(arr)
        
        

        
        #deneme
        
        
        #print("arr: ",arr)
        #print("x",x)


        if arr >=5000:
                  if x==0:
                      numara_kontrolcu.append(0)
                  elif x== 1:
                      numara_kontrolcu.append(1)
                  elif x== 2:
                      numara_kontrolcu.append(2)
                  elif x== 3:
                      numara_kontrolcu.append(3)
                  elif x== 4:
                      numara_kontrolcu.append(4)
                  elif x== 5:
                      numara_kontrolcu.append(5)
                  elif x== 6:
                      numara_kontrolcu.append(6)
                  elif x== 7:
                      numara_kontrolcu.append(7)
                  elif x== 8:
                      numara_kontrolcu.append(8)
                  elif x== 9:
                      numara_kontrolcu.append(9)






s = numara_kontrolcu
  
# using list comprehension 
kurum_kodu_no = ' '.join(map(str, s)) 
  
#print(kurum_kodu_no)  
kurum_kodu_no=kurum_kodu_no.replace(" ","")


#sonuç
print("kurum kodu no: %s "%kurum_kodu_no)






"""


Sınav Kodu


"""

imgBiggestContours = img.copy()

biggestContour_6=sinav_kisimi
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
crop_img = gray[130:825, 55:370]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)







docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (700, 1000)) 

##cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 






def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,10)    
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,7)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
##cv2.imshow("test",boxes[5])
##cv2.waitKey(0) 


"""
colored = imgWarpColored[130:825, 55:370]
colored = cv2.resize(colored, (350, 500)) 
deneme= colored.copy()
deneme= colored.copy()



soldan_saga=[25,77,129,181,233,285,337]
yukaridan_asagi=[20,70,120,170,220,270,320,370,420,470]


for i in range(0,7):
    for a in range(0,10):
        center_coordinates = (soldan_saga[i], yukaridan_asagi[a])
    

        
        # Radius of circle
        radius = 19
          
        # Blue color in BGR
        color = (0,250,0)
          
        # Line thickness of 2 px
        thickness = 2
          
        # Using cv2.circle() method
        # Draw a circle with blue line borders of thickness of 2 px
        
        image = cv2.circle(deneme, center_coordinates, radius, color, thickness)
          
        # Displaying the image 
#cv2.imshow("adana", image) 
#cv2.waitKey(0) 
        #print(cv2.countNonZero(boxes[14]),cv2.countNonZero(boxes[9]))
        
    
"""




#cevap alma

myPixelVal=np.zeros((10,7))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(10,7)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[3][3]


HaydiBakalim=myPixelVal[0][0]
"""
colored = imgWarpColored[130:825, 55:370]
colored = cv2.resize(colored, (350, 500)) 
deneme= colored.copy()
deneme= colored.copy()
soldan_saga=[25,77,129,181,233,285,337]
yukaridan_asagi=[20,70,120,170,220,270,320,370,420,470]
radius = 19
color = (0,250,0)
thickness = 2

"""            
center_coordinates=[]

sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[]
for deneme in range (0,7):

    for x in range(0,10):
        
        arr=myPixelVal[x][deneme]
        #print(arr)
        #print("arr: ",arr)
        #print("x",x)


        if arr >=5000:
                  #center_coordinates.append((soldan_saga[deneme],yukaridan_asagi[x]))
                  if x==0:
                      numara_kontrolcu.append(0)
                  elif x== 1:
                      numara_kontrolcu.append(1)
                  elif x== 2:
                      numara_kontrolcu.append(2)
                  elif x== 3:
                      numara_kontrolcu.append(3)
                  elif x== 4:
                      numara_kontrolcu.append(4)
                  elif x== 5:
                      numara_kontrolcu.append(5)
                  elif x== 6:
                      numara_kontrolcu.append(6)
                  elif x== 7:
                      numara_kontrolcu.append(7)
                  elif x== 8:
                      numara_kontrolcu.append(8)
                  elif x== 9:
                      numara_kontrolcu.append(9)
                      
                  





s = numara_kontrolcu
  
# using list comprehension 
sınav_kodu_no = ' '.join(map(str, s)) 
  
#print(kurum_kodu_no)  
sınav_kodu_no=sınav_kodu_no.replace(" ","")


#sonuç
print("sınav kodu no: %s "%sınav_kodu_no)
"""
colored = imgWarpColored[130:825, 55:370]
colored = cv2.resize(colored, (350, 500)) 
sinavkodu_deneme= colored.copy()

#halka çizdirme
for i in center_coordinates:
    print(i)
    image = cv2.circle(sinavkodu_deneme, i, radius, color, thickness)


"""





"""


Öğrenci no


"""

imgBiggestContours = img.copy()

biggestContour_6=ogr_kisimi
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
crop_img = gray[130:825, 55:370]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)







docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


#cv2.imshow("gosterme", thresh)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 





threshd = cv2.resize(thresh, (700, 1000)) 

##cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 






def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,10)    
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,7)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
###cv2.imshow("test",boxes[6])
###cv2.waitKey(0) 



#print(cv2.countNonZero(boxes[14]),cv2.countNonZero(boxes[9]))








#cevap alma

myPixelVal=np.zeros((10,7))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(10,7)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[3][3]


HaydiBakalim=myPixelVal[0][0]







sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[]
for deneme in range (0,7):

    for x in range(0,10):
        
        arr=myPixelVal[x][deneme]
        
        
        
        #print(arr)
        #print("arr: ",arr)
        #print("x",x)


        if arr >=5000:
                  if x==0:
                      numara_kontrolcu.append(0)
                  elif x== 1:
                      numara_kontrolcu.append(1)
                  elif x== 2:
                      numara_kontrolcu.append(2)
                  elif x== 3:
                      numara_kontrolcu.append(3)
                  elif x== 4:
                      numara_kontrolcu.append(4)
                  elif x== 5:
                      numara_kontrolcu.append(5)
                  elif x== 6:
                      numara_kontrolcu.append(6)
                  elif x== 7:
                      numara_kontrolcu.append(7)
                  elif x== 8:
                      numara_kontrolcu.append(8)
                  elif x== 9:
                      numara_kontrolcu.append(9)






s = numara_kontrolcu
  
# using list comprehension 
ogr_kodu_no = ' '.join(map(str, s)) 
  
#print(kurum_kodu_no)  
ogr_kodu_no=ogr_kodu_no.replace(" ","")


#sonuç
print("öğrenci kodu no: %s "%ogr_kodu_no)


 
"""

Json çıkarma

"""

"""

40 hatası çözümü



"""



adana=matematik_cvp_anahtari_gercek.keys()
badana=turkce_cvp_anahtari_gercek.keys()

kadana=sosyal_cvp_anahtari_gercek.keys()
badanama=fen_cvp_anahtari_gercek.keys()

if len(adana) <= 2:
    matematik_cvp_anahtari = """{  }"""
    matematik_cvp_anahtari_gercek = json.loads(matematik_cvp_anahtari)

if len(badana) <= 2:
    turkce_cvp_anahtari = """{  }"""
    turkce_cvp_anahtari_gercek = json.loads(turkce_cvp_anahtari)

if len(kadana) <= 2:
    sosyal_cvp_anahtari = """{  }"""
    sosyal_cvp_anahtari_gercek = json.loads(sosyal_cvp_anahtari)
    
if len(badanama) <= 2:
    fen_cvp_anahtari = """{  }"""
    fen_cvp_anahtari_gercek = json.loads(fen_cvp_anahtari)
    
import json

x = {
  "kurum_kodu": kurum_kodu_no,
  "sınav_kodu": sınav_kodu_no,
  "ogr_no": ogr_kodu_no,
  "matematik": matematik_cvp_anahtari_gercek,
  "türkçe": turkce_cvp_anahtari_gercek,
  "sosyal": sosyal_cvp_anahtari_gercek,
  "fen": fen_cvp_anahtari_gercek,

}

sonuc_json=(json.dumps(x, ensure_ascii=False).encode('utf8'))
print("!!!!! json çıktı !!!!")
print(sonuc_json.decode())


