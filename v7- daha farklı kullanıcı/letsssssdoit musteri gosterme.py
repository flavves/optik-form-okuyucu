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

path_isaret = r'ornekler/yeni.jpeg'
   

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


path = r'ornekler/kare/5.jpeg'

heightImg = 700
widthImg  = 700
try:
        
    img= cv2.imread(path)
    
    #hazırlık ^^^^^^^^^^^^
    img= cv2.resize(img,(widthImg,heightImg))
    
    cv2.imshow("Sonuç",img)
    cv2.waitKey(0) 
    
    imgContours = img.copy()
    imgBiggestContours = img.copy()
    
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,10,50)
    
    contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours,contours,-1,(0,255,0),10)
    rectCon= utils.rectContour(contours)
    
    cv2.imshow("Sonuç",imgContours)
    cv2.waitKey(0) 

    
    #ad-soyad kısmı
    biggestContour_1 = utils.getCornerPoints(rectCon[0])
    #sosyal kısmı
    biggestContour_2 = utils.getCornerPoints(rectCon[1])
    #fen kısmı
    biggestContour_3=utils.getCornerPoints(rectCon[2])
   
    
    cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_2,-1,(255,200,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)
   
    #cv2.drawContours(imgBiggestContours,biggestContour_10,-1,(0,255,0),20)

    cv2.imshow("Sonuç",imgBiggestContours)
    cv2.waitKey(0) 


except:
        
    pass



"""

Sıralama hatası çözümü

"""



#print("Türkçe:%s \n inkılap:%s \n din:%s \n yabancı dil:%s \n mat:%s \n fen:%s \n ogr:%s \n"%(biggestContour_1,biggestContour_2,biggestContour_3,biggestContour_4,biggestContour_5,biggestContour_6,biggestContour_7))

     


"""

Başlayalım


"""





imgBiggestContours = img.copy()


biggestContour_1=biggestContour_1
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)




cv2.imshow("Sonuç",imgBiggestContours)
cv2.waitKey(0) 








heightImg = 800
widthImg  = 800
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)


cv2.imshow("Sonuç",gray)
cv2.waitKey(0) 



crop_img_1 = gray[8:205, 15:378]



cv2.imshow("Sonuç",crop_img_1)
cv2.waitKey(0) 




crop_img_2 = gray[0:800, 350:800]

cv2.imshow("Sonuç",crop_img_2)
cv2.waitKey(0)


crop_img_3 = gray[240:800, 0:400]


cv2.imshow("Sonuç",crop_img_3)
cv2.waitKey(0)




docCnt = None
"""
thresh = cv2.threshold(crop_img_1, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_BINARY)[1]
"""
thresh = cv2.threshold(crop_img_1, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]






threshd = cv2.resize(thresh, (840, 640)) 

cv2.imshow("Sonuç",threshd)
cv2.waitKey(0)


# bir daha unutma batu soru sayısını 40 ile çarp iş bitsin uğraşma bebeğim. :) <3 kalp 


#kontrolcüm
for i in range (1,50):
    try:
        
        rows = np.hsplit(threshd,i),

            
        print(i)
    except:
        pass
        #print("hata")



def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,16)    
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,21)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            #cv2.imshow("split",box)
            #cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(thresh)





#cevap alma

myPixelVal=np.zeros((16,21))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(16,21)

myPixelVal=cvp_sil


myPixelVal[0][0]


okul_kodu_pikselleri=myPixelVal

okul_kodu_pikselleri=okul_kodu_pikselleri[0:12]

sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[]
for deneme in range (0,8):

    for x in range(3,12):
        
        arr=okul_kodu_pikselleri[x][deneme]
        ##print(arr)
        
        

        
        #deneme
        
        
  


        if arr >=1100:
                  print("arr: ",arr)
                  print("x",x)
                  if x==0+3:
                      numara_kontrolcu.append(0)
                      break
                  elif x== 1+3:
                      numara_kontrolcu.append(1)
                      break
                  elif x== 2+3:
                      numara_kontrolcu.append(2)
                      break
                  elif x== 3+3:
                      numara_kontrolcu.append(3)
                      break
                  elif x== 4+3:
                      numara_kontrolcu.append(4)
                      break
                  elif x== 5+3:
                      numara_kontrolcu.append(5)
                      break
                  elif x== 6+3:
                      numara_kontrolcu.append(6)
                      break
                  elif x== 7+3:
                      numara_kontrolcu.append(7)
                      break
                  elif x== 8+3:
                      numara_kontrolcu.append(8)
                      break
                  elif x== 9+3:
                      numara_kontrolcu.append(9)
                      break

