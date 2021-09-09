try:  
    # -*- coding: utf-8 -*-
    """
    Created on Mon Sep  6 15:09:09 2021
    
    @author: yazılım
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
    
    
    path = input(str("dosya adı: "))
    
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
    
    
    crop_img_1 = imgWarpColored[8:205, 15:378]
    
    
    cv2.imshow("Sonuç",crop_img_1)
    cv2.waitKey(0) 
    
    crop_img_1 = cv2.resize(crop_img_1, (840, 640)) 
    
    cv2.imshow("Sonuç",crop_img_1)
    cv2.waitKey(0) 
    
    
    #kutucuk bulma için
    
    image=crop_img_1
    
    gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    th1,img_bin = cv2.threshold(gray_scale,150,225,cv2.THRESH_BINARY)
    img_bin=~img_bin
    
    cv2.imshow("split",img_bin)
    cv2.waitKey(0) 
    
    
    
    
    line_min_width = 15
    kernal_h = np.ones((1,line_min_width), np.uint8)
    kernal_v = np.ones((line_min_width,1), np.uint8)
    
    img_bin_h = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_h)
    
    cv2.imshow("split",img_bin_h)
    cv2.waitKey(0) 
    
    
    
    img_bin_v = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_v)
    
    cv2.imshow("split",img_bin_v)
    cv2.waitKey(0) 
    
    
    
    
    img_bin_final=img_bin_h|img_bin_v
    
    cv2.imshow("split",img_bin_final)
    cv2.waitKey(0) 
    
    _, labels, stats,_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    
    for x,y,w,h,area in stats[2:]:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    
    cv2.imshow("split",image)
    cv2.waitKey(0) 
    
    
    final_kernel = np.ones((3,3), np.uint8)
    img_bin_final=cv2.dilate(img_bin_final,final_kernel,iterations=1)
    
    cv2.imshow("split",img_bin_final)
    cv2.waitKey(0) 
    
    
    _, labels, stats,_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    
    
    for x,y,w,h,area in stats[2:]:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    
    cv2.imshow("split",img_bin_final)
    cv2.waitKey(0) 
    
    
    
    okul_kodu_crop = img_bin_final[120:517, 0:305]
    
    cv2.imshow("Sonuç",okul_kodu_crop)
    cv2.waitKey(0)
    
    threshd = cv2.resize(okul_kodu_crop, (840, 640)) 
    
    
    cv2.imshow("Sonuç",threshd)
    cv2.waitKey(0)
    
    
    thresh = cv2.threshold(threshd, 0, 255,
    	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    
    cv2.imshow("Sonuç",thresh)
    cv2.waitKey(0)
    
    
    #kontrolcüm
    for i in range (1,50):
        try:
            
            rows = np.hsplit(thresh,i),
    
                
            #print(i)
        except:
            pass
            #print("hata")
    
    
    
    def splitBoxes(img):
            
        
        #rows = np.hsplit(threshd,5)
        rows = np.vsplit(thresh,10)    
        ##cv2.imshow("split",rows[5])
        ##cv2.waitKey(0) 
     
        boxes =[]
        for r in rows:
            cols = np.hsplit(r,8)
            
            ##cv2.imshow("split",cols[0])
            ##cv2.waitKey(0) 
            for box in cols:
                boxes.append(box)
                #cv2.imshow("split",box)
                #cv2.waitKey(0) 
        return boxes
    
    boxes=splitBoxes(thresh)
    
    
    
    #cevap alma
    
    myPixelVal=np.zeros((10,8))
    
    
    countC=0
    countR=0
    cvp_sil=[]
    for image in boxes:
        totalPixels = cv2.countNonZero(image)
        cvp_sil.append(totalPixels)
    
    cvp_sil=np.array(cvp_sil)
    cvp_sil=cvp_sil.reshape(10,8)
    
    myPixelVal=cvp_sil
    
    
    myPixelVal[0][0]
    
    
    okul_kodu_pikselleri=myPixelVal
    
    
    
    sayac=0
    sınav_kodu_buldum=[]
    numara_kontrolcu=[]
    ekleme_listesi_deneme=[]
    ekleme_listesi_deneme_sonucu=0
    for x in range(0,8):
        for deneme in range (0,10):
    
        
            
            arr=okul_kodu_pikselleri[deneme][x]
            ##print(arr)
            
            
            ekleme_listesi_deneme.append(arr)
            
            #deneme
            
            
      
    
        ekleme_listesi_deneme.sort()
        
        ekleme_listesi_deneme_sonucu=ekleme_listesi_deneme[0]
        ekleme_listesi_deneme=[]
        for deneme in range(0,10):
            arr=okul_kodu_pikselleri[deneme][x]
            if arr == ekleme_listesi_deneme_sonucu:
        
        
        
        
    
                      #print("arr: ",arr)
                      #print("x",x)
                      if deneme==0:
                          numara_kontrolcu.append(0)
                          break
                      elif deneme== 1:
                          numara_kontrolcu.append(1)
                          break
                      elif deneme== 2:
                          numara_kontrolcu.append(2)
                          break
                      elif deneme== 3:
                          numara_kontrolcu.append(3)
                          break
                      elif deneme== 4:
                          numara_kontrolcu.append(4)
                          break
                      elif deneme== 5:
                          numara_kontrolcu.append(5)
                          break
                      elif deneme== 6:
                          numara_kontrolcu.append(6)
                          break
                      elif deneme== 7:
                          numara_kontrolcu.append(7)
                          break
                      elif deneme== 8:
                          numara_kontrolcu.append(8)
                          break
                      elif deneme== 9:
                          numara_kontrolcu.append(9)
                          break
    
    print("okul kodu numarası: ", numara_kontrolcu)
    
    ###############################################################################################
    
    # Öğrenci numarası kısmı
    
    #################################################################################
    
    
    
    
    
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
    
    
    crop_img_1 = imgWarpColored[8:205, 15:378]
    
    
    cv2.imshow("Sonuç",crop_img_1)
    cv2.waitKey(0) 
    
    crop_img_1 = cv2.resize(crop_img_1, (840, 640)) 
    
    cv2.imshow("Sonuç",crop_img_1)
    cv2.waitKey(0) 
    
    
    #kutucuk bulma için
    
    image=crop_img_1
    
    gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    th1,img_bin = cv2.threshold(gray_scale,150,225,cv2.THRESH_BINARY)
    img_bin=~img_bin
    
    cv2.imshow("split",img_bin)
    cv2.waitKey(0) 
    
    
    
    
    line_min_width = 15
    kernal_h = np.ones((1,line_min_width), np.uint8)
    kernal_v = np.ones((line_min_width,1), np.uint8)
    
    img_bin_h = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_h)
    
    cv2.imshow("split",img_bin_h)
    cv2.waitKey(0) 
    
    
    
    img_bin_v = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_v)
    
    cv2.imshow("split",img_bin_v)
    cv2.waitKey(0) 
    
    
    
    
    img_bin_final=img_bin_h|img_bin_v
    
    cv2.imshow("split",img_bin_final)
    cv2.waitKey(0) 
    
    _, labels, stats,_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    
    for x,y,w,h,area in stats[2:]:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    
    cv2.imshow("split",image)
    cv2.waitKey(0) 
    
    
    final_kernel = np.ones((3,3), np.uint8)
    img_bin_final=cv2.dilate(img_bin_final,final_kernel,iterations=1)
    
    cv2.imshow("split",img_bin_final)
    cv2.waitKey(0) 
    
    
    _, labels, stats,_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    
    
    for x,y,w,h,area in stats[2:]:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    
    cv2.imshow("split",img_bin_final)
    cv2.waitKey(0) 
    
    
    
    okul_kodu_crop = img_bin_final[120:520, 355:550]
    
    cv2.imshow("Sonuç",okul_kodu_crop)
    cv2.waitKey(0)
    
    threshd = cv2.resize(okul_kodu_crop, (840, 640)) 
    
    
    cv2.imshow("Sonuç",threshd)
    cv2.waitKey(0)
    
    
    thresh = cv2.threshold(threshd, 0, 255,
    	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    
    cv2.imshow("Sonuç",thresh)
    cv2.waitKey(0)
    
    
    
    
    
    
    #kontrolcüm
    for i in range (1,50):
        try:
            
            rows = np.hsplit(thresh,i),
    
                
            #print(i)
        except:
            pass
            #print("hata")
    
    
    
    def splitBoxes(img):
            
        
        #rows = np.hsplit(threshd,5)
        rows = np.vsplit(thresh,10)    
        ###cv2.imshow("split",rows[5])
        ###cv2.waitKey(0) 
     
        boxes =[]
        for r in rows:
            cols = np.hsplit(r,5)
            
            ###cv2.imshow("split",cols[0])
            ###cv2.waitKey(0) 
            for box in cols:
                boxes.append(box)
                ##cv2.imshow("split",box)
                ##cv2.waitKey(0) 
        return boxes
    
    boxes=splitBoxes(thresh)
    
    
    
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
    
    myPixelVal=cvp_sil
    
    
    myPixelVal[0][0]
    
    
    okul_kodu_pikselleri=myPixelVal
    
    
    
    sayac=0
    sınav_kodu_buldum=[]
    numara_kontrolcu=[]
    ekleme_listesi_deneme=[]
    ekleme_listesi_deneme_sonucu=0
    
    
    
    
    
    
    
    for x in range(0,5):
        for deneme in range (0,10):
    
        
            
            arr=okul_kodu_pikselleri[deneme][x]
            ##print(arr)
            
            
            ekleme_listesi_deneme.append(arr)
            
            #deneme
            
            
      
    
        ekleme_listesi_deneme.sort()
        
        ekleme_listesi_deneme_sonucu=ekleme_listesi_deneme[0]
        ekleme_listesi_deneme=[]
        for deneme in range(0,10):
            arr=okul_kodu_pikselleri[deneme][x]
            if arr == ekleme_listesi_deneme_sonucu:
        
        
        
        
    
                      #print("arr: ",arr)
                      #print("x",x)
                      if deneme==0:
                          numara_kontrolcu.append(0)
                          break
                      elif deneme== 1:
                          numara_kontrolcu.append(1)
                          break
                      elif deneme== 2:
                          numara_kontrolcu.append(2)
                          break
                      elif deneme== 3:
                          numara_kontrolcu.append(3)
                          break
                      elif deneme== 4:
                          numara_kontrolcu.append(4)
                          break
                      elif deneme== 5:
                          numara_kontrolcu.append(5)
                          break
                      elif deneme== 6:
                          numara_kontrolcu.append(6)
                          break
                      elif deneme== 7:
                          numara_kontrolcu.append(7)
                          break
                      elif deneme== 8:
                          numara_kontrolcu.append(8)
                          break
                      elif deneme== 9:
                          numara_kontrolcu.append(9)
                          break
    
    print("öğrenci kodu numarası: ", numara_kontrolcu)
    
    
    """
    
    Sınıf şube
    
    """
    
    
    """
    
    ALAN
    
    """
    
    
    """
    
    KİTAPÇIK
    
    """
    
    
    """
    
    TÜRKÇE
    
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
    
    
    crop_img_1 = imgWarpColored[0:800, 350:800]
    
    
    cv2.imshow("Sonuç",crop_img_1)
    cv2.waitKey(0) 
    
    crop_img_1 = cv2.resize(crop_img_1, (840, 640)) 
    
    cv2.imshow("Sonuç",crop_img_1)
    cv2.waitKey(0) 
    
    
    #kutucuk bulma için
    
    image=crop_img_1
    
    gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    th1,img_bin = cv2.threshold(gray_scale,150,225,cv2.THRESH_BINARY)
    img_bin=~img_bin
    
    cv2.imshow("split",img_bin)
    cv2.waitKey(0) 
    
    
    
    
    line_min_width = 15
    kernal_h = np.ones((1,line_min_width), np.uint8)
    kernal_v = np.ones((line_min_width,1), np.uint8)
    
    img_bin_h = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_h)
    
    cv2.imshow("split",img_bin_h)
    cv2.waitKey(0) 
    
    
    
    img_bin_v = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_v)
    
    cv2.imshow("split",img_bin_v)
    cv2.waitKey(0) 
    
    
    
    
    img_bin_final=img_bin_h|img_bin_v
    
    cv2.imshow("split",img_bin_final)
    cv2.waitKey(0) 
    
    _, labels, stats,_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    
    for x,y,w,h,area in stats[2:]:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    
    cv2.imshow("split",image)
    cv2.waitKey(0) 
    
    
    final_kernel = np.ones((3,3), np.uint8)
    img_bin_final=cv2.dilate(img_bin_final,final_kernel,iterations=1)
    
    cv2.imshow("split",img_bin_final)
    cv2.waitKey(0) 
    
    
    _, labels, stats,_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    
    
    for x,y,w,h,area in stats[2:]:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    
    cv2.imshow("split",img_bin_final)
    cv2.waitKey(0) 
    
    
    
    okul_kodu_crop = img_bin_final[187:575, 80:232]
    
    cv2.imshow("Sonuç",okul_kodu_crop)
    cv2.waitKey(0)
    
    threshd = cv2.resize(okul_kodu_crop, (840, 640)) 
    
    
    cv2.imshow("Sonuç",threshd)
    cv2.waitKey(0)
    
    
    thresh = cv2.threshold(threshd, 0, 255,
    	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    
    cv2.imshow("Sonuç",thresh)
    cv2.waitKey(0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    threshd = cv2.resize(thresh, (450, 800)) 
    
    
    cv2.imshow("Sonuç",threshd)
    cv2.waitKey(0)
    
    
    #########################################################
    
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
                #cv2.imshow("split",box)
                #cv2.waitKey(0) 
        return boxes
    
    boxes=splitBoxes(threshd)
    
    
    cv2.imshow("test",boxes[19])
    cv2.waitKey(0) 
    
    
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
    
    myPixelVal=cvp_sil
    
    
    
    
    okul_kodu_pikselleri=myPixelVal
    
    ortalama=okul_kodu_pikselleri[0][0]+okul_kodu_pikselleri[0][1]+okul_kodu_pikselleri[0][2]+okul_kodu_pikselleri[0][3]+okul_kodu_pikselleri[0][4]+okul_kodu_pikselleri[1][0]+okul_kodu_pikselleri[1][1]+okul_kodu_pikselleri[1][2]+okul_kodu_pikselleri[1][3]+okul_kodu_pikselleri[1][4]
    ortalama=ortalama/10
    sayac=0
    sınav_kodu_buldum=[]
    numara_kontrolcu=[]
    ekleme_listesi_deneme=[]
    ekleme_listesi_deneme_sonucu=0
    #########################################################
    #sil
    #sil
    
    
    
    
    ####################################################33
    
    sayac=0
    sınav_kodu_buldum=[]
    numara_kontrolcu=[]
    ekleme_listesi_deneme=[]
    ekleme_listesi_deneme_sonucu=0
    
    
    
    for deneme in range(0,40):
        for x in range (0,5):
    
        
            
            arr=okul_kodu_pikselleri[deneme][x]
            ##print(arr)
            
    
                
            ekleme_listesi_deneme.append(arr)
            
            #deneme
            
            
      
    
        ekleme_listesi_deneme.sort()
        
        ekleme_listesi_deneme_sonucu=ekleme_listesi_deneme[0]
        ekleme_listesi_deneme=[]
        for x in range(0,5):
            arr=okul_kodu_pikselleri[deneme][x]
            if arr == ekleme_listesi_deneme_sonucu:
        
        
        
        
    
                      #print("arr: ",arr)
                      #print("x",x)
                      if x==0:
                          numara_kontrolcu.append("A")
                          break
                      elif x== 1:
                          numara_kontrolcu.append("B")
                          break
                      elif x== 2:
                          numara_kontrolcu.append("C")
                          break
                      elif x== 3:
                          numara_kontrolcu.append("D")
                          break
                      elif x== 4:
                          numara_kontrolcu.append("E")
                          break
      
    print("türkçe cevap anahtarı")                 
    sayac_1=0              
    for numara in numara_kontrolcu:
        sayac_1=sayac_1+1
        print(str(sayac_1)+" :"+str(numara))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    
    SOSYAL
    
    """
    
    
    """
    
    TEMEL MATEMATİK
    
    """
    
    """
    
    FEN
    
    """
    
    """
    
    AD-SOYAD
    
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
    
    thresh_2 = cv2.threshold(crop_img_2, 0, 255,
    	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    
    thresh_3 = cv2.threshold(crop_img_3, 0, 255,
    	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    
    
    
    
    threshd = cv2.resize(thresh, (840, 640)) 
    
    cv2.imshow("Sonuç",threshd)
    cv2.waitKey(0)
    
    
    
    #####################################################################################
    
    threshd = cv2.resize(thresh, (840, 640)) 
    
    cv2.imshow("Sonuç",threshd)
    cv2.waitKey(0)
    
    sınıf_kodu_crop = threshd[120:520, 640:670]
    
    cv2.imshow("Sonuç",sınıf_kodu_crop)
    cv2.waitKey(0)
    
    threshd = cv2.resize(sınıf_kodu_crop, (840, 640)) 
    
    
    cv2.imshow("Sonuç",threshd)
    cv2.waitKey(0)
    
    #kontrolcüm
    for i in range (1,50):
        try:
            
            rows = np.hsplit(threshd,i),
    
                
            #print(i)
        except:
            pass
            #print("hata")
    
    
    #########################################################
    
    def splitBoxes(img):
            
        
        #rows = np.hsplit(threshd,5)
        rows = np.vsplit(threshd,5)    
        ##cv2.imshow("split",rows[5])
        ##cv2.waitKey(0) 
     
        boxes =[]
        for r in rows:
            cols = np.hsplit(r,1)
            
            ##cv2.imshow("split",cols[0])
            ##cv2.waitKey(0) 
            for box in cols:
                boxes.append(box)
                #cv2.imshow("split",box)
                #cv2.waitKey(0) 
        return boxes
    
    boxes=splitBoxes(thresh)
    
    
    
    #cevap alma
    
    myPixelVal=np.zeros((5,1))
    
    
    countC=0
    countR=0
    cvp_sil=[]
    for image in boxes:
        totalPixels = cv2.countNonZero(image)
        cvp_sil.append(totalPixels)
    
    cvp_sil=np.array(cvp_sil)
    cvp_sil=cvp_sil.reshape(5,1)
    
    myPixelVal=cvp_sil
    
    
    
    
    okul_kodu_pikselleri=myPixelVal
    
    
    
    sayac=0
    sınav_kodu_buldum=[]
    numara_kontrolcu=[]
    ekleme_listesi_deneme=[]
    ekleme_listesi_deneme_sonucu=0
    #########################################################
    
    for x in range(0,1):
        for deneme in range (0,5):
    
        
            
            arr=okul_kodu_pikselleri[deneme][x]
            ##print(arr)
            
            
            ekleme_listesi_deneme.append(arr)
            
            #deneme
            
            
      
    
        ekleme_listesi_deneme.sort(reverse=True)
        
        ekleme_listesi_deneme_sonucu=ekleme_listesi_deneme[0]
        ekleme_listesi_deneme=[]
        for deneme in range(0,10):
            arr=okul_kodu_pikselleri[deneme][x]
            if arr == ekleme_listesi_deneme_sonucu:
        
        
        
        
    
                      #print("arr: ",arr)
                      #print("x",x)
                      if deneme==0:
                          numara_kontrolcu.append("9")
                          break
                      elif deneme== 1:
                          numara_kontrolcu.append("10")
                          break
                      elif deneme== 2:
                          numara_kontrolcu.append("11")
                          break
                      elif deneme== 3:
                          numara_kontrolcu.append("12")
                          break
                      elif deneme== 4:
                          numara_kontrolcu.append("Mezun")
                          break
                     
    
    print("sınıf kodu numarası: ", numara_kontrolcu)
    
    #####################################################################################
    
    
    #####################################################################################
    
    threshd = cv2.resize(thresh, (840, 640)) 
    
    cv2.imshow("Sonuç",threshd)
    cv2.waitKey(0)
    
    sube_kodu_crop = threshd[123:520, 680:710]
    
    cv2.imshow("Sonuç",sube_kodu_crop)
    cv2.waitKey(0)
    
    threshd = cv2.resize(sube_kodu_crop, (840, 640)) 
    
    
    cv2.imshow("Sonuç",threshd)
    cv2.waitKey(0)
    
    #kontrolcüm
    for i in range (1,50):
        try:
            
            rows = np.hsplit(threshd,i),
    
                
            #print(i)
        except:
            pass
            #print("hata")
    
    
    #########################################################
    
    def splitBoxes(img):
            
        
        #rows = np.hsplit(threshd,5)
        rows = np.vsplit(threshd,10)    
        ##cv2.imshow("split",rows[5])
        ##cv2.waitKey(0) 
     
        boxes =[]
        for r in rows:
            cols = np.hsplit(r,1)
            
            ##cv2.imshow("split",cols[0])
            ##cv2.waitKey(0) 
            for box in cols:
                boxes.append(box)
                #cv2.imshow("split",box)
                #cv2.waitKey(0) 
        return boxes
    
    boxes=splitBoxes(thresh)
    
    
    
    #cevap alma
    
    myPixelVal=np.zeros((10,1))
    
    
    countC=0
    countR=0
    cvp_sil=[]
    for image in boxes:
        totalPixels = cv2.countNonZero(image)
        cvp_sil.append(totalPixels)
    
    cvp_sil=np.array(cvp_sil)
    cvp_sil=cvp_sil.reshape(10,1)
    
    myPixelVal=cvp_sil
    
    
    
    
    okul_kodu_pikselleri=myPixelVal
    
    
    
    sayac=0
    sınav_kodu_buldum=[]
    numara_kontrolcu=[]
    ekleme_listesi_deneme=[]
    ekleme_listesi_deneme_sonucu=0
    #########################################################
    
    for x in range(0,1):
        for deneme in range (0,10):
    
        
            
            arr=okul_kodu_pikselleri[deneme][x]
            ##print(arr)
            
            
            ekleme_listesi_deneme.append(arr)
            
            #deneme
            
            
      
    
        ekleme_listesi_deneme.sort(reverse=True)
        
        ekleme_listesi_deneme_sonucu=ekleme_listesi_deneme[0]
        ekleme_listesi_deneme=[]
        for deneme in range(0,10):
            arr=okul_kodu_pikselleri[deneme][x]
            if arr == ekleme_listesi_deneme_sonucu:
        
        
        
        
    
                      #print("arr: ",arr)
                      #print("x",x)
                      if deneme==0:
                          numara_kontrolcu.append("A")
                          break
                      elif deneme== 1:
                          numara_kontrolcu.append("B")
                          break
                      elif deneme== 2:
                          numara_kontrolcu.append("C")
                          break
                      elif deneme== 3:
                          numara_kontrolcu.append("Ç")
                          break
                      elif deneme== 4:
                          numara_kontrolcu.append("D")
                          break
                      elif deneme== 5:
                          numara_kontrolcu.append("E")
                          break
                      elif deneme== 6:
                          numara_kontrolcu.append("F")
                          break
                      elif deneme== 7:
                          numara_kontrolcu.append("G")
                          break
                      elif deneme== 8:
                          numara_kontrolcu.append("Ğ")
                          break
                      elif deneme== 9:
                          numara_kontrolcu.append("H")
                          break
                     
                     
    
    print("şube kodu numarası: ", numara_kontrolcu)
except:
    input("batu")
    pass