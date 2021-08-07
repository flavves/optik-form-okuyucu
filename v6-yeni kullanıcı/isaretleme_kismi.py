# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:45:28 2021

@author: yazılım
"""


"""

Cevap işaretleyici


"""



# örnek fotoğrafımızı alalım

import cv2
   

path_isaret = r'ornekler/orijinal_optik_form.jpg'
   

image_isaret = cv2.imread(path_isaret)
   

window_name = 'image_isaret_isaret'
  




sayac_uzun=0
sayac_yatay=0


y=94

x_ler=[68,94,120,145,171]
x1_ler=[222,248,274,299,325]
x2_ler=[374,400,425,450,475]
while 1:
    
    
    try:
        x=x_ler[sayac_yatay]    
        center_coordinates = (x, y)
        
        radius = 8
      
    
        color = (0, 255, 0)
          
        
        thickness = 3
          
        
        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
        
        sayac_yatay=sayac_yatay+1
        
        if sayac_yatay==5:
            sayac_uzun=sayac_uzun+1
            sayac_yatay=0
            y=y+26
        if sayac_uzun==15:
            break
    except:
        break



sayac_uzun=0
sayac_yatay=0


y=94
while 1:
    
    
    try:
        x=x1_ler[sayac_yatay]    
        center_coordinates = (x, y)
        
        radius = 8
      
    
        color = (0, 255, 0)
          
        
        thickness = 3
          
        
        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
        
        sayac_yatay=sayac_yatay+1
        
        if sayac_yatay==5:
            sayac_uzun=sayac_uzun+1
            sayac_yatay=0
            y=y+26
        if sayac_uzun==15:
            break
    except:
        break
    




sayac_uzun=0
sayac_yatay=0


y=94
while 1:
    
    
    try:
        x=x2_ler[sayac_yatay]    
        center_coordinates = (x, y)
        
        radius = 8
      
    
        color = (0, 255, 0)
          
        
        thickness = 3
          
        
        image_isaret = cv2.circle(image_isaret, center_coordinates, radius, color, thickness)
        
        sayac_yatay=sayac_yatay+1
        
        if sayac_yatay==5:
            sayac_uzun=sayac_uzun+1
            sayac_yatay=0
            y=y+26
        if sayac_uzun==10:
            break
    except:
        break
    

cv2.imshow(window_name, image_isaret)
cv2.waitKey(0)    