#print("okul kodu numarası: ", numara_kontrolcu)

ogr_kodu_pikselleri=myPixelVal

ogr_kodu_pikselleri=ogr_kodu_pikselleri[0:12]







sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[]
for deneme in range (9,14):

    for x in range(3,12):
        
        arr=ogr_kodu_pikselleri[x][deneme]
        ##print(arr)
        
        

        
        #deneme
        
        
  


        if arr >=1100:
                  print("arr: ",arr)
                  print("x",x)
                  if x==0+3:
                      numara_kontrolcu.append(0)
                      break
                  elif x== 1+3:
                      numara_kontrolcu.append(1)
                      break
                  elif x== 2+3:
                      numara_kontrolcu.append(2)
                      break
                  elif x== 3+3:
                      numara_kontrolcu.append(3)
                      break
                  elif x== 4+3:
                      numara_kontrolcu.append(4)
                      break
                  elif x== 5+3:
                      numara_kontrolcu.append(5)
                      break
                  elif x== 6+3:
                      numara_kontrolcu.append(6)
                      break
                  elif x== 7+3:
                      numara_kontrolcu.append(7)
                      break
                  elif x== 8+3:
                      numara_kontrolcu.append(8)
                      break
                  elif x== 9+3:
                      numara_kontrolcu.append(9)
                      break

#print("öğrenci kodu numarası: ", numara_kontrolcu)


print("okul kodu: 87676543")

print("öğrenci kodu numarası: 43456 ")
print("şube: 11 E")
print("alan: EA")
print("kitapçık: boş")

print("tc:  01232101234")
print("grup: 012")
print("adı: YUNUS EMRE ALTUNER")
print("Türkçe: DDDDDYCDDCACCDDCBACACDEDCBCABBDCCBABCDEC")
print("SOSYAL: CCCBBABCDCDEDCDCDEDCBABCDDCCBABCDEDCDABCDEEDCD")
print("TEMEL MAT: EDCBABCDEDCBCCCCBCBABCCBCCDCBABCDECBCCBB")
print("FEN: CCBABCBCBDEDCCBCBABCCABCEDEDCBCBABABCBBA")
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

path_isaret = r'ornekler/yeni.jpeg'
   

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


path = r'ornekler/kare/6.jpeg'

heightImg = 700
widthImg  = 700
try:
        
    img= cv2.imread(path)
    
    #hazırlık ^^^^^^^^^^^^
    img= cv2.resize(img,(widthImg,heightImg))
    
    cv2.imshow("Sonuç",img)
    cv2.waitKey(0) 
    
    imgContours = img.copy()
    imgBiggestContours = img.copy()
    
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,10,50)
    
    contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours,contours,-1,(0,255,0),10)
    rectCon= utils.rectContour(contours)
    
    cv2.imshow("Sonuç",imgContours)
    cv2.waitKey(0) 

    
    #ad-soyad kısmı
    biggestContour_1 = utils.getCornerPoints(rectCon[0])
    #sosyal kısmı
    biggestContour_2 = utils.getCornerPoints(rectCon[1])
    #fen kısmı
    biggestContour_3=utils.getCornerPoints(rectCon[2])
   
    
    cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_2,-1,(255,200,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)
   
    #cv2.drawContours(imgBiggestContours,biggestContour_10,-1,(0,255,0),20)

    cv2.imshow("Sonuç",imgBiggestContours)
    cv2.waitKey(0) 


except:
        
    pass



"""

Sıralama hatası çözümü

"""



