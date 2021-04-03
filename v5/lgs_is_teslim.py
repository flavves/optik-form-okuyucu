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





path = "ornekler/sorun2.jpeg"

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
    #biggestContour_10=utils.getCornerPoints(rectCon[9])
    ##print("Türkçe:%s \n sosyal:%s \n matematik:%s \n fen:%s \n"%(biggestContour_5,biggestContour_2,biggestContour_4,biggestContour_3))
    ##print(len(biggestContour))
    ##print(biggestContour)
    ##print(gradePoints)
    
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
    #biggestContour_10=utils.getCornerPoints(rectCon[9])
    
    ##print(len(biggestContour))
    ##print(biggestContour)
    ##print(gradePoints)
    
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



#print("Türkçe:%s \n inkılap:%s \n din:%s \n yabancı dil:%s \n mat:%s \n fen:%s \n ogr:%s \n"%(biggestContour_1,biggestContour_2,biggestContour_3,biggestContour_4,biggestContour_5,biggestContour_6,biggestContour_7))

     
siralama=[]
sag_siralama=[]

if biggestContour_1[0][0][1] < 300:   
    siralama.append(biggestContour_1[0][0][0])
if biggestContour_2[0][0][1] < 300:
    siralama.append(biggestContour_2[0][0][0])
if biggestContour_3[0][0][1] < 300:
    siralama.append(biggestContour_3[0][0][0])
if biggestContour_4[0][0][1] < 300:
    siralama.append(biggestContour_4[0][0][0])
if biggestContour_5[0][0][1] < 300:
    siralama.append(biggestContour_5[0][0][0])
if biggestContour_6[0][0][1] < 300:
    siralama.append(biggestContour_6[0][0][0])
if biggestContour_7[0][0][1] < 300:
    siralama.append(biggestContour_7[0][0][0])
if biggestContour_8[0][0][1] < 300:
    siralama.append(biggestContour_8[0][0][0])
if biggestContour_9[0][0][1] < 300:
    siralama.append(biggestContour_9[0][0][0])

if biggestContour_1[0][0][1] > 300:   
    sag_siralama.append(biggestContour_1[0][0][0])
if biggestContour_2[0][0][1] > 300:
    sag_siralama.append(biggestContour_2[0][0][0])
if biggestContour_3[0][0][1] > 300:
    sag_siralama.append(biggestContour_3[0][0][0])
if biggestContour_4[0][0][1] > 300:
    sag_siralama.append(biggestContour_4[0][0][0])
if biggestContour_5[0][0][1] > 300:
    sag_siralama.append(biggestContour_5[0][0][0])
if biggestContour_6[0][0][1] > 300:
    sag_siralama.append(biggestContour_6[0][0][0])
if biggestContour_7[0][0][1] > 300:
    sag_siralama.append(biggestContour_7[0][0][0])
if biggestContour_8[0][0][1] > 300:
    sag_siralama.append(biggestContour_8[0][0][0])
if biggestContour_9[0][0][1] > 300:
    sag_siralama.append(biggestContour_9[0][0][0])



siralama.sort()
sag_siralama.sort()



### 0000000 ######
if sag_siralama[0]==biggestContour_1[0][0][0]:
    ogr_no=biggestContour_1
    
elif sag_siralama[0]==biggestContour_2[0][0][0]:
    ogr_no=biggestContour_2
    
elif sag_siralama[0]==biggestContour_3[0][0][0]:
    ogr_no=biggestContour_3
    
elif sag_siralama[0]==biggestContour_4[0][0][0]:
    ogr_no=biggestContour_4

elif sag_siralama[0]==biggestContour_5[0][0][0]:
    ogr_no=biggestContour_5
    
elif sag_siralama[0] == biggestContour_6[0][0][0]:
        ogr_no=biggestContour_6
        
elif sag_siralama[0] == biggestContour_7[0][0][0]:
        ogr_no=biggestContour_7
        
elif sag_siralama[0]==biggestContour_8[0][0][0]:
    ogr_no=biggestContour_8

