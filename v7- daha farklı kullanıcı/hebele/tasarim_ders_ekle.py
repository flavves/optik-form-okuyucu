# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:06:41 2020
batuhan ökmen
@author: okmen
"""
import sys
def anaMenu():
    
    global menusecim
    
    print("""
  ═════════════════════════════════════════════════════

             https://batuhanokmen.com/
      

  ═════════════════════════════════════════════════════ """)  




from PyQt5.QtWidgets import *

from ders_modulu_ekle_python import Ui_MainWindow2

from PyQt5.QtCore import pyqtSignal

class MainWindow2(QMainWindow):
        veri_gonderisi= pyqtSignal(str)
        
        def __init__(self):
            super(MainWindow2, self).__init__()
            self.ui = Ui_MainWindow2()
            self.ui.setupUi(self)
            
            self.ui.pushButton_2.clicked.connect(self.ders_ekeleme_verilerini_gonder)
        
        def ders_ekeleme_verilerini_gonder(self):
            gonderi=[]
            
            if self.ui.checkBox.isChecked(): turkcee="1" 
            else: turkcee="0"
            if self.ui.checkBox_2.isChecked(): matematikk="1" 
            else: matematikk="0"
            if self.ui.checkBox_3.isChecked(): fenn="1" 
            else: fenn="0"
            if self.ui.checkBox_4.isChecked(): sosyall="1" 
            else: sosyall="0"
            
            kac_soruluk_olsun = self.ui.comboBox.currentText()
            gonderme=turkcee+","+matematikk+","+fenn+","+sosyall+","+kac_soruluk_olsun
            #print(gonderme)
            self.veri_gonderisi.emit(gonderme)
            pass
            
            
if __name__ == "__main__":
            app = QApplication(sys.argv)
        
            window = MainWindow2()
            window.setWindowTitle("Translate program")
            window.show()
        
            sys.exit(app.exec_())
    