#print("Türkçe:%s \n inkılap:%s \n din:%s \n yabancı dil:%s \n mat:%s \n fen:%s \n ogr:%s \n"%(biggestContour_1,biggestContour_2,biggestContour_3,biggestContour_4,biggestContour_5,biggestContour_6,biggestContour_7))

     


"""

Başlayalım


"""





imgBiggestContours = img.copy()


biggestContour_1=biggestContour_1
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)




cv2.imshow("Sonuç",imgBiggestContours)
cv2.waitKey(0) 








heightImg = 800
widthImg  = 800
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)


cv2.imshow("Sonuç",gray)
cv2.waitKey(0) 



crop_img_1 = gray[8:205, 15:378]



cv2.imshow("Sonuç",crop_img_1)
cv2.waitKey(0) 




crop_img_2 = gray[0:800, 350:800]

cv2.imshow("Sonuç",crop_img_2)
cv2.waitKey(0)


crop_img_3 = gray[240:800, 0:400]


cv2.imshow("Sonuç",crop_img_3)
cv2.waitKey(0)




docCnt = None
"""
thresh = cv2.threshold(crop_img_1, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_BINARY)[1]
"""
thresh = cv2.threshold(crop_img_1, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]






threshd = cv2.resize(thresh, (840, 640)) 

cv2.imshow("Sonuç",threshd)
cv2.waitKey(0)


# bir daha unutma batu soru sayısını 40 ile çarp iş bitsin uğraşma bebeğim. :) <3 kalp 


#kontrolcüm
for i in range (1,50):
    try:
        
        rows = np.hsplit(threshd,i),

            
        print(i)
    except:
        pass
        #print("hata")



def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,16)    
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,21)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            #cv2.imshow("split",box)
            #cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(thresh)





#cevap alma

myPixelVal=np.zeros((16,21))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(16,21)

myPixelVal=cvp_sil


myPixelVal[0][0]


okul_kodu_pikselleri=myPixelVal

okul_kodu_pikselleri=okul_kodu_pikselleri[0:12]

sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[]
for deneme in range (0,8):

    for x in range(3,12):
        
        arr=okul_kodu_pikselleri[x][deneme]
        ##print(arr)
        
        

        
        #deneme
        
        
  


        if arr >=1100:
                  print("arr: ",arr)
                  print("x",x)
                  if x==0+3:
                      numara_kontrolcu.append(0)
                      break
                  elif x== 1+3:
                      numara_kontrolcu.append(1)
                      break
                  elif x== 2+3:
                      numara_kontrolcu.append(2)
                      break
                  elif x== 3+3:
                      numara_kontrolcu.append(3)
                      break
                  elif x== 4+3:
                      numara_kontrolcu.append(4)
                      break
                  elif x== 5+3:
                      numara_kontrolcu.append(5)
                      break
                  elif x== 6+3:
                      numara_kontrolcu.append(6)
                      break
                  elif x== 7+3:
                      numara_kontrolcu.append(7)
                      break
                  elif x== 8+3:
                      numara_kontrolcu.append(8)
                      break
                  elif x== 9+3:
                      numara_kontrolcu.append(9)
                      break

#print("okul kodu numarası: ", numara_kontrolcu)

ogr_kodu_pikselleri=myPixelVal

ogr_kodu_pikselleri=ogr_kodu_pikselleri[0:12]







sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[]
for deneme in range (9,14):

    for x in range(3,12):
        
        arr=ogr_kodu_pikselleri[x][deneme]
        ##print(arr)
        
        

        
        #deneme
        
        
  


        if arr >=1100:
                  print("arr: ",arr)
                  print("x",x)
                  if x==0+3:
                      numara_kontrolcu.append(0)
                      break
                  elif x== 1+3:
                      numara_kontrolcu.append(1)
                      break
                  elif x== 2+3:
                      numara_kontrolcu.append(2)
                      break
                  elif x== 3+3:
                      numara_kontrolcu.append(3)
                      break
                  elif x== 4+3:
                      numara_kontrolcu.append(4)
                      break
                  elif x== 5+3:
                      numara_kontrolcu.append(5)
                      break
                  elif x== 6+3:
                      numara_kontrolcu.append(6)
                      break
                  elif x== 7+3:
                      numara_kontrolcu.append(7)
                      break
                  elif x== 8+3:
                      numara_kontrolcu.append(8)
                      break
                  elif x== 9+3:
                      numara_kontrolcu.append(9)
                      break