elif sag_siralama[0]==biggestContour_9[0][0][0]:
    ogr_no=biggestContour_9

###### 111111 #######

if sag_siralama[1]==biggestContour_1[0][0][0]:
    kurum_kodu=biggestContour_1
    
elif sag_siralama[1]==biggestContour_2[0][0][0]:
    kurum_kodu=biggestContour_2
    
elif sag_siralama[1]==biggestContour_3[0][0][0]:
    kurum_kodu=biggestContour_3
    
elif sag_siralama[1]==biggestContour_4[0][0][0]:
    kurum_kodu=biggestContour_4

elif sag_siralama[1]==biggestContour_5[0][0][0]:
    kurum_kodu=biggestContour_5
    
elif sag_siralama[1] == biggestContour_6[0][0][0]:
        kurum_kodu=biggestContour_6
        
elif sag_siralama[1] == biggestContour_7[0][0][0]:
        kurum_kodu=biggestContour_7
        
elif sag_siralama[1]==biggestContour_8[0][0][0]:
    kurum_kodu=biggestContour_8

elif sag_siralama[1]==biggestContour_9[0][0][0]:
    kurum_kodu=biggestContour_9
    
##### 2222222 ########

if sag_siralama[2]==biggestContour_1[0][0][0]:
    sinav_turu=biggestContour_1
    
elif sag_siralama[2]==biggestContour_2[0][0][0]:
    sinav_turu=biggestContour_2
    
elif sag_siralama[2]==biggestContour_3[0][0][0]:
    sinav_turu=biggestContour_3
    
elif sag_siralama[2]==biggestContour_4[0][0][0]:
    sinav_turu=biggestContour_4

elif sag_siralama[2]==biggestContour_5[0][0][0]:
    sinav_turu=biggestContour_5
    
elif sag_siralama[2] == biggestContour_6[0][0][0]:
        sinav_turu=biggestContour_6
        
elif sag_siralama[2] == biggestContour_7[0][0][0]:
        sinav_turu=biggestContour_7
        
elif sag_siralama[2]==biggestContour_8[0][0][0]:
    sinav_turu=biggestContour_8

elif sag_siralama[2]==biggestContour_9[0][0][0]:
    sinav_turu=biggestContour_9



#### üst kısım #######


"""

#### üst kısım #######

"""
# türkçe

if siralama[0]==biggestContour_1[0][0][0]:
    turkce_kisimi=biggestContour_1
    
elif siralama[0]==biggestContour_2[0][0][0]:
    turkce_kisimi=biggestContour_2
    
elif siralama[0]==biggestContour_3[0][0][0]:
    turkce_kisimi=biggestContour_3
    
elif siralama[0]==biggestContour_4[0][0][0]:
    turkce_kisimi=biggestContour_4

elif siralama[0]==biggestContour_5[0][0][0]:
    turkce_kisimi=biggestContour_5
    
elif siralama[0] == biggestContour_6[0][0][0]:
        turkce_kisimi=biggestContour_6
        
elif siralama[0] == biggestContour_7[0][0][0]:
        turkce_kisimi=biggestContour_7
        
elif siralama[0]==biggestContour_8[0][0][0]:
    turkce_kisimi=biggestContour_8

elif siralama[0]==biggestContour_9[0][0][0]:
    turkce_kisimi=biggestContour_9


# ink tarihi

if siralama[1]==biggestContour_1[0][0][0]:
    inkilap_kisimi=biggestContour_1
    
elif siralama[1]==biggestContour_2[0][0][0]:
    inkilap_kisimi=biggestContour_2
    
elif siralama[1]==biggestContour_3[0][0][0]:
    inkilap_kisimi=biggestContour_3
    
elif siralama[1]==biggestContour_4[0][0][0]:
    inkilap_kisimi=biggestContour_4

elif siralama[1]==biggestContour_5[0][0][0]:
    inkilap_kisimi=biggestContour_5
    
elif siralama[1] == biggestContour_6[0][0][0]:
        inkilap_kisimi=biggestContour_6
        
