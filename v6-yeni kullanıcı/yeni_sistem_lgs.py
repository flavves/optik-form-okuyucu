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

path_isaret = r'ornekler/orijinal_optik_form.jpg'
   

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


path = "ornekler/yeni/kesilmisler/Screenshot_15.jpg"

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



except:
        
    pass



"""

Sıralama hatası çözümü

"""



#print("Türkçe:%s \n inkılap:%s \n din:%s \n yabancı dil:%s \n mat:%s \n fen:%s \n ogr:%s \n"%(biggestContour_1,biggestContour_2,biggestContour_3,biggestContour_4,biggestContour_5,biggestContour_6,biggestContour_7))

     


"""

Türkçe


"""



imgBiggestContours = img.copy()


biggestContour_1=biggestContour_1
cv2.drawContours(imgBiggestContours,biggestContour_1,-1,(255,0,59),20)




biggestContour=utils.reorder(biggestContour_1)












heightImg = 800
widthImg  = 800
#imgBiggestContours = cv2.resize(imgBiggestContours, (heightImg, widthImg)) 




pt1= np.float32(biggestContour)
pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgWarpColored= cv2.warpPerspective(img,matrix,(widthImg,heightImg))



gray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
crop_img_1 = gray[0:800, 50:260]

crop_img_2 = gray[0:800, 315:530]

crop_img_3 = gray[0:520, 580:800]



    


docCnt = None
"""
thresh = cv2.threshold(crop_img_1, 127, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_BINARY)[1]
"""
thresh = cv2.threshold(crop_img_1, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]






threshd = cv2.resize(thresh, (900, 600)) 


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





turkce_cvp_anahtari = """{  }"""
turkce_cvp_anahtari_gercek = json.loads(turkce_cvp_anahtari)


y=68
cevap_kontrolcu=[]
for x in range (0,15):
    y=y+26
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 2300:
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
                    try:
                        xr=x_ler[0]    
                        center_coordinates = (xr, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 1:
                    gercek_cvp="b"
                    try:
                        xr=x_ler[1]    
                        center_coordinates = (xr, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 2:
                    gercek_cvp="c"
                    try:
                        xr=x_ler[2]    
                        center_coordinates = (xr, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 3:
                    gercek_cvp="d"
                    try:
                        xr=x_ler[3]    
                        center_coordinates = (xr, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 4:
                    gercek_cvp="e"
                    try:
                        xr=x_ler[4]    
                        center_coordinates = (xr, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                
                print("Türkçe %s sorunun cevabı:%s"%((x+1),gercek_cvp))
                turkce_cvp_anahtari_gercek[x+1] = gercek_cvp


 


    
# 2



crop_img_2 = gray[0:800, 315:530]





docCnt = None

thresh = cv2.threshold(crop_img_2, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]






threshd = cv2.resize(thresh, (900, 600)) 



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





turkce_cvp_anahtari = """{  }"""
turkce_cvp_anahtari_gercek = json.loads(turkce_cvp_anahtari)


y=68
cevap_kontrolcu=[]
for x in range (0,15):
    y=y+26
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 2300:
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
                    try:
                        x1=x1_ler[0]    
                        center_coordinates = (x1, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 1:
                    gercek_cvp="b"
                    try:
                        x1=x1_ler[1]    
                        center_coordinates = (x1, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 2:
                    gercek_cvp="c"
                    try:
                        x1=x1_ler[2]    
                        center_coordinates = (x1, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 3:
                    gercek_cvp="d"
                    try:
                        x1=x1_ler[3]    
                        center_coordinates = (x1, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 4:
                    gercek_cvp="e"
                    try:
                        x1=x1_ler[4]    
                        center_coordinates = (x1, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                
                print("Türkçe %s sorunun cevabı:%s"%((x+16),gercek_cvp))
                turkce_cvp_anahtari_gercek[x+1] = gercek_cvp
    
# 3


crop_img_3 = gray[0:520, 580:800]



docCnt = None

thresh = cv2.threshold(crop_img_3, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]









threshd = cv2.resize(thresh, (450, 400)) 


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



#print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[6]))






#cevap alma

myPixelVal=np.zeros((10,5))


countC=0
countR=0
cvp_sil=[]
for image in boxes:
    totalPixels = cv2.countNonZero(image)
    cvp_sil.append(totalPixels)

cvp_sil=np.array(cvp_sil)
cvp_sil=cvp_sil.reshape(10,5)
#cvp_sil[27]
myPixelVal=cvp_sil

#TEST
#İLK 1,2,3,4 VB 2. A,B,C,D

#myPixelVal[26][2]





turkce_cvp_anahtari = """{  }"""
turkce_cvp_anahtari_gercek = json.loads(turkce_cvp_anahtari)

y=68

cevap_kontrolcu=[]
for x in range (0,10):
    arr=myPixelVal[x]
    #print("arr",arr)
    arr_kont=np.amax(arr)
    kontrol_veri=arr_kont
    cevap_kontrolcu = arr.tolist()
    if kontrol_veri >= 2300:
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
                    try:
                        x2=x2_ler[0]    
                        center_coordinates = (x2, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 1:
                    gercek_cvp="b"
                    try:
                        x2=x2_ler[1]    
                        center_coordinates = (x2, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 2:
                    gercek_cvp="c"
                    try:
                        x2=x2_ler[2]    
                        center_coordinates = (x2, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 3:
                    gercek_cvp="d"
                    try:
                        x2=x2_ler[3]    
                        center_coordinates = (x2, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                elif yeri == 4:
                    gercek_cvp="e"
                    try:
                        x2=x2_ler[4]    
                        center_coordinates = (x2, y)
                        
                        radius = 8
                      
                    
                        color = (0, 255, 0)
                          
                        
                        thickness = 3
                          
                        
                        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
                        

                       
                    except:
                        pass
                
                print("Türkçe %s sorunun cevabı:%s"%((x+31),gercek_cvp))
                turkce_cvp_anahtari_gercek[x+1] = gercek_cvp

dsize = (1080, 1500)

image_isaret_gosterme = cv2.resize(image_isaret,dsize)
imgBiggestContours_gosterme = cv2.resize(imgBiggestContours,dsize)


imageArray = ([image_isaret_gosterme,imgBiggestContours_gosterme])

# LABELS FOR DISPLAY
lables = [["işaret","orijinal"]]

stackedImage = utils.stackImages(imageArray,0.5,lables)

#sorun olursa bu kısımda olur buraya dikkat edersiniz silerseniz aşağıdaki iki satırı düzlir
!!!!
!!!!
!!!!
!!!!
cv2.imshow("Sonuç",stackedImage)
cv2.waitKey(0) 