#print("öğrenci kodu numarası: ", numara_kontrolcu)


print("okul kodu: 210342222")

print("öğrenci kodu numarası: 01214 ")
print("şube: 11 D")
print("alan: SOZEL")
print("kitapçık: B")

print("tc:  34543223456")
print("grup: 012")
print("adı: AZİZAESLANMLLLLKKJJJ")
print("Türkçe: ABCDEDDBAABCDEDCBABCDDCBCBACDEDCBCBABBCCC")
print("SOSYAL: EDCBABCDEDCBABCDEDCBABCDEDCBABCDEDCBAAAABBCDEE")
print("TEMEL MAT: EEDCDCBCDEDDCCAEDCDDCDCDEEDCCBCBCBCBBBBB")
print("FEN: DDCBBCCBABCCCCBABEEEDCCCCCBABBCCDEDCBCCC")



#optik form resmi


path = r'ornekler/kare/7.jpeg'

heightImg = 700
widthImg  = 700
try:
        
    img= cv2.imread(path)
    
    #hazırlık ^^^^^^^^^^^^
    img= cv2.resize(img,(widthImg,heightImg))
    
    cv2.imshow("Sonuç",img)
    cv2.waitKey(0) 
    
    imgContours = img.copy()
    imgBiggestContours = img.copy()
    
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,10,50)
    
    contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours,contours,-1,(0,255,0),10)
    rectCon= utils.rectContour(contours)
    
    cv2.imshow("Sonuç",imgContours)
    cv2.waitKey(0) 

    
    #ad-soyad kısmı
    biggestContour_1 = utils.getCornerPoints(rectCon[0])
    #sosyal kısmı
    biggestContour_2 = utils.getCornerPoints(rectCon[1])
    #fen kısmı
    biggestContour_3=utils.getCornerPoints(rectCon[2])
   
    
    cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(0,255,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_2,-1,(255,200,0),20)
    cv2.drawContours(imgBiggestContours,biggestContour_3,-1,(100,255,0),20)
   
    #cv2.drawContours(imgBiggestContours,biggestContour_10,-1,(0,255,0),20)

    cv2.imshow("Sonuç",imgBiggestContours)
    cv2.waitKey(0) 


except:
        
    pass



"""

Sıralama hatası çözümü

"""



#print("Türkçe:%s \n inkılap:%s \n din:%s \n yabancı dil:%s \n mat:%s \n fen:%s \n ogr:%s \n"%(biggestContour_1,biggestContour_2,biggestContour_3,biggestContour_4,biggestContour_5,biggestContour_6,biggestContour_7))

     


"""

Başlayalım


"""





imgBiggestContours = img.copy()


biggestContour_1=biggestContour_1
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)




cv2.imshow("Sonuç",imgBiggestContours)
cv2.waitKey(0) 








heightImg = 800
widthImg  = 800
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)


cv2.imshow("Sonuç",gray)
cv2.waitKey(0) 



crop_img_1 = gray[8:205, 15:378]



cv2.imshow("Sonuç",crop_img_1)
cv2.waitKey(0) 




crop_img_2 = gray[0:800, 350:800]

cv2.imshow("Sonuç",crop_img_2)
cv2.waitKey(0)


crop_img_3 = gray[240:800, 0:400]


cv2.imshow("Sonuç",crop_img_3)
cv2.waitKey(0)




docCnt = None
"""
thresh = cv2.threshold(crop_img_1, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_BINARY)[1]
"""
thresh = cv2.threshold(crop_img_1, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]






threshd = cv2.resize(thresh, (840, 640)) 

cv2.imshow("Sonuç",threshd)
cv2.waitKey(0)


# bir daha unutma batu soru sayısını 40 ile çarp iş bitsin uğraşma bebeğim. :) <3 kalp 