elif siralama[1] == biggestContour_7[0][0][0]:
        inkilap_kisimi=biggestContour_7
        
elif siralama[1]==biggestContour_8[0][0][0]:
    inkilap_kisimi=biggestContour_8

elif siralama[1]==biggestContour_9[0][0][0]:
    inkilap_kisimi=biggestContour_9


# din

if siralama[2]==biggestContour_1[0][0][0]:
    din_kisimi=biggestContour_1
    
elif siralama[2]==biggestContour_2[0][0][0]:
    din_kisimi=biggestContour_2
    
elif siralama[2]==biggestContour_3[0][0][0]:
    din_kisimi=biggestContour_3
    
elif siralama[2]==biggestContour_4[0][0][0]:
    din_kisimi=biggestContour_4

elif siralama[2]==biggestContour_5[0][0][0]:
    din_kisimi=biggestContour_5
    
elif siralama[2] == biggestContour_6[0][0][0]:
        din_kisimi=biggestContour_6
        
elif siralama[2] == biggestContour_7[0][0][0]:
        din_kisimi=biggestContour_7
        
elif siralama[2]==biggestContour_8[0][0][0]:
    din_kisimi=biggestContour_8

elif siralama[2]==biggestContour_9[0][0][0]:
    din_kisimi=biggestContour_9



# yabanci

if siralama[3]==biggestContour_1[0][0][0]:
    yabanci_kisimi=biggestContour_1
    
elif siralama[3]==biggestContour_2[0][0][0]:
    yabanci_kisimi=biggestContour_2
    
elif siralama[3]==biggestContour_3[0][0][0]:
    yabanci_kisimi=biggestContour_3
    
elif siralama[3]==biggestContour_4[0][0][0]:
    yabanci_kisimi=biggestContour_4

elif siralama[3]==biggestContour_5[0][0][0]:
    yabanci_kisimi=biggestContour_5
    
elif siralama[3] == biggestContour_6[0][0][0]:
        yabanci_kisimi=biggestContour_6
        
elif siralama[3] == biggestContour_7[0][0][0]:
        yabanci_kisimi=biggestContour_7
        
elif siralama[3]==biggestContour_8[0][0][0]:
    yabanci_kisimi=biggestContour_8

elif siralama[3]==biggestContour_9[0][0][0]:
    yabanci_kisimi=biggestContour_9



# mat

if siralama[4]==biggestContour_1[0][0][0]:
    mat_kisimi=biggestContour_1
    
elif siralama[4]==biggestContour_2[0][0][0]:
    mat_kisimi=biggestContour_2
    
elif siralama[4]==biggestContour_3[0][0][0]:
    mat_kisimi=biggestContour_3
    
elif siralama[4]==biggestContour_4[0][0][0]:
    mat_kisimi=biggestContour_4

elif siralama[4]==biggestContour_5[0][0][0]:
    mat_kisimi=biggestContour_5
    
elif siralama[4] == biggestContour_6[0][0][0]:
        mat_kisimi=biggestContour_6
        
elif siralama[4] == biggestContour_7[0][0][0]:
        mat_kisimi=biggestContour_7
        
elif siralama[4]==biggestContour_8[0][0][0]:
    mat_kisimi=biggestContour_8

elif siralama[4]==biggestContour_9[0][0][0]:
    mat_kisimi=biggestContour_9



# fen

if siralama[5]==biggestContour_1[0][0][0]:
    fen_kisimi=biggestContour_1
    
elif siralama[5]==biggestContour_2[0][0][0]:
    fen_kisimi=biggestContour_2
    
elif siralama[5]==biggestContour_3[0][0][0]:
    fen_kisimi=biggestContour_3
    
elif siralama[5]==biggestContour_4[0][0][0]:
    fen_kisimi=biggestContour_4

elif siralama[5]==biggestContour_5[0][0][0]:
    fen_kisimi=biggestContour_5
    
elif siralama[5] == biggestContour_6[0][0][0]:
        fen_kisimi=biggestContour_6
        
elif siralama[5] == biggestContour_7[0][0][0]:
        fen_kisimi=biggestContour_7
        
