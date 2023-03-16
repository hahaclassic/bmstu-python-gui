
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import pyperclip
from CaesarCipher import *
from VigenereCipher import *
from Simple_Substitution_Cipher import *
from transposition_cipher import *
from times_start import start_time
# GUI FILE
from ui_main_17 import Ui_MainWindow
from ui_start_6 import Ui_StartWindow



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Cryptography for beginners")
        
        self.ui.stackedWidget.setCurrentIndex(0)
    
        ## PAGES 
        ########################################################################
        #введение
        self.ui.btn_page_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        # PAGE 4
        self.ui.btn_page_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        # PAGE 5
        self.ui.btn_page_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        # terms
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))

        self.ui.checkBox.setChecked(True)
        self.ui.checkBox_3.setChecked(True)
        self.ui.checkBox_4.setChecked(True)

        button_group_1 = QButtonGroup(self)
        button_group_1.addButton(self.ui.checkBox)
        button_group_1.addButton(self.ui.checkBox_2)
        button_group_2 = QButtonGroup(self)
        button_group_2.addButton(self.ui.checkBox_3)
        button_group_2.addButton(self.ui.checkBox_6)
        button_group_3 = QButtonGroup(self)
        button_group_3.addButton(self.ui.checkBox_4)
        button_group_3.addButton(self.ui.checkBox_7)

        self.ui.pushButton.clicked.connect(self.ui.code_caesar_encrypt)
        self.ui.pushButton_2.clicked.connect(self.ui.code_caesar_decrypt)
        self.ui.pushButton_3.clicked.connect(self.ui.copy_text_1)
        self.ui.pushButton_19.clicked.connect(self.ui.random_key_1)
        self.ui.pushButton_15.clicked.connect(self.ui.delete_1)

        self.ui.pushButton_10.clicked.connect(self.ui.code_transposition_encrypt)
        self.ui.pushButton_12.clicked.connect(self.ui.code_transposition_decrypt)
        self.ui.pushButton_13.clicked.connect(self.ui.copy_text_2)
        self.ui.pushButton_18.clicked.connect(self.ui.random_key_2)
        self.ui.pushButton_21.clicked.connect(self.ui.delete_2)

        self.ui.pushButton_4.clicked.connect(self.ui.code_vigenere_encrypt)
        self.ui.pushButton_5.clicked.connect(self.ui.code_vigenere_decrypt)
        self.ui.pushButton_6.clicked.connect(self.ui.copy_text_3)
        self.ui.pushButton_14.clicked.connect(self.ui.random_key_3)
        self.ui.pushButton_16.clicked.connect(self.ui.delete_3)

        self.ui.pushButton_7.clicked.connect(self.ui.code_sim_sub_encrypt)
        self.ui.pushButton_8.clicked.connect(self.ui.code_sim_sub_decrypt)
        self.ui.pushButton_9.clicked.connect(self.ui.copy_text_4)
        self.ui.pushButton_11.clicked.connect(self.ui.random_key_4)
        self.ui.pushButton_17.clicked.connect(self.ui.delete_4)

        ########################################################################
class StartWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Cryptography for beginners")
        self.ui.textEdit_3.setPlainText(start_time())

class start(QMainWindow):
    def show_window_1(self):
        self.w1 = StartWindow()
        self.w1.ui.pushButton.clicked.connect(self.show_window_2)
        self.w1.ui.pushButton.clicked.connect(self.w1.close)
        self.w1.show()

    def show_window_2(self):
        self.w2 = MainWindow()
        self.w2.show()
        self.w2.ui.Btn_Toggle.clicked.connect(self.show_window_1)
        self.w2.ui.Btn_Toggle.clicked.connect(self.w2.close)

if __name__ == "__main__":
    try:
        from PyQt5.QtWinExtras import QtWin                                  
        myappid = 'mycompany.myproduct.subproduct.version'                        
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)                         
    except ImportError:
        pass
    app = QApplication(sys.argv)
    window = start()
    window.show_window_1()
    app.setWindowIcon(QtGui.QIcon('1122.jpg'))
    window.setWindowIcon(QtGui.QIcon('1122.jpg'))
    sys.exit(app.exec_())
    