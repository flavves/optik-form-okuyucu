# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 00:49:27 2021

@author: yazılım
"""


"""

v3

ad soyad okuyor

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


# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()

#ap.add_argument("-i", "--image", required=True,
#	help="path to the input image")
#args = vars(ap.parse_args())
# define the answer key which maps the question number
# to the correct answer
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}


# load the image, convert it to grayscale, blur it
# slightly, then find edges
image = cv2.imread("bionluk.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

cv2.imshow("gosterme paper", gray)                            # Show image

cv2.imshow("gosterme blurred", blurred)                            # Show image

cv2.imshow("gosterme paper", edged)                            # Show image
cv2.waitKey(0) 


cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None
# ensure that at least one contour was found
if len(cnts) > 0:
	# sort the contours according to their size in
	# descending order
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
	# loop over the sorted contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		# if our approximated contour has four points,
		# then we can assume we have found the paper
		if len(approx) == 4:
			docCnt = approx
			break
paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))
cv2.imshow("gosterme paper", paper)                            # Show image
cv2.waitKey(0) 

import cv2
crop_img = warped[77:1045, 0:500]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)


thresh = cv2.threshold(crop_img, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#bu kısımda kesme işlemi yapabilirsin ad ve soyad için

thresh = cv2.resize(thresh, (870, 870)) 



#cv2.imshow("gosterme", thresh)                            # Show image


"""

şimdi sallama zamanı

#kontrolcüm
for i in range (1,40):
    try:
        
        rows = np.vsplit(thresh,i)
        print(i)
    except:
        print("hata")
        
"""



"""

Farklı yöntem kullancam

"""

def splitBoxes(img):
        
    rows = np.hsplit(img,15)
    boxes =[]
    for r in rows:
        cols = np.vsplit(r,29)
        for box in cols:
            boxes.append(box)
            #cv2.imshow("split",box)
            #cv2.waitKey(0) 
    return boxes

boxes=splitBoxes(thresh)
#cv2.imshow("test",boxes[3])

print(cv2.countNonZero(boxes[1]),cv2.countNonZero(boxes[5]))
#cv2.waitKey(0) 
#cols = np.hsplit(thresh,15)   
#cv2.imshow("split",cols[10])
#cv2.waitKey(0) 

#cevap alma

myPixelVal=np.zeros((15,29))

countC=0
countR=0

for image in boxes:
    totalPixels = cv2.countNonZero(image)
    myPixelVal[countC][countR]=totalPixels
    countR +=1
    if (countR==29):countC +=1 ;countR=0
print(myPixelVal)
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
    if kontrol_veri >= 700: 
        myIndexVal=np.where(arr==np.amax(arr))
        print(myIndexVal[0])
        harfler.append(myIndexVal[0][0])

adi_soyadi=[]
for i in range (0,len(harfler)):
    print(i)
    haf_bul=harfler[i]
    
    adi_soyadi.append(sozluk[str(haf_bul)])
print(adi_soyadi)