elif siralama[5]==biggestContour_8[0][0][0]:
    fen_kisimi=biggestContour_8

elif siralama[5]==biggestContour_9[0][0][0]:
    fen_kisimi=biggestContour_9



#### optik okumalara geçelim #####





"""

Türkçe


"""



imgBiggestContours = img.copy()


biggestContour_1=turkce_kisimi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 










heightImg = 800
widthImg  = 200
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[17:775, 49:180]
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





threshd = cv2.resize(thresh, (720, 800)) 

#cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


"""
#kontrolcüm
for i in range (1,50):
    try:
        
        rows = np.vsplit(threshd,i)
        #print(i)
    except:
        #print("hata")

"""


def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,20)    
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,4)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
#cv2.imshow("test",boxes[0])
#cv2.waitKey(0) 



##print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))






#cevap alma

myPixelVal=np.zeros((20,4))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(20,4)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]





turkce_cvp_anahtari = """{  }"""
turkce_cvp_anahtari_gercek = json.loads(turkce_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,20):
    arr=myPixelVal[x]
    ##print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 4000:
        ##print("adanam")
        for i in range (0,4):
            kontrol=cevap_kontrolcu[i]
            ##print(kontrol)
            i+=1
            if kontrol==kontrol_veri:
                ##print("dogru")
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
                
                #print("Türkçe %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                turkce_cvp_anahtari_gercek[x+1] = gercek_cvp
    




"""

ink. tarihi


"""



imgBiggestContours = img.copy()


biggestContour_1=inkilap_kisimi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 










heightImg = 800
widthImg  = 200
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[17:775, 49:180]
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





threshd = cv2.resize(thresh, (720, 800)) 

#cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


"""
#kontrolcüm
for i in range (1,50):
    try:
        
        rows = np.vsplit(threshd,i)
        #print(i)
    except:
        #print("hata")

"""


def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,20)    
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,4)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
#cv2.imshow("test",boxes[0])
#cv2.waitKey(0) 



##print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))






#cevap alma

myPixelVal=np.zeros((20,4))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(20,4)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]





ink_cvp_anahtari = """{  }"""
ink_cvp_anahtari_gercek = json.loads(ink_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,20):
    arr=myPixelVal[x]
    ##print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 4000:
        ##print("adanam")
        for i in range (0,4):
            kontrol=cevap_kontrolcu[i]
            ##print(kontrol)
            i+=1
            if kontrol==kontrol_veri:
                ##print("dogru")
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
                
                #print("inkilap %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                ink_cvp_anahtari_gercek[x+1] = gercek_cvp
    





"""

din kültürü

"""



imgBiggestContours = img.copy()


biggestContour_1=din_kisimi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 










heightImg = 800
widthImg  = 200
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[17:775, 49:180]
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





threshd = cv2.resize(thresh, (720, 800)) 

#cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


"""
#kontrolcüm
for i in range (1,50):
    try:
        
        rows = np.vsplit(threshd,i)
        #print(i)
    except:
        #print("hata")

"""


def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,20)    
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,4)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
#cv2.imshow("test",boxes[0])
#cv2.waitKey(0) 



##print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))






#cevap alma

myPixelVal=np.zeros((20,4))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(20,4)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]





din_cvp_anahtari = """{  }"""
din_cvp_anahtari_gercek = json.loads(din_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,20):
    arr=myPixelVal[x]
    ##print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 4000:
        ##print("adanam")
        for i in range (0,4):
            kontrol=cevap_kontrolcu[i]
            ##print(kontrol)
            i+=1
            if kontrol==kontrol_veri:
                ##print("dogru")
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
                
                #print("din %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                din_cvp_anahtari_gercek[x+1] = gercek_cvp
    




"""

Yabancı dil

"""



imgBiggestContours = img.copy()


biggestContour_1=yabanci_kisimi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 










heightImg = 800
widthImg  = 200
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[17:775, 49:180]
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





threshd = cv2.resize(thresh, (720, 800)) 

#cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


