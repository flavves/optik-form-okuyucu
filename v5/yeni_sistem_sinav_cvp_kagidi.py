# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:22:25 2021

@author: yazılım
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:22:32 2021

@author: yazılım
"""


"""

Bionluk Yeni optik kod okuma Projesi v5 sunum


"""


import json
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import utils



path = "ornekler/1a.jpeg"

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
    #biggestContour_5=utils.getCornerPoints(rectCon[4])
    
    
    cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_2,-1,(255,200,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_4,-1,(255,0,59),20)
    #cv2.drawContours(imgBiggestContours,biggestContour_5,-1,(45,255,79),20)
    
    
    
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
    
    
    cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_2,-1,(255,200,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_4,-1,(255,0,59),20)
    cv2.drawContours(imgBiggestContours,biggestContour_5,-1,(45,255,79),20)
   
    
    #cv2.imshow("gosterme paper", imgBiggestContours)
    #cv2.waitKey(0) 


"""

Sıralama hatası çözümü

"""



print("ilk:%s \n ikinci:%s \n üçüncü:%s \n numara:%s \n"%(biggestContour_1,biggestContour_2,biggestContour_3,biggestContour_4))

siralama=[]

siralama.append(biggestContour_1[0][0][0])
siralama.append(biggestContour_2[0][0][0])
siralama.append(biggestContour_3[0][0][0])
#siralama.append(biggestContour_4[0][0][0])

siralama.sort()






if siralama[0]==biggestContour_1[0][0][0]:
    ilk_kisim=biggestContour_1
elif siralama[0] == biggestContour_2[0][0][0]:
        ilk_kisim=biggestContour_2
elif siralama[0] == biggestContour_3[0][0][0]:
        ilk_kisim=biggestContour_3



if siralama[1]==biggestContour_1[0][0][0]:
    ikinci_kisim=biggestContour_1
elif siralama[1] == biggestContour_2[0][0][0]:
        ikinci_kisim=biggestContour_2
elif siralama[1] == biggestContour_3[0][0][0]:
        ikinci_kisim=biggestContour_3


if siralama[2]==biggestContour_1[0][0][0]:
    ucuncu_kisim=biggestContour_1
elif siralama[2] == biggestContour_2[0][0][0]:
        ucuncu_kisim=biggestContour_2
elif siralama[2] == biggestContour_3[0][0][0]:
        ucuncu_kisim=biggestContour_3




"""

ilk kisim


"""



imgBiggestContours = img.copy()


biggestContour_1=ilk_kisim
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
crop_img = gray[19:1340, 42:185]
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





threshd = cv2.resize(thresh, (900, 1200)) 

#cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
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
    rows = np.vsplit(threshd,30)    
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

myPixelVal=np.zeros((30,5))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(30,5)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]





ilk_cvp_anahtari = """{  }"""
ilk_cvp_anahtari_gercek = json.loads(ilk_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,30):
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
                
                print("ilk kisim %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                ilk_cvp_anahtari_gercek[x+1] = gercek_cvp
    



"""

ikinci cevap anahtarı


"""



imgBiggestContours = img.copy()


biggestContour_1=ikinci_kisim
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
crop_img = gray[19:1340, 42:185]
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





threshd = cv2.resize(thresh, (900, 1200)) 

#cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
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
    rows = np.vsplit(threshd,30)    
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

myPixelVal=np.zeros((30,5))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(30,5)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]






cevap_kontrolcu=[]
for x in range (0,30):
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
                
                print("ikinci kisim %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                ilk_cvp_anahtari_gercek[x+31] = gercek_cvp
    



"""

ucuncu


"""



imgBiggestContours = img.copy()


biggestContour_1=ucuncu_kisim
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
crop_img = gray[35:1320, 42:181]
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





threshd = cv2.resize(thresh, (450, 600)) 

#cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
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
    rows = np.vsplit(threshd,15)    
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

myPixelVal=np.zeros((15,5))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(15,5)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]






cevap_kontrolcu=[]
for x in range (0,15):
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
                
                print("ikinci kisim %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                ilk_cvp_anahtari_gercek[x+61] = gercek_cvp
    


"""


kurum kodu


"""

imgBiggestContours = img.copy()

biggestContour_6=biggestContour_4
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
crop_img = gray[85:825, 55:375]
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
        
        

        
        #deneme
        
        
        #print("arr: ",arr)
        #print("x",x)


        if arr >=4000:
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
ogr_no = ' '.join(map(str, s)) 
  
#print(kurum_kodu_no)  
ogr_no=ogr_no.replace(" ","")


#sonuç
print("ogr_no: %s "%ogr_no)

 
"""

Json çıkarma

"""


import json

x = {
  "kurum_kodu": ilk_cvp_anahtari_gercek,
  "öğrenci_no": ogr_no,

}

sonuc_json=(json.dumps(x, ensure_ascii=False).encode('utf8'))
print("!!!!! json çıktı !!!!")
print(sonuc_json.decode())


