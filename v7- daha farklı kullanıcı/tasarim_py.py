# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:06:41 2020
batuhan ökmen
@author: okmen
"""

def anaMenu():
    
    global menusecim
    
    print("""
  ═════════════════════════════════════════════════════

             https://batuhanokmen.com/
      

  ═════════════════════════════════════════════════════ """)  





import json
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2


import sys

from PyQt5.QtWidgets import *

from PyQt5.QtCore import pyqtSignal

from optik_form_oluşturucu_python import Ui_MainWindow

from tasarim_ders_ekle import MainWindow2


        
def ceviriProgramim():
    
    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            
            #obur formdan sinyal almak için
            
            self.ders_ekle_object= MainWindow2()
            #Butonları tanımlama
            self.ui.pushButton_2.clicked.connect(self.ders_eklek)
            self.ders_ekle_object.veri_gonderisi.connect(self.dersler_eklendi)

        def ders_eklek(self):
            self.ders_ekle_object.show()
        def dersler_eklendi(self, veriler):
            print(veriler)
            veriler=veriler.split(",")
            
            

            
            turkce = cv2.imread("ornekler/turkce.png")
            matematik = cv2.imread("ornekler/matematik.png")
            fen = cv2.imread("ornekler/fen.png")
            sosyal = cv2.imread("ornekler/sosyal.png")
            
            bir_sayac=0
            
            for bir in veriler:
                if bir =="1":
                        
                    bir_sayac=bir_sayac+1
            
            
     
            
            
            
            l_img = cv2.imread("ornekler/optik_tekli.png")
            
            y1_offset=200
            x1_offset=50
            
            y2_offset=200
            x2_offset=450
            
            y3_offset=200
            x3_offset=850
            
            y4_offset=200
            x4_offset=1250
            
            
            
            turkce_y=100
            turkce_x=130
            
            matematik_y=100
            matematik_x=500
            
            fen_y=100
            fen_x=930
            
            sosyal_y=100
            sosyal_x=1330
            
            
            s_img = cv2.imread("ornekler/10.png")
            s2_img = cv2.imread("ornekler/20.png")
            s3_img = cv2.imread("ornekler/30.png")
            s4_img = cv2.imread("ornekler/40.png")
            
            
            
              
            
            
            if bir_sayac==1:
                  
                
                if veriler[0]=="1":
                    print("olması")  
                    turkce_y=100
                    turkce_x=130
                    l_img[turkce_y:turkce_y+turkce.shape[0], turkce_x:turkce_x+turkce.shape[1]] = turkce
                    

                if veriler[1]=="1":
                    matematik_y=100
                    matematik_x=130
                    l_img[matematik_y:matematik_y+matematik.shape[0], matematik_x:matematik_x+matematik.shape[1]] = matematik

                if veriler[2]=="1":
                    fen_y=100
                    fen_x=130
                    l_img[fen_y:fen_y+fen.shape[0], fen_x:fen_x+fen.shape[1]] = fen
                if veriler[3]=="1":
                    sosyal_y=100
                    sosyal_x=130
                    l_img[sosyal_y:sosyal_y+sosyal.shape[0], sosyal_x:sosyal_x+sosyal.shape[1]] = sosyal

            elif bir_sayac==2:
                    
                
                if veriler[0]=="1":
                    turkce_y=100
                    turkce_x=130
                    l_img[turkce_y:turkce_y+turkce.shape[0], turkce_x:turkce_x+turkce.shape[1]] = turkce
                if veriler[1]=="1":
                    matematik_y=100
                    matematik_x=500
                    l_img[matematik_y:matematik_y+matematik.shape[0], matematik_x:matematik_x+matematik.shape[1]] = matematik

                if veriler[2]=="1":
                    fen_y=100
                    fen_x=500
                    l_img[fen_y:fen_y+fen.shape[0], fen_x:fen_x+fen.shape[1]] = fen
                if veriler[3]=="1":
                    sosyal_y=100
                    sosyal_x=500
                    l_img[sosyal_y:sosyal_y+sosyal.shape[0], sosyal_x:sosyal_x+sosyal.shape[1]] = sosyal
            elif bir_sayac==3:
                    
                
                if veriler[0]=="1":
                    turkce_y=100
                    turkce_x=130
                    l_img[turkce_y:turkce_y+turkce.shape[0], turkce_x:turkce_x+turkce.shape[1]] = turkce
                if veriler[1]=="1":
                    matematik_y=100
                    matematik_x=500
                    l_img[matematik_y:matematik_y+matematik.shape[0], matematik_x:matematik_x+matematik.shape[1]] = matematik
                if veriler[2]=="1":
                    fen_y=100
                    fen_x=930
                    l_img[fen_y:fen_y+fen.shape[0], fen_x:fen_x+fen.shape[1]] = fen
                if veriler[3]=="1":
                    sosyal_y=100
                    sosyal_x=930
                    l_img[sosyal_y:sosyal_y+sosyal.shape[0], sosyal_x:sosyal_x+sosyal.shape[1]] = sosyal
            elif bir_sayac==4:
                    
                
                if veriler[0]=="1":
                    turkce_y=100
                    turkce_x=130
                    l_img[turkce_y:turkce_y+turkce.shape[0], turkce_x:turkce_x+turkce.shape[1]] = turkce
                if veriler[1]=="1":
                    matematik_y=100
                    matematik_x=500
                    l_img[matematik_y:matematik_y+matematik.shape[0], matematik_x:matematik_x+matematik.shape[1]] = matematik
                if veriler[2]=="1":
                    fen_y=100
                    fen_x=500
                    l_img[fen_y:fen_y+fen.shape[0], fen_x:fen_x+fen.shape[1]] = fen
                if veriler[3]=="1":
                    sosyal_y=100
                    sosyal_x=1330
                    l_img[sosyal_y:sosyal_y+sosyal.shape[0], sosyal_x:sosyal_x+sosyal.shape[1]] = sosyal
            
            
       
            
            
            
            if veriler[4]=="10":   
                if bir_sayac==1:
                    l_img[y1_offset:y1_offset+s_img.shape[0], x1_offset:x1_offset+s_img.shape[1]] = s_img
                elif bir_sayac==2:
                    l_img[y1_offset:y1_offset+s_img.shape[0], x1_offset:x1_offset+s_img.shape[1]] = s_img
                    l_img[y2_offset:y2_offset+s_img.shape[0], x2_offset:x2_offset+s_img.shape[1]] = s_img
                elif bir_sayac==3:
                    l_img[y1_offset:y1_offset+s_img.shape[0], x1_offset:x1_offset+s_img.shape[1]] = s_img
                    l_img[y2_offset:y2_offset+s_img.shape[0], x2_offset:x2_offset+s_img.shape[1]] = s_img
                    l_img[y3_offset:y3_offset+s_img.shape[0], x3_offset:x3_offset+s_img.shape[1]] = s_img
                elif bir_sayac==4:
                    l_img[y1_offset:y1_offset+s_img.shape[0], x1_offset:x1_offset+s_img.shape[1]] = s_img
                    l_img[y2_offset:y2_offset+s_img.shape[0], x2_offset:x2_offset+s_img.shape[1]] = s_img
                    l_img[y3_offset:y3_offset+s_img.shape[0], x3_offset:x3_offset+s_img.shape[1]] = s_img
                    l_img[y4_offset:y4_offset+s_img.shape[0], x4_offset:x4_offset+s_img.shape[1]] = s_img
                    
            elif veriler[4]=="20":
                if bir_sayac==1:
                    l_img[y1_offset:y1_offset+s2_img.shape[0], x1_offset:x1_offset+s2_img.shape[1]] = s2_img
                elif bir_sayac==2:
                    l_img[y1_offset:y1_offset+s2_img.shape[0], x1_offset:x1_offset+s2_img.shape[1]] = s2_img
                    l_img[y2_offset:y2_offset+s2_img.shape[0], x2_offset:x2_offset+s2_img.shape[1]] = s2_img
                elif bir_sayac==3:
                    l_img[y1_offset:y1_offset+s2_img.shape[0], x1_offset:x1_offset+s2_img.shape[1]] = s2_img
                    l_img[y2_offset:y2_offset+s2_img.shape[0], x2_offset:x2_offset+s2_img.shape[1]] = s2_img
                    l_img[y3_offset:y3_offset+s2_img.shape[0], x3_offset:x3_offset+s2_img.shape[1]] = s2_img
                elif bir_sayac==4:
                    l_img[y1_offset:y1_offset+s2_img.shape[0], x1_offset:x1_offset+s2_img.shape[1]] = s2_img
                    l_img[y2_offset:y2_offset+s2_img.shape[0], x2_offset:x2_offset+s2_img.shape[1]] = s2_img
                    l_img[y3_offset:y3_offset+s2_img.shape[0], x3_offset:x3_offset+s2_img.shape[1]] = s2_img
                    l_img[y4_offset:y4_offset+s2_img.shape[0], x4_offset:x4_offset+s2_img.shape[1]] = s2_img
                    
            elif veriler[4]=="30":
                if bir_sayac==1:
                    l_img[y1_offset:y1_offset+s3_img.shape[0], x1_offset:x1_offset+s3_img.shape[1]] = s3_img
                elif bir_sayac==2:
                    l_img[y1_offset:y1_offset+s3_img.shape[0], x1_offset:x1_offset+s3_img.shape[1]] = s3_img
                    l_img[y2_offset:y2_offset+s3_img.shape[0], x2_offset:x2_offset+s3_img.shape[1]] = s3_img
                elif bir_sayac==3:
                    l_img[y1_offset:y1_offset+s3_img.shape[0], x1_offset:x1_offset+s3_img.shape[1]] = s3_img
                    l_img[y2_offset:y2_offset+s3_img.shape[0], x2_offset:x2_offset+s3_img.shape[1]] = s3_img
                    l_img[y3_offset:y3_offset+s3_img.shape[0], x3_offset:x3_offset+s3_img.shape[1]] = s3_img
                elif bir_sayac==4:
                    l_img[y1_offset:y1_offset+s3_img.shape[0], x1_offset:x1_offset+s3_img.shape[1]] = s3_img
                    l_img[y2_offset:y2_offset+s3_img.shape[0], x2_offset:x2_offset+s3_img.shape[1]] = s3_img
                    l_img[y3_offset:y3_offset+s3_img.shape[0], x3_offset:x3_offset+s3_img.shape[1]] = s3_img
                    l_img[y4_offset:y4_offset+s3_img.shape[0], x4_offset:x4_offset+s3_img.shape[1]] = s3_img
                    
            elif veriler[4]=="40":
                if bir_sayac==1:
                    l_img[y1_offset:y1_offset+s4_img.shape[0], x1_offset:x1_offset+s4_img.shape[1]] = s4_img
                elif bir_sayac==2:
                    l_img[y1_offset:y1_offset+s4_img.shape[0], x1_offset:x1_offset+s4_img.shape[1]] = s4_img
                    l_img[y2_offset:y2_offset+s4_img.shape[0], x2_offset:x2_offset+s4_img.shape[1]] = s4_img
                elif bir_sayac==3:
                    l_img[y1_offset:y1_offset+s4_img.shape[0], x1_offset:x1_offset+s4_img.shape[1]] = s4_img
                    l_img[y2_offset:y2_offset+s4_img.shape[0], x2_offset:x2_offset+s4_img.shape[1]] = s4_img
                    l_img[y3_offset:y3_offset+s4_img.shape[0], x3_offset:x3_offset+s4_img.shape[1]] = s4_img
                elif bir_sayac==4:
                    l_img[y1_offset:y1_offset+s4_img.shape[0], x1_offset:x1_offset+s4_img.shape[1]] = s4_img
                    l_img[y2_offset:y2_offset+s4_img.shape[0], x2_offset:x2_offset+s4_img.shape[1]] = s4_img
                    l_img[y3_offset:y3_offset+s4_img.shape[0], x3_offset:x3_offset+s4_img.shape[1]] = s4_img
                    l_img[y4_offset:y4_offset+s4_img.shape[0], x4_offset:x4_offset+s4_img.shape[1]] = s4_img
                    
            
            
            
            
            

            
            
            
            
            gostermelik = cv2.resize(l_img, (1500, 750)) 
            
            cv2.imshow("Sonuç",gostermelik)
            cv2.waitKey(0) 
            
            
            cv2.imwrite("Sonuc.png", l_img)
       
    
    if __name__ == "__main__":
        app = QApplication(sys.argv)
    
        window = MainWindow()
        window.setWindowTitle("dene program")
        window.show()
    
        sys.exit(app.exec_())



"""
başlayalım

"""


while True:
    anaMenu()
    secim= 1
    if secim == 1:
        ceviriProgramim()
    else:
        print("Bir hata oluştu")