"""
#kontrolcüm
for i in range (1,50):
    try:
        
        rows = np.vsplit(threshd,i)
        #print(i)
    except:
        #print("hata")

"""


def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,20)    
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,4)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
#cv2.imshow("test",boxes[0])
#cv2.waitKey(0) 



##print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))






#cevap alma

myPixelVal=np.zeros((20,4))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(20,4)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]





yabanci_cvp_anahtari = """{  }"""
yabanci_cvp_anahtari_gercek = json.loads(yabanci_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,20):
    arr=myPixelVal[x]
    ##print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 4000:
        ##print("adanam")
        for i in range (0,4):
            kontrol=cevap_kontrolcu[i]
            ##print(kontrol)
            i+=1
            if kontrol==kontrol_veri:
                ##print("dogru")
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
                
                #print("yabanci %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                yabanci_cvp_anahtari_gercek[x+1] = gercek_cvp
    



"""

Mat

"""



imgBiggestContours = img.copy()


biggestContour_1=mat_kisimi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 










heightImg = 800
widthImg  = 200
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[17:775, 49:180]
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





threshd = cv2.resize(thresh, (720, 800)) 

#cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


"""
#kontrolcüm
for i in range (1,50):
    try:
        
        rows = np.vsplit(threshd,i)
        #print(i)
    except:
        #print("hata")

"""


def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,20)    
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,4)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
#cv2.imshow("test",boxes[0])
#cv2.waitKey(0) 



##print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))






#cevap alma

myPixelVal=np.zeros((20,4))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(20,4)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]





mat_cvp_anahtari = """{  }"""
mat_cvp_anahtari_gercek = json.loads(mat_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,20):
    arr=myPixelVal[x]
    ##print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 4000:
        ##print("adanam")
        for i in range (0,4):
            kontrol=cevap_kontrolcu[i]
            ##print(kontrol)
            i+=1
            if kontrol==kontrol_veri:
                ##print("dogru")
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
                
                #print("matematik %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                mat_cvp_anahtari_gercek[x+1] = gercek_cvp
    


"""

FEN

"""



imgBiggestContours = img.copy()


biggestContour_1=fen_kisimi
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)


#cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 










heightImg = 800
widthImg  = 200
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[17:775, 49:180]
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





threshd = cv2.resize(thresh, (720, 800)) 

#cv2.imshow("gosterme", threshd)                            # Show image

###cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


"""
#kontrolcüm
for i in range (1,50):
    try:
        
        rows = np.vsplit(threshd,i)
        #print(i)
    except:
        #print("hata")

"""


def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,20)    
    ###cv2.imshow("split",rows[5])
    ###cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,4)
        
        ###cv2.imshow("split",cols[0])
        ###cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ###cv2.imshow("split",box)
            ###cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
#cv2.imshow("test",boxes[0])
#cv2.waitKey(0) 



##print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))






#cevap alma

myPixelVal=np.zeros((20,4))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(20,4)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]





fen_cvp_anahtari = """{  }"""
fen_cvp_anahtari_gercek = json.loads(fen_cvp_anahtari)



cevap_kontrolcu=[]
for x in range (0,20):
    arr=myPixelVal[x]
    ##print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 4000:
        ##print("adanam")
        for i in range (0,4):
            kontrol=cevap_kontrolcu[i]
            ##print(kontrol)
            i+=1
            if kontrol==kontrol_veri:
                ##print("dogru")
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
                
                #print("fen %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                fen_cvp_anahtari_gercek[x+1] = gercek_cvp
    



"""


ögr numarası


"""

imgBiggestContours = img.copy()

biggestContour_6=ogr_no
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

##cv2.imshow("cropped", imgWarpColored)
##cv2.waitKey(0)


gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[140:820, 65:370]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)







docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


##cv2.imshow("gosterme", thresh)                            # Show image

####cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 





threshd = cv2.resize(thresh, (700, 1000)) 

###cv2.imshow("gosterme", threshd)                            # Show image

####cv2.imshow("gosterme paper", imgBiggestContours)
###cv2.waitKey(0) 