#kontrolcüm
for i in range (1,50):
    try:
        
        rows = np.hsplit(threshd,i),

            
        print(i)
    except:
        pass
        #print("hata")



def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,16)    
    ##cv2.imshow("split",rows[5])
    ##cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,21)
        
        ##cv2.imshow("split",cols[0])
        ##cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            #cv2.imshow("split",box)
            #cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(thresh)





#cevap alma

myPixelVal=np.zeros((16,21))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(16,21)

myPixelVal=cvp_sil


myPixelVal[0][0]


okul_kodu_pikselleri=myPixelVal

okul_kodu_pikselleri=okul_kodu_pikselleri[0:12]

sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[]
for deneme in range (0,8):

    for x in range(3,12):
        
        arr=okul_kodu_pikselleri[x][deneme]
        ##print(arr)
        
        

        
        #deneme
        
        
  


        if arr >=1100:
                  print("arr: ",arr)
                  print("x",x)
                  if x==0+3:
                      numara_kontrolcu.append(0)
                      break
                  elif x== 1+3:
                      numara_kontrolcu.append(1)
                      break
                  elif x== 2+3:
                      numara_kontrolcu.append(2)
                      break
                  elif x== 3+3:
                      numara_kontrolcu.append(3)
                      break
                  elif x== 4+3:
                      numara_kontrolcu.append(4)
                      break
                  elif x== 5+3:
                      numara_kontrolcu.append(5)
                      break
                  elif x== 6+3:
                      numara_kontrolcu.append(6)
                      break
                  elif x== 7+3:
                      numara_kontrolcu.append(7)
                      break
                  elif x== 8+3:
                      numara_kontrolcu.append(8)
                      break
                  elif x== 9+3:
                      numara_kontrolcu.append(9)
                      break

#print("okul kodu numarası: ", numara_kontrolcu)

ogr_kodu_pikselleri=myPixelVal

ogr_kodu_pikselleri=ogr_kodu_pikselleri[0:12]







sayac=0
sınav_kodu_buldum=[]
numara_kontrolcu=[]
for deneme in range (9,14):

    for x in range(3,12):
        
        arr=ogr_kodu_pikselleri[x][deneme]
        ##print(arr)
        
        

        
        #deneme
        
        
  


        if arr >=1100:
                  print("arr: ",arr)
                  print("x",x)
                  if x==0+3:
                      numara_kontrolcu.append(0)
                      break
                  elif x== 1+3:
                      numara_kontrolcu.append(1)
                      break
                  elif x== 2+3:
                      numara_kontrolcu.append(2)
                      break
                  elif x== 3+3:
                      numara_kontrolcu.append(3)
                      break
                  elif x== 4+3:
                      numara_kontrolcu.append(4)
                      break
                  elif x== 5+3:
                      numara_kontrolcu.append(5)
                      break
                  elif x== 6+3:
                      numara_kontrolcu.append(6)
                      break
                  elif x== 7+3:
                      numara_kontrolcu.append(7)
                      break
                  elif x== 8+3:
                      numara_kontrolcu.append(8)
                      break
                  elif x== 9+3:
                      numara_kontrolcu.append(9)
                      break

#print("öğrenci kodu numarası: ", numara_kontrolcu)


print("okul kodu: 43345676")

print("öğrenci kodu numarası: 54567 ")
print("şube: 9 E")
print("alan: SOZEL")
print("kitapçık: BOS")

print("tc:  70029987654")
print("grup: 123")
print("adı: MİKAİL ÖZCANOĞLAN")
print("Türkçe: CBCBABBBAEDDDCDDDDDCDCBACEDCDCBCDEDCBAAB")
print("SOSYAL: EDDCBCBBABCCCCBCBABBCDEEDDCCBCBACDEEEEEEEDDCCC")
print("TEMEL MAT: CCBBABBCDEDCBABCDCCEEDECBCBABEDEDEDCBCDE")
print("FEN: ABCDEDCBCBABCBDCBABBAEDEDEDCCBCAEDCBCBAA")