def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,10)    
    ####cv2.imshow("split",rows[5])
    ####cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,7)
        
        ####cv2.imshow("split",cols[0])
        ####cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ####cv2.imshow("split",box)
            ####cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
####cv2.imshow("test",boxes[6])
####cv2.waitKey(0) 



##print(cv2.countNonZero(boxes[14]),cv2.countNonZero(boxes[9]))








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
        ##print(arr)
        
        

        
        #deneme
        
        
        ##print("arr: ",arr)
        ##print("x",x)


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
  
##print(kurum_kodu_no)  
ogr_no=ogr_no.replace(" ","")


#sonuç
#print("ogr_no: %s "%ogr_no)



"""


Kurum  Kodu


"""

imgBiggestContours = img.copy()

biggestContour_6=kurum_kodu
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

##cv2.imshow("cropped", imgWarpColored)
##cv2.waitKey(0)


gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[140:818, 65:365]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)







docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


##cv2.imshow("gosterme", thresh)                            # Show image

####cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 





threshd = cv2.resize(thresh, (700, 1000)) 

###cv2.imshow("gosterme", threshd)                            # Show image

####cv2.imshow("gosterme paper", imgBiggestContours)
###cv2.waitKey(0) 






def splitBoxes(img):
        
    
    #rows = np.hsplit(threshd,5)
    rows = np.vsplit(threshd,10)    
    ####cv2.imshow("split",rows[5])
    ####cv2.waitKey(0) 
 
    boxes =[]
    for r in rows:
        cols = np.hsplit(r,7)
        
        ####cv2.imshow("split",cols[0])
        ####cv2.waitKey(0) 
        for box in cols:
            boxes.append(box)
            ####cv2.imshow("split",box)
            ####cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(threshd)
####cv2.imshow("test",boxes[6])
####cv2.waitKey(0) 



##print(cv2.countNonZero(boxes[14]),cv2.countNonZero(boxes[9]))








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
        ##print(arr)
        
        

        
        #deneme
        
        
        ##print("arr: ",arr)
        ##print("x",x)


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
kurum_koddd = ' '.join(map(str, s)) 
  
##print(kurum_kodu_no)  
kurum_koddd=kurum_koddd.replace(" ","")


#sonuç
#print("ogr_no: %s "%kurum_koddd)





"""


Oturum sınav türü


"""

imgBiggestContours = img.copy()

biggestContour_6=sinav_turu
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

##cv2.imshow("cropped", imgWarpColored)
##cv2.waitKey(0)


gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img = gray[410:480, 175:220]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)







docCnt = None
#crop_img=four_point_transform(crop_img, docCnt.reshape(4, 2))
thresh = cv2.threshold(crop_img, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

#thresh = cv2.resize(thresh, (199, 1363)) 


##cv2.imshow("gosterme", thresh)                            # Show image

####cv2.imshow("gosterme paper", imgBiggestContours)
##cv2.waitKey(0) 





threshd = cv2.resize(thresh, (100, 100)) 

#cv2.imshow("gosterme", threshd)                            # Show image

####cv2.imshow("gosterme paper", imgBiggestContours)
#cv2.waitKey(0) 


#   !!!!!!!! >>>

totalPixels = cv2.countNonZero(threshd)

if totalPixels > 3500:
    sinav_tur_a="sayisal"
else:
    sinav_tur_a="sözel"





"""

Json çıkarma

"""


import json

x = {
  "kurum_kodu": kurum_koddd,
  "ogr_no": ogr_no,
  "turkce": turkce_cvp_anahtari_gercek,
  "inkilap": ink_cvp_anahtari_gercek,
  "din": din_cvp_anahtari_gercek,
  "yabancidil": yabanci_cvp_anahtari_gercek,
  "mat": mat_cvp_anahtari_gercek,
  "fen": fen_cvp_anahtari_gercek,
  "sinav_tur": sinav_tur_a,

}

sonuc_json=(json.dumps(x, ensure_ascii=False).encode('utf8'))
print("!!!!! json çıktı !!!!")
print(sonuc_json.decode())








