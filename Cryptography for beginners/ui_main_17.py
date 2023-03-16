
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from CaesarCipher import *
from VigenereCipher import *
from Simple_Substitution_Cipher import *
from transposition_cipher import *
from Simple_Substitution_Cipher import alphabet_4

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1262, 840)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1262, 840))
        MainWindow.setMaximumSize(QSize(1262, 840))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setGeometry(QRect(0, 0, 100, 40))
        self.frame_toggle.setMaximumSize(QSize(101, 40))
        self.frame_toggle.setStyleSheet(u"background-color:rgb(106, 90, 205);\n"
"")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        self.Btn_Toggle.setGeometry(QRect(0, 0, 100, 40))
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet(u"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setGeometry(QRect(101, 0, 1161, 40))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setCursor(QCursor(Qt.PointingHandCursor))
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(100, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setGeometry(QRect(0, 0, 101, 291))
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setGeometry(QRect(0, 40, 101, 40))
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setGeometry(QRect(0, 120, 101, 40))
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setGeometry(QRect(0, 160, 101, 40))
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setGeometry(QRect(0, 240, 101, 40))
        self.btn_page_4.setMinimumSize(QSize(0, 40))
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.btn_page_6 = QPushButton(self.frame_top_menus)
        self.btn_page_6.setObjectName(u"btn_page_6")
        self.btn_page_6.setGeometry(QRect(0, 0, 101, 40))
        self.btn_page_6.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.btn_page_6.setFont(font1)
        self.btn_page_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.btn_page_5 = QPushButton(self.frame_top_menus)
        self.btn_page_5.setObjectName(u"btn_page_5")
        self.btn_page_5.setGeometry(QRect(0, 80, 101, 40))
        self.btn_page_5.setMinimumSize(QSize(0, 40))
        self.btn_page_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.btn_page_7 = QPushButton(self.frame_top_menus)
        self.btn_page_7.setObjectName(u"btn_page_7")
        self.btn_page_7.setGeometry(QRect(0, 200, 101, 40))
        self.btn_page_7.setMinimumSize(QSize(0, 40))
        self.btn_page_7.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1151, 900))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMinimumSize(QSize(0, 500))
        self.stackedWidget.setStyleSheet(u"")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.textEdit_39 = QTextEdit(self.page_4)
        self.textEdit_39.setObjectName(u"textEdit_39")
        self.textEdit_39.setEnabled(True)
        self.textEdit_39.setGeometry(QRect(10, 0, 1051, 71))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(100)
        sizePolicy2.setHeightForWidth(self.textEdit_39.sizePolicy().hasHeightForWidth())
        self.textEdit_39.setSizePolicy(sizePolicy2)
        self.textEdit_39.setMinimumSize(QSize(500, 30))
        self.textEdit_39.setMaximumSize(QSize(10000, 100))
        self.textEdit_39.setSizeIncrement(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(45, 45, 45, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textEdit_39.setPalette(palette)
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(34)
        font2.setBold(False)
        font2.setWeight(50)
        self.textEdit_39.setFont(font2)
        self.textEdit_39.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit_39.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEdit_39.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_39.setFrameShape(QFrame.NoFrame)
        self.textEdit_39.setFrameShadow(QFrame.Sunken)
        self.textEdit_39.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_39.setLineWrapColumnOrWidth(1)
        self.textEdit_39.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_13 = QFrame(self.page_4)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(10, 80, 1141, 16))
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.textEdit_40 = QTextEdit(self.page_4)
        self.textEdit_40.setObjectName(u"textEdit_40")
        self.textEdit_40.setGeometry(QRect(10, 100, 1141, 681))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(14)
        self.textEdit_40.setFont(font3)
        self.textEdit_40.setFrameShape(QFrame.NoFrame)
        self.textEdit_40.setTextInteractionFlags(Qt.NoTextInteraction)
        self.stackedWidget.addWidget(self.page_4)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.textEdit = QTextEdit(self.page_1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QRect(10, 0, 500, 71))
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(500, 30))
        self.textEdit.setMaximumSize(QSize(300, 100))
        self.textEdit.setSizeIncrement(QSize(0, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textEdit.setPalette(palette1)
        self.textEdit.setFont(font2)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEdit.setLayoutDirection(Qt.LeftToRight)
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setLineWrapColumnOrWidth(1)
        self.textEdit.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line = QFrame(self.page_1)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(170, 80, 991, 31))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setBold(False)
        font4.setWeight(50)
        self.line.setFont(font4)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.textEdit_2 = QTextEdit(self.page_1)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(170, 570, 361, 181))
        self.textEdit_2.setFont(font3)
        self.textEdit_2.setStyleSheet(u"color: white;")
        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(560, 570, 151, 41))
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.pushButton.setFont(font5)
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton.setInputMethodHints(Qt.ImhNone)
        self.pushButton_2 = QPushButton(self.page_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(560, 640, 151, 41))
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.line_2 = QFrame(self.page_1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(150, 170, 1021, 31))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.pushButton_3 = QPushButton(self.page_1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(560, 710, 151, 41))
        self.pushButton_3.setFont(font5)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.textEdit_3 = QTextEdit(self.page_1)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 100, 1141, 81))
        self.textEdit_3.setFont(font3)
        self.textEdit_3.setFrameShape(QFrame.NoFrame)
        self.textEdit_3.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_4 = QTextEdit(self.page_1)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(10, 190, 901, 301))
        font6 = QFont()
        font6.setFamily(u"Century Gothic")
        font6.setPointSize(14)
        font6.setKerning(False)
        self.textEdit_4.setFont(font6)
        self.textEdit_4.setFrameShape(QFrame.NoFrame)
        self.textEdit_4.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_5 = QTextEdit(self.page_1)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(10, 80, 161, 31))
        font7 = QFont()
        font7.setFamily(u"Century Gothic")
        font7.setPointSize(10)
        self.textEdit_5.setFont(font7)
        self.textEdit_5.setFrameShape(QFrame.NoFrame)
        self.textEdit_5.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_6 = QTextEdit(self.page_1)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(10, 170, 141, 31))
        self.textEdit_6.setFont(font7)
        self.textEdit_6.setFrameShape(QFrame.NoFrame)
        self.textEdit_6.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textBrowser = QTextBrowser(self.page_1)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 510, 131, 41))
        font8 = QFont()
        font8.setFamily(u"Century Gothic")
        font8.setPointSize(12)
        self.textBrowser.setFont(font8)
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_3 = QFrame(self.page_1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 480, 1141, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.textEdit_8 = QTextEdit(self.page_1)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(740, 500, 411, 61))
        self.textEdit_8.setFont(font8)
        self.textEdit_8.setFrameShape(QFrame.NoFrame)
        self.textEdit_8.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_9 = QTextEdit(self.page_1)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(20, 570, 141, 41))
        self.textEdit_9.setFont(font8)
        self.textEdit_9.setFrameShape(QFrame.NoFrame)
        self.textEdit_9.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_43 = QTextEdit(self.page_1)
        self.textEdit_43.setObjectName(u"textEdit_43")
        self.textEdit_43.setGeometry(QRect(170, 500, 361, 51))
        font9 = QFont()
        font9.setFamily(u"Century Gothic")
        font9.setPointSize(16)
        self.textEdit_43.setFont(font9)
        self.textEdit_43.setStyleSheet(u"color: white;")
        self.textEdit_7 = QTextEdit(self.page_1)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(740, 570, 361, 181))
        self.textEdit_7.setFont(font3)
        self.textEdit_7.setStyleSheet(u"color: white;")
        self.textEdit_7.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.checkBox = QCheckBox(self.page_1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 620, 121, 31))
        self.checkBox.setFont(font8)
        self.checkBox.setStyleSheet(u"color: white;")
        self.checkBox_2 = QCheckBox(self.page_1)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(30, 660, 121, 31))
        self.checkBox_2.setFont(font8)
        self.checkBox_2.setStyleSheet(u"color: white;")
        self.pushButton_15 = QPushButton(self.page_1)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(20, 710, 121, 41))
        self.pushButton_15.setFont(font5)
        self.pushButton_15.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_15.setInputMethodHints(Qt.ImhNone)
        self.pushButton_19 = QPushButton(self.page_1)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(560, 500, 151, 51))
        self.pushButton_19.setFont(font5)
        self.pushButton_19.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_19.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(930, 220, 221, 251))
        self.label_2.setPixmap(QPixmap(u"photo/caesar2.png"))
        self.line_11 = QFrame(self.page_1)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(910, 220, 20, 251))
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.page_1)
        self.textEdit.raise_()
        self.line.raise_()
        self.textEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.line_2.raise_()
        self.pushButton_3.raise_()
        self.textEdit_5.raise_()
        self.textBrowser.raise_()
        self.textEdit_8.raise_()
        self.textEdit_9.raise_()
        self.textEdit_43.raise_()
        self.textEdit_7.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.pushButton_15.raise_()
        self.pushButton_19.raise_()
        self.label_2.raise_()
        self.line_11.raise_()
        self.textEdit_3.raise_()
        self.textEdit_6.raise_()
        self.textEdit_4.raise_()
        self.line_3.raise_()
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.textEdit_37 = QTextEdit(self.page_5)
        self.textEdit_37.setObjectName(u"textEdit_37")
        self.textEdit_37.setEnabled(True)
        self.textEdit_37.setGeometry(QRect(10, 0, 881, 100))
        sizePolicy2.setHeightForWidth(self.textEdit_37.sizePolicy().hasHeightForWidth())
        self.textEdit_37.setSizePolicy(sizePolicy2)
        self.textEdit_37.setMinimumSize(QSize(500, 30))
        self.textEdit_37.setMaximumSize(QSize(16777215, 100))
        self.textEdit_37.setSizeIncrement(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textEdit_37.setPalette(palette2)
        self.textEdit_37.setFont(font2)
        self.textEdit_37.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit_37.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEdit_37.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_37.setFrameShape(QFrame.NoFrame)
        self.textEdit_37.setFrameShadow(QFrame.Sunken)
        self.textEdit_37.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_37.setLineWrapColumnOrWidth(1)
        self.textEdit_37.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_51 = QTextEdit(self.page_5)
        self.textEdit_51.setObjectName(u"textEdit_51")
        self.textEdit_51.setGeometry(QRect(10, 80, 161, 31))
        self.textEdit_51.setFont(font7)
        self.textEdit_51.setFrameShape(QFrame.NoFrame)
        self.textEdit_51.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_16 = QFrame(self.page_5)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(170, 80, 991, 31))
        self.line_16.setFont(font4)
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.textEdit_49 = QTextEdit(self.page_5)
        self.textEdit_49.setObjectName(u"textEdit_49")
        self.textEdit_49.setGeometry(QRect(10, 110, 1141, 61))
        self.textEdit_49.setFont(font3)
        self.textEdit_49.setFrameShape(QFrame.NoFrame)
        self.textEdit_49.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_52 = QTextEdit(self.page_5)
        self.textEdit_52.setObjectName(u"textEdit_52")
        self.textEdit_52.setGeometry(QRect(10, 170, 141, 31))
        self.textEdit_52.setFont(font7)
        self.textEdit_52.setFrameShape(QFrame.NoFrame)
        self.textEdit_52.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_17 = QFrame(self.page_5)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(150, 170, 1031, 31))
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)
        self.textEdit_50 = QTextEdit(self.page_5)
        self.textEdit_50.setObjectName(u"textEdit_50")
        self.textEdit_50.setGeometry(QRect(10, 200, 811, 281))
        self.textEdit_50.setFont(font3)
        self.textEdit_50.setFrameShape(QFrame.NoFrame)
        self.textEdit_50.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_18 = QFrame(self.page_5)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setGeometry(QRect(10, 480, 1141, 16))
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)
        self.pushButton_21 = QPushButton(self.page_5)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(20, 710, 121, 41))
        self.pushButton_21.setFont(font5)
        self.pushButton_21.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_21.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_21.setInputMethodHints(Qt.ImhNone)
        self.textEdit_54 = QTextEdit(self.page_5)
        self.textEdit_54.setObjectName(u"textEdit_54")
        self.textEdit_54.setGeometry(QRect(20, 570, 131, 41))
        self.textEdit_54.setFont(font8)
        self.textEdit_54.setFrameShape(QFrame.NoFrame)
        self.textEdit_54.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textBrowser_5 = QTextBrowser(self.page_5)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(20, 510, 141, 41))
        self.textBrowser_5.setFont(font8)
        self.textBrowser_5.setFrameShape(QFrame.NoFrame)
        self.textBrowser_5.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_34 = QTextEdit(self.page_5)
        self.textEdit_34.setObjectName(u"textEdit_34")
        self.textEdit_34.setGeometry(QRect(170, 500, 361, 51))
        self.textEdit_34.setFont(font9)
        self.textEdit_34.setStyleSheet(u"color: white;")
        self.textEdit_29 = QTextEdit(self.page_5)
        self.textEdit_29.setObjectName(u"textEdit_29")
        self.textEdit_29.setGeometry(QRect(170, 570, 361, 181))
        self.textEdit_29.setFont(font3)
        self.textEdit_29.setStyleSheet(u"color: white;")
        self.pushButton_10 = QPushButton(self.page_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(560, 570, 151, 41))
        self.pushButton_10.setFont(font5)
        self.pushButton_10.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_10.setInputMethodHints(Qt.ImhNone)
        self.pushButton_12 = QPushButton(self.page_5)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(560, 640, 151, 41))
        self.pushButton_12.setFont(font5)
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_13 = QPushButton(self.page_5)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(560, 710, 151, 41))
        self.pushButton_13.setFont(font5)
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.textEdit_45 = QTextEdit(self.page_5)
        self.textEdit_45.setObjectName(u"textEdit_45")
        self.textEdit_45.setGeometry(QRect(740, 570, 361, 181))
        self.textEdit_45.setFont(font3)
        self.textEdit_45.setStyleSheet(u"color: white;")
        self.textEdit_45.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.textEdit_46 = QTextEdit(self.page_5)
        self.textEdit_46.setObjectName(u"textEdit_46")
        self.textEdit_46.setGeometry(QRect(740, 490, 391, 71))
        font10 = QFont()
        font10.setFamily(u"Century Gothic")
        font10.setPointSize(11)
        self.textEdit_46.setFont(font10)
        self.textEdit_46.setFrameShape(QFrame.NoFrame)
        self.textEdit_46.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton_18 = QPushButton(self.page_5)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(560, 500, 151, 51))
        self.pushButton_18.setFont(font5)
        self.pushButton_18.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_18.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.label = QLabel(self.page_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(840, 200, 311, 271))
        self.label.setPixmap(QPixmap(u"photo/trans3.png"))
        self.line_10 = QFrame(self.page_5)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(820, 200, 20, 271))
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.textEdit_11 = QTextEdit(self.page_2)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setEnabled(True)
        self.textEdit_11.setGeometry(QRect(10, 0, 500, 100))
        sizePolicy2.setHeightForWidth(self.textEdit_11.sizePolicy().hasHeightForWidth())
        self.textEdit_11.setSizePolicy(sizePolicy2)
        self.textEdit_11.setMinimumSize(QSize(500, 30))
        self.textEdit_11.setMaximumSize(QSize(300, 100))
        self.textEdit_11.setSizeIncrement(QSize(0, 0))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textEdit_11.setPalette(palette3)
        self.textEdit_11.setFont(font2)
        self.textEdit_11.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit_11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEdit_11.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_11.setFrameShape(QFrame.NoFrame)
        self.textEdit_11.setFrameShadow(QFrame.Sunken)
        self.textEdit_11.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_11.setLineWrapColumnOrWidth(1)
        self.textEdit_11.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_15 = QTextEdit(self.page_2)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setGeometry(QRect(10, 80, 161, 31))
        self.textEdit_15.setFont(font7)
        self.textEdit_15.setFrameShape(QFrame.NoFrame)
        self.textEdit_15.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_4 = QFrame(self.page_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(180, 80, 991, 31))
        self.line_4.setFont(font4)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.textEdit_13 = QTextEdit(self.page_2)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setGeometry(QRect(10, 110, 1141, 61))
        self.textEdit_13.setFont(font3)
        self.textEdit_13.setFrameShape(QFrame.NoFrame)
        self.textEdit_13.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_16 = QTextEdit(self.page_2)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setGeometry(QRect(10, 170, 141, 31))
        self.textEdit_16.setFont(font7)
        self.textEdit_16.setFrameShape(QFrame.NoFrame)
        self.textEdit_16.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_5 = QFrame(self.page_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(150, 170, 1041, 31))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.textEdit_14 = QTextEdit(self.page_2)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setGeometry(QRect(10, 200, 1141, 281))
        self.textEdit_14.setFont(font3)
        self.textEdit_14.setFrameShape(QFrame.NoFrame)
        self.textEdit_14.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_6 = QFrame(self.page_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 480, 1141, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.textBrowser_2 = QTextBrowser(self.page_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(20, 510, 141, 61))
        self.textBrowser_2.setFont(font8)
        self.textBrowser_2.setFrameShape(QFrame.NoFrame)
        self.textBrowser_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_19 = QTextEdit(self.page_2)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setGeometry(QRect(20, 570, 131, 41))
        self.textEdit_19.setFont(font8)
        self.textEdit_19.setFrameShape(QFrame.NoFrame)
        self.textEdit_19.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_12 = QTextEdit(self.page_2)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setGeometry(QRect(170, 570, 361, 181))
        self.textEdit_12.setFont(font3)
        self.textEdit_12.setStyleSheet(u"color: white;")
        self.textEdit_18 = QTextEdit(self.page_2)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setGeometry(QRect(740, 510, 411, 51))
        self.textEdit_18.setFont(font8)
        self.textEdit_18.setFrameShape(QFrame.NoFrame)
        self.textEdit_18.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton_6 = QPushButton(self.page_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(560, 710, 151, 41))
        self.pushButton_6.setFont(font5)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(560, 640, 151, 41))
        self.pushButton_5.setFont(font5)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(560, 570, 151, 41))
        self.pushButton_4.setFont(font5)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.textEdit_42 = QTextEdit(self.page_2)
        self.textEdit_42.setObjectName(u"textEdit_42")
        self.textEdit_42.setGeometry(QRect(170, 500, 361, 51))
        self.textEdit_42.setFont(font9)
        self.textEdit_42.setStyleSheet(u"color: white;")
        self.textEdit_17 = QTextEdit(self.page_2)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setGeometry(QRect(740, 570, 361, 181))
        self.textEdit_17.setFont(font3)
        self.textEdit_17.setStyleSheet(u"color: white;")
        self.textEdit_17.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.checkBox_3 = QCheckBox(self.page_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(30, 620, 121, 31))
        self.checkBox_3.setFont(font8)
        self.checkBox_3.setStyleSheet(u"color: white")
        self.checkBox_6 = QCheckBox(self.page_2)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(30, 660, 121, 31))
        self.checkBox_6.setFont(font8)
        self.checkBox_6.setStyleSheet(u"color: white")
        self.pushButton_16 = QPushButton(self.page_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(20, 710, 121, 41))
        self.pushButton_16.setFont(font5)
        self.pushButton_16.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_16.setInputMethodHints(Qt.ImhNone)
        self.pushButton_14 = QPushButton(self.page_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(560, 500, 151, 51))
        self.pushButton_14.setFont(font5)
        self.pushButton_14.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_14.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.textEdit_10 = QTextEdit(self.page_3)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setEnabled(True)
        self.textEdit_10.setGeometry(QRect(10, 0, 761, 100))
        sizePolicy2.setHeightForWidth(self.textEdit_10.sizePolicy().hasHeightForWidth())
        self.textEdit_10.setSizePolicy(sizePolicy2)
        self.textEdit_10.setMinimumSize(QSize(500, 30))
        self.textEdit_10.setMaximumSize(QSize(10000, 100))
        self.textEdit_10.setSizeIncrement(QSize(0, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textEdit_10.setPalette(palette4)
        self.textEdit_10.setFont(font2)
        self.textEdit_10.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit_10.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEdit_10.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_10.setFrameShape(QFrame.NoFrame)
        self.textEdit_10.setFrameShadow(QFrame.Sunken)
        self.textEdit_10.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_10.setLineWrapColumnOrWidth(1)
        self.textEdit_10.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_23 = QTextEdit(self.page_3)
        self.textEdit_23.setObjectName(u"textEdit_23")
        self.textEdit_23.setGeometry(QRect(10, 80, 161, 31))
        self.textEdit_23.setFont(font7)
        self.textEdit_23.setFrameShape(QFrame.NoFrame)
        self.textEdit_23.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_7 = QFrame(self.page_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(150, 80, 1011, 31))
        self.line_7.setFont(font4)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.textEdit_21 = QTextEdit(self.page_3)
        self.textEdit_21.setObjectName(u"textEdit_21")
        self.textEdit_21.setGeometry(QRect(10, 100, 1141, 131))
        self.textEdit_21.setFont(font8)
        self.textEdit_21.setFrameShape(QFrame.NoFrame)
        self.textEdit_21.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_24 = QTextEdit(self.page_3)
        self.textEdit_24.setObjectName(u"textEdit_24")
        self.textEdit_24.setGeometry(QRect(10, 200, 141, 31))
        self.textEdit_24.setFont(font7)
        self.textEdit_24.setFrameShape(QFrame.NoFrame)
        self.textEdit_24.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_8 = QFrame(self.page_3)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(150, 200, 1021, 31))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.textEdit_22 = QTextEdit(self.page_3)
        self.textEdit_22.setObjectName(u"textEdit_22")
        self.textEdit_22.setGeometry(QRect(10, 230, 1141, 171))
        self.textEdit_22.setFont(font3)
        self.textEdit_22.setFrameShape(QFrame.NoFrame)
        self.textEdit_22.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textBrowser_3 = QTextBrowser(self.page_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(20, 500, 161, 81))
        self.textBrowser_3.setFont(font8)
        self.textBrowser_3.setFrameShape(QFrame.NoFrame)
        self.textBrowser_3.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_9 = QFrame(self.page_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(10, 480, 1141, 16))
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.textEdit_27 = QTextEdit(self.page_3)
        self.textEdit_27.setObjectName(u"textEdit_27")
        self.textEdit_27.setGeometry(QRect(20, 580, 151, 41))
        self.textEdit_27.setFont(font8)
        self.textEdit_27.setFrameShape(QFrame.NoFrame)
        self.textEdit_27.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton_7 = QPushButton(self.page_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(560, 570, 151, 41))
        self.pushButton_7.setFont(font5)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_8 = QPushButton(self.page_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(560, 640, 151, 41))
        self.pushButton_8.setFont(font5)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_9 = QPushButton(self.page_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(560, 710, 151, 41))
        self.pushButton_9.setFont(font5)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.textEdit_26 = QTextEdit(self.page_3)
        self.textEdit_26.setObjectName(u"textEdit_26")
        self.textEdit_26.setGeometry(QRect(740, 500, 411, 61))
        self.textEdit_26.setFont(font8)
        self.textEdit_26.setFrameShape(QFrame.NoFrame)
        self.textEdit_26.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_20 = QTextEdit(self.page_3)
        self.textEdit_20.setObjectName(u"textEdit_20")
        self.textEdit_20.setGeometry(QRect(170, 570, 361, 181))
        self.textEdit_20.setFont(font3)
        self.textEdit_20.setStyleSheet(u"color: white;")
        self.pushButton_11 = QPushButton(self.page_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(560, 500, 151, 51))
        self.pushButton_11.setFont(font5)
        self.pushButton_11.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.textEdit_25 = QTextEdit(self.page_3)
        self.textEdit_25.setObjectName(u"textEdit_25")
        self.textEdit_25.setGeometry(QRect(170, 500, 361, 51))
        font11 = QFont()
        font11.setFamily(u"Century Gothic")
        font11.setPointSize(10)
        font11.setBold(True)
        font11.setWeight(75)
        self.textEdit_25.setFont(font11)
        self.textEdit_25.setStyleSheet(u"color: white;")
        self.textEdit_44 = QTextEdit(self.page_3)
        self.textEdit_44.setObjectName(u"textEdit_44")
        self.textEdit_44.setGeometry(QRect(740, 570, 361, 181))
        self.textEdit_44.setFont(font3)
        self.textEdit_44.setStyleSheet(u"color: white;")
        self.textEdit_44.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.checkBox_4 = QCheckBox(self.page_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(30, 620, 121, 31))
        self.checkBox_4.setFont(font8)
        self.checkBox_4.setStyleSheet(u"color: white")
        self.checkBox_7 = QCheckBox(self.page_3)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(30, 660, 121, 31))
        self.checkBox_7.setFont(font8)
        self.checkBox_7.setStyleSheet(u"color: white")
        self.pushButton_17 = QPushButton(self.page_3)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(20, 710, 121, 41))
        self.pushButton_17.setFont(font5)
        self.pushButton_17.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }\n"
"")
        self.pushButton_17.setInputMethodHints(Qt.ImhNone)
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 400, 691, 71))
        self.label_3.setPixmap(QPixmap(u"photo/ssc.png"))
        self.textBrowser_4 = QTextBrowser(self.page_3)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(10, 410, 91, 61))
        self.textBrowser_4.setFont(font8)
        self.textBrowser_4.setFrameShape(QFrame.NoFrame)
        self.textBrowser_4.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_28 = QTextEdit(self.page_3)
        self.textEdit_28.setObjectName(u"textEdit_28")
        self.textEdit_28.setGeometry(QRect(800, 400, 351, 101))
        self.textEdit_28.setFont(font8)
        self.textEdit_28.setFrameShape(QFrame.NoFrame)
        self.textEdit_28.setTextInteractionFlags(Qt.NoTextInteraction)
        self.stackedWidget.addWidget(self.page_3)
        self.textEdit_10.raise_()
        self.textEdit_23.raise_()
        self.line_7.raise_()
        self.textEdit_21.raise_()
        self.textEdit_24.raise_()
        self.line_8.raise_()
        self.textEdit_22.raise_()
        self.textBrowser_3.raise_()
        self.textEdit_27.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.textEdit_26.raise_()
        self.textEdit_20.raise_()
        self.pushButton_11.raise_()
        self.textEdit_25.raise_()
        self.textEdit_44.raise_()
        self.checkBox_4.raise_()
        self.checkBox_7.raise_()
        self.pushButton_17.raise_()
        self.label_3.raise_()
        self.textBrowser_4.raise_()
        self.textEdit_28.raise_()
        self.line_9.raise_()
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.textEdit_30 = QTextEdit(self.page)
        self.textEdit_30.setObjectName(u"textEdit_30")
        self.textEdit_30.setEnabled(True)
        self.textEdit_30.setGeometry(QRect(10, 0, 781, 71))
        sizePolicy2.setHeightForWidth(self.textEdit_30.sizePolicy().hasHeightForWidth())
        self.textEdit_30.setSizePolicy(sizePolicy2)
        self.textEdit_30.setMinimumSize(QSize(500, 30))
        self.textEdit_30.setMaximumSize(QSize(10000, 100))
        self.textEdit_30.setSizeIncrement(QSize(0, 0))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textEdit_30.setPalette(palette5)
        self.textEdit_30.setFont(font2)
        self.textEdit_30.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit_30.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEdit_30.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_30.setFrameShape(QFrame.NoFrame)
        self.textEdit_30.setFrameShadow(QFrame.Sunken)
        self.textEdit_30.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_30.setLineWrapColumnOrWidth(1)
        self.textEdit_30.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_15 = QFrame(self.page)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(10, 80, 1141, 20))
        self.line_15.setStyleSheet(u"")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)
        self.textEdit_31 = QTextEdit(self.page)
        self.textEdit_31.setObjectName(u"textEdit_31")
        self.textEdit_31.setGeometry(QRect(10, 100, 1141, 361))
        self.textEdit_31.setFont(font8)
        self.textEdit_31.setFrameShape(QFrame.NoFrame)
        self.textEdit_31.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 340, 541, 341))
        self.label_4.setPixmap(QPixmap(u"photo/My_project.png"))
        self.stackedWidget.addWidget(self.page)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.textEdit_38 = QTextEdit(self.page_6)
        self.textEdit_38.setObjectName(u"textEdit_38")
        self.textEdit_38.setEnabled(True)
        self.textEdit_38.setGeometry(QRect(10, 0, 911, 100))
        sizePolicy2.setHeightForWidth(self.textEdit_38.sizePolicy().hasHeightForWidth())
        self.textEdit_38.setSizePolicy(sizePolicy2)
        self.textEdit_38.setMinimumSize(QSize(500, 30))
        self.textEdit_38.setMaximumSize(QSize(10000, 100))
        self.textEdit_38.setSizeIncrement(QSize(0, 0))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textEdit_38.setPalette(palette6)
        self.textEdit_38.setFont(font2)
        self.textEdit_38.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit_38.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEdit_38.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_38.setFrameShape(QFrame.NoFrame)
        self.textEdit_38.setFrameShadow(QFrame.Sunken)
        self.textEdit_38.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_38.setLineWrapColumnOrWidth(1)
        self.textEdit_38.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_41 = QTextEdit(self.page_6)
        self.textEdit_41.setObjectName(u"textEdit_41")
        self.textEdit_41.setGeometry(QRect(10, 100, 1131, 691))
        self.textEdit_41.setFont(font3)
        self.textEdit_41.setFrameShape(QFrame.NoFrame)
        self.textEdit_41.setTextInteractionFlags(Qt.NoTextInteraction)
        self.line_14 = QFrame(self.page_6)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(10, 80, 1141, 16))
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.page_6)

        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440 \u0426\u0435\u0437\u0430\u0440\u044f", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440 \u0412\u0438\u0436\u0435\u043d\u0435\u0440\u0430", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043d\u043e\u0430\u043b\u0444\u0430\u0432\u0438\u0442\u043d\u044b\u0439", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0440\u043c\u0438\u043d\u044b", None))
        self.btn_page_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u0438\u0435", None))
        self.btn_page_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u0439", None))
        self.btn_page_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442 \u0430\u0432\u0442\u043e\u0440\u0430", None))
        self.textEdit_39.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:34pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412\u0432\u0435\u0434\u0435\u043d\u0438\u0435. \u041a\u0430\u043a \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438?</span></p></body></html>", None))
        self.textEdit_40.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0425\u043e\u0442\u0438\u0442\u0435 \u043d\u0430\u0447\u0430\u0442\u044c \u0438\u0437\u0443\u0447\u0430\u0442\u044c \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044e, \u0443\u0437\u043d\u0430\u0442\u044c, \u043a\u0430\u043a \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 \u0448\u0438\u0444\u0440\u044b, \u0438 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u043b\u0438 \u044d\u0442\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435? \u0412\u044b \u0434\u0432\u0438\u0433\u0430\u0435\u0442"
                        "\u0435\u0441\u044c \u0432 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u043c \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0438. \u041d\u0438\u0436\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0430 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f, \u043a\u0430\u043a \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0432 </span><span style=\" font-weight:600; color:#6a5acd;\">Cryptography for beginners</span><span style=\" color:#ffffff;\">, \u0447\u0442\u043e\u0431\u044b \u0443\u0447\u0435\u0431\u043d\u044b\u0439 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 \u0431\u044b\u043b \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u043f\u043e\u043b\u0435\u0437\u043d\u044b\u043c. \u041f\u0440\u0438\u044f\u0442\u043d\u043e\u0433\u043e \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u043d\u043e\u0432\u044b\u0445 \u0437\u043d\u0430\u043d\u0438\u0439!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-botto"
                        "m:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 5 \u0442\u0438\u043f\u043e\u0432 \u043a\u043d\u043e\u043f\u043e\u043a</span><span style=\" font-weight:600; color:#ffffff;\">:</span><span style=\" color:#ffffff;\"> &quot;\u043e\u0442\u0447\u0438\u0441\u0442\u0438\u0442\u044c&quot;, &quot;\u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043a\u043b\u044e\u0447\u0430&quot;, &quot;\u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;, &quot;\u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot; \u0438 &quot;\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c&quot;. \u041a\u0430\u0436\u0434\u0430\u044f \u043a"
                        "\u043d\u043e\u043f\u043a\u0430 \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442 \u0437\u0430 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u0443\u044e \u0444\u0443\u043d\u043a\u0446\u0438\u044e.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">1. </span><span style=\" color:#6a5acd;\">&quot;</span><span style=\" font-weight:600; color:#6a5acd;\">\u041e\u0442\u0447\u0438\u0441\u0442\u0438\u0442\u044c</span><span style=\" color:#6a5acd;\">&quot;</span><span style=\" color:#ffffff;\"> - \u043e\u0442\u0447\u0438\u0449\u0430\u0435\u0442 \u043f\u043e\u043b\u0435 \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">2. </span><span style=\" color:#6a5"
                        "acd;\">&quot;</span><span style=\" font-weight:600; color:#6a5acd;\">\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043a\u043b\u044e\u0447\u0430</span><span style=\" color:#6a5acd;\">&quot;</span><span style=\" color:#ffffff;\"> - \u0433\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u0442 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0439 \u043a\u043b\u044e\u0447: \u0447\u0438\u0441\u043b\u043e, \u0441\u043b\u043e\u0432\u043e \u0438\u043b\u0438 \u043d\u0430\u0431\u043e\u0440 \u0431\u0443\u043a\u0432, \u0432 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">3. </span><span style=\" color:#6a5acd;\">&quot;</span><span style=\" font-weight:600; color:#6a5acd;\">\u0417\u0430\u0448\u0438\u0444"
                        "\u0440\u043e\u0432\u0430\u0442\u044c</span><span style=\" color:#6a5acd;\">&quot;</span><span style=\" color:#ffffff;\"> - \u0448\u0438\u0444\u0440\u0443\u0435\u0442 \u0438\u0441\u0445\u043e\u0434\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u043e\u0433\u043e \u043a\u043b\u044e\u0447\u0430.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">4. </span><span style=\" color:#6a5acd;\">&quot;</span><span style=\" font-weight:600; color:#6a5acd;\">\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c</span><span style=\" color:#6a5acd;\">&quot;</span><span style=\" color:#ffffff;\"> - \u0434\u0435\u0448\u0438\u0444\u0440\u0443\u0435\u0442 \u0438\u0441\u0445\u043e\u0434\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0432\u0432\u0435\u0434\u0435"
                        "\u043d\u043d\u043e\u0433\u043e \u043a\u043b\u044e\u0447\u0430.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">5. </span><span style=\" color:#6a5acd;\">&quot;</span><span style=\" font-weight:600; color:#6a5acd;\">\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c</span><span style=\" color:#6a5acd;\">&quot;</span><span style=\" color:#ffffff;\"> - \u043a\u043e\u043f\u0438\u0440\u0443\u0435\u0442 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0438\u043b\u0438 \u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#6a5acd;\">\u0418\u041d\u0421\u0422\u0420\u0423\u041a\u0426\u0418\u042f</span><span style=\" color:#ffffff;\"> (\u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u0432 </span><span style=\" font-weight:600; color:#6a5acd;\">Cryptography for beginners</span><span style=\" color:#ffffff;\">):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">1. \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044f\u0437\u044b\u043a \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">2. \u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447, \u0437\u0430\u0442\u0435\u043c \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043e\u043e"
                        "\u0431\u0449\u0435\u043d\u0438\u0435, \u0442\u0435\u043a\u0441\u0442 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">3. \u041d\u0430\u0436\u043c\u0438\u0442\u0435 &quot;\u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">4. \u041f\u0440\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438 \u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442, \u043d\u0430\u0436\u0430\u0432 \u043d\u0430 \u043a\u043d"
                        "\u043e\u043f\u043a\u0443 &quot;\u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">5. \u0414\u043b\u044f \u043b\u0443\u0447\u0448\u0435\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0447\u0442\u043e-\u043d\u0438\u0431\u0443\u0434\u044c \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0430 \u043b\u0438\u0441\u0442\u043e\u0447\u043a\u0435, \u0441\u0432\u0435\u0440\u044f\u044f\u0441\u044c \u0441 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043e\u0439: \u0442\u0430\u043a \u0432\u044b \u0431\u044b\u0441\u0442\u0440\u0435\u0435 \u0443\u0441\u0432\u043e\u0438\u0442\u0435 \u0438\u0434\u0435\u044e \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u0430\u043b"
                        "\u0433\u043e\u0440\u0438\u0442\u043c\u0430!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0414\u043b\u044f \u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432\u0432\u043e\u0434\u0438\u0442\u0435 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0438 \u043d\u0430\u0436\u0438\u043c\u0430\u0435\u0442\u0435 &quot;\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#6a5acd;\">!!!  \u041e\u0411\u0420\u0410\u0422\u0418\u0422\u0415 \u0412\u041d\u0418\u041c\u0410\u041d\u0418\u0415  !!!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0415\u0441\u043b\u0438 \u0432\u044b \u043f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u0435 \u0434\u043b\u044f \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043e\u0434\u0438\u043d \u044f\u0437\u044b\u043a, \u043d\u043e \u0432\u0432\u0435\u0434\u0435\u0442\u0435 \u0441\u043e\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043d\u0430 \u0434\u0440\u0443\u0433\u043e\u043c, \u0442\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043d\u0435 \u0437\u0430\u0448\u0438\u0444\u0440\u0443\u0435\u0442 \u0435\u0433\u043e \u0438 \u0432\u044b\u0432\u0435\u0434\u0435\u0442 \u0431\u0435\u0437 \u0438\u0437\u043c\u0435"
                        "\u043d\u0435\u043d\u0438\u0439. \u0411\u0443\u0434\u044c\u0442\u0435 \u0432\u043d\u0438\u043c\u0430\u0442\u0435\u043b\u044c\u043d\u044b \u043f\u0440\u0438 \u0432\u0432\u043e\u0434\u0435 \u0434\u0430\u043d\u043d\u044b\u0445.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">*\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432\u0441\u0435\u0445 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u0442\u0435\u0440\u043c\u0438\u043d\u043e\u0432 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0443\u0437\u043d\u0430\u0442\u044c \u0432\u043e \u0432\u043a\u043b\u0430\u0434\u043a\u0435 </span><span style=\" color:#6a5acd;\""
                        ">&quot;\u0422\u0435\u0440\u043c\u0438\u043d\u044b&quot;</span><span style=\" color:#ffffff;\">.</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:34pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#ffffff;\">\u0428\u0438\u0444\u0440 \u0426\u0435\u0437\u0430\u0440\u044f</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">\u0421\u0442\u043e\u0438\u0442 \u0437\u0430\u043c\u0435\u0442\u0438\u0442\u044c, \u0447\u0442\u043e \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u043f\u043e\u044f\u0432\u0438\u043b\u0430\u0441\u044c \u0435\u0449\u0435 \u0437\u0430\u0434\u043e\u043b\u0433\u043e \u0434\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043e\u0432. \u041f\u0435\u0440\u0432\u044b\u0435 \u00ab\u0448\u0438\u0444\u0440\u044b\u00bb"
                        " \u043d\u0430\u0447\u0430\u043b\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f \u0435\u0449\u0435 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0442\u044b\u0441\u044f\u0447 \u043b\u0435\u0442 \u043d\u0430\u0437\u0430\u0434 \u0432 \u0432\u0438\u0434\u0435 \u0442\u0430\u0439\u043d\u043e\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0438\u0435\u0440\u043e\u0433\u043b\u0438\u0444\u043e\u0432. \u041d\u043e \u043d\u0430\u0438\u0431\u043e\u043b\u0435\u0435 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u043c \u0441\u043f\u043e\u0441\u043e\u0431\u043e\u043c \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0438\u0437 \u0434\u0440\u0435\u0432\u043d\u043e\u0441\u0442\u0438 \u0441\u0442\u0430\u043b \u0448\u0438\u0444\u0440 \u0426\u0435\u0437\u0430\u0440\u044f. </span></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">\u0428\u0438\u0444\u0440 \u0426\u0435\u0437\u0430\u0440\u044f \u043e\u0441\u043d\u043e\u0432\u0430\u043d \u043d\u0430 \u0437\u0430\u043c\u0435\u043d\u0435 \u043e\u0434\u043d\u043e\u0439 \u0431\u0443\u043a\u0432\u044b \u0434\u0440\u0443\u0433\u043e\u0439 \u043f\u043e\u0441\u043b\u0435 \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u0432\u0441\u0435\u0433\u043e \u0430\u043b\u0444\u0430\u0432\u0438"
                        "\u0442\u0430 \u043d\u0430 \u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u043f\u043e\u0437\u0438\u0446\u0438\u0439. \u042e\u043b\u0438\u0439 \u0426\u0435\u0437\u0430\u0440\u044c \u0437\u0430\u043c\u0435\u043d\u044f\u043b \u0431\u0443\u043a\u0432\u044b \u0432 \u0441\u0432\u043e\u0438\u0445 \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0445 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f\u0445 \u043f\u0443\u0442\u0435\u043c \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0430 \u043d\u0430 \u0442\u0440\u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0438 \u0438 \u043f\u043e\u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0439 \u0437\u0430\u043c\u0435\u043d\u044b \u043a\u0430\u0436\u0434\u043e\u0439 \u0431\u0443\u043a\u0432\u044b \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0439 \u0431\u0443\u043a\u0432\u043e\u0439 \u0438\u0437 \u0441\u043c\u0435\u0449\u0435\u043d\u043d\u043e\u0433"
                        "\u043e \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0430. \u0428\u0438\u0444\u0440 \u0426\u0435\u0437\u0430\u0440\u044f \u043c\u043e\u0436\u043d\u043e \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u0446\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u0430\u043a \u0448\u0438\u0444\u0440 \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438, \u043f\u0440\u0438 \u0431\u043e\u043b\u0435\u0435 \u0443\u0437\u043a\u043e\u0439 \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438 \u2014 \u0448\u0438\u0444\u0440 \u043f\u0440\u043e\u0441\u0442\u043e\u0439 \u0437\u0430\u043c\u0435\u043d\u044b. \u0412 \u0448\u0438\u0444\u0440\u0435 \u0426\u0435\u0437\u0430\u0440\u044f  \u043a\u043b\u044e\u0447\u043e\u043c \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u043c\u044b \u0441\u043c\u0435\u0449\u0430\u0435\u043c \u0430\u043b"
                        "\u0444\u0430\u0432\u0438\u0442. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u043a\u043b\u044e\u0447 - </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00ab2\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, \u0442\u043e \u0432 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u0439 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0435 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00ab\u0410\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\"> \u0431\u0443\u0434\u0435\u0442 \u043c\u0435\u043d\u044f\u0442\u044c\u0441\u044f \u043d\u0430 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00ab\u0421\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00ab\u0421\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\"> \u0431\u0443\u0434\u0435\u0442 \u043c\u0435\u043d\u044f\u0442\u044c\u0441\u044f \u043d\u0430 </span><span style=\" font-size:12pt; color:#6a5acd;\">"
                        "\u00abE\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abE\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\"> \u0431\u0443\u0434\u0435\u0442 \u043c\u0435\u043d\u044f\u0442\u044c\u0441\u044f \u043d\u0430 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abG\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\"> \u0438 \u0442\u0430\u043a \u0434\u0430\u043b\u0435\u0435. \u0410\u043b\u0444\u0430\u0432\u0438\u0442 \u0441\u043b\u043e\u0432\u043d\u043e \u0437\u0430\u043c\u043a\u043d\u0443\u0442\u044b\u0439 \u043a\u0440\u0443\u0433: \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u0431\u0443\u0434\u0443\u0442 \u043c\u0435\u043d\u044f\u0442\u044c\u0441\u044f \u043d\u0430 \u043f\u0435\u0440\u0432\u044b\u0435. \u041f\u043e\u044d\u0442\u043e\u043c\u0443 \u043a\u043b\u044e\u0447\u0438, \u0434\u043b\u0438\u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043f\u0440\u0435"
                        "\u0432\u044b\u0448\u0430\u0435\u0442 \u0434\u043b\u0438\u043d\u0443 \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0430, \u043d\u0435 \u0438\u043c\u0435\u044e\u0442 \u0441\u043c\u044b\u0441\u043b\u0430. \u0422\u0430\u043a, \u043f\u0440\u0438 \u043a\u043b\u044e\u0447\u0435 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00ab2\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abZ\u00bb </span><span style=\" font-size:12pt; color:#ffffff;\">\u043f\u0440\u043e\u0441\u0442\u043e \u043f\u043e\u043c\u0435\u043d\u044f\u0435\u0442\u0441\u044f \u043d\u0430</span><span style=\" font-size:12pt; color:#6a5acd;\"> \u00abB\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">. \u0414\u043b\u044f \u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0432\u044b\u0447\u0438\u0442\u0430\u043d\u0438\u0435 \u043a\u044e"
                        "\u0447\u0430 \u0438\u0437 \u0438\u043d\u0434\u0435\u043a\u0441\u0430 \u0431\u0443\u043a\u0432\u044b \u0448\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442\u0430. \u0412\u0430\u0436\u043d\u043e \u0443\u0442\u043e\u0447\u043d\u0438\u0442\u044c, \u0447\u0442\u043e \u0443 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u0433\u043e \u0438 \u0440\u0443\u0441\u0441\u043a\u043e\u0433\u043e \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u043e\u0432 \u0440\u0430\u0437\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432: </span><span style=\" font-size:12pt; color:#6a5acd;\">26</span><span style=\" font-size:12pt; color:#ffffff;\"> \u0438 </span><span style=\" font-size:12pt; color:#6a5acd;\">33</span><span style=\" font-size:12pt; color:#ffffff;\">. \u0410 \u0447\u0442\u043e\u0431\u044b \u0448\u0438\u0444\u0440 \u0431\u044b\u043b \u0431\u043e\u043b\u0435\u0435 \u0443\u0441\u0442\u043e\u0439\u0447\u0438\u0432\u044b\u043c, \u0430\u043b\u0444"
                        "\u0430\u0432\u0438\u0442\u044b, \u0441\u043e\u0441\u0442\u043e\u044f\u0449\u0438\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0438\u0437 \u0437\u0430\u0433\u043b\u0430\u0432\u043d\u044b\u0445 \u0431\u0443\u043a\u0432, \u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u044b \u0437\u0430 \u0441\u0447\u0435\u0442 \u043f\u0440\u043e\u043f\u0438\u0441\u043d\u044b\u0445 \u0431\u0443\u043a\u0432, \u0446\u0438\u0444\u0440, \u0437\u043d\u0430\u043a\u043e\u0432 \u043f\u0440\u0435\u043f\u0438\u043d\u0430\u043d\u0438\u044f \u0438 \u043f\u0440\u043e\u0431\u0435\u043b\u0430.  \u041f\u0440\u0438\u043c\u0435\u0440 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u0433\u043e \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0430: </span><span style=\" font-size:12pt; color:#6a5acd;\">ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,</span></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#747474;\">\u0418\u0441\u0442\u043e\u0440\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u043f\u0440\u0430\u0432\u043a\u0430</span></p></body></html>", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#747474;\">\u041a\u0430\u043a \u044d\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442?</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447: </span></p></body></html>", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u041f\u0435\u0440\u0435\u0434 \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0435\u0439 \u043a\u043b\u044e\u0447\u0430 \u043d\u0435 \u0437\u0430\u0431\u0443\u0434\u044c\u0442\u0435 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u044f\u0437\u044b\u043a \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f!</span></p></body></html>", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442:</span></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043a\u043b\u044e\u0447\u0430", None))
        self.label_2.setText("")
        self.textEdit_37.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:34pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#ffffff;\">\u0428\u0438\u0444\u0440 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438</span></p></body></html>", None))
        self.textEdit_51.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#747474;\">\u0418\u0441\u0442\u043e\u0440\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u043f\u0440\u0430\u0432\u043a\u0430</span></p></body></html>", None))
        self.textEdit_49.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">&quot;\u0422\u043e\u0447\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u0448\u0438\u0444\u0440\u0430 \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0435 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u043e. \u0412\u043f\u043e\u043b\u043d\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e, \u0447\u0442\u043e \u043f\u0438\u0441\u0446\u044b \u0432 \u0434\u0440\u0435\u0432\u043d\u043e\u0441\u0442\u0438 \u043f"
                        "\u0435\u0440\u0435\u0441\u0442\u0430\u0432\u043b\u044f\u043b\u0438 \u0431\u0443\u043a\u0432\u044b \u0432 \u0438\u043c\u0435\u043d\u0438 \u0441\u0432\u043e\u0435\u0433\u043e \u0446\u0430\u0440\u044f \u0440\u0430\u0434\u0438 \u0442\u043e\u0433\u043e, \u0447\u0442\u043e\u0431\u044b \u0441\u043a\u0440\u044b\u0442\u044c \u0435\u0433\u043e \u043f\u043e\u0434\u043b\u0438\u043d\u043d\u043e\u0435 \u0438\u043c\u044f \u0438\u043b\u0438 \u0432 \u0440\u0438\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0445 \u0446\u0435\u043b\u044f\u0445 &quot; </span><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">- \u0424\u0440\u0435\u0434 \u0411. \u0420\u0438\u043a\u0441\u043e\u043d. </span></p></body></html>", None))
        self.textEdit_52.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#747474;\">\u041a\u0430\u043a \u044d\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442?</span></p></body></html>", None))
        self.textEdit_50.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">\u0415\u0441\u043b\u0438 \u0432 \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u043e\u043c \u0448\u0438\u0444\u0440\u0435 \u043e\u0434\u043d\u0438 \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u0437\u0430\u043c\u0435\u043d\u044f\u044e\u0442\u0441\u044f \u0434\u0440\u0443\u0433\u0438\u043c\u0438, \u0442\u043e \u0432 \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u043e\u043c \u0448\u0438\u0444\u0440\u0435 \u0441\u0438\u043c\u0432\u043e\u043b"
                        "\u044b \u043e\u0441\u0442\u0430\u044e\u0442\u0441\u044f \u0442\u0435\u043c\u0438 \u0436\u0435, \u043d\u043e \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0442\u0430\u043a, \u0447\u0442\u043e\u0431\u044b \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0431\u044b\u043b\u043e \u043d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u043f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c. \u041f\u043e\u0441\u043a\u043e\u043b\u044c\u043a\u0443 \u043a\u0430\u0436\u0434\u044b\u0439 \u043a\u043b\u044e\u0447 \u0441\u043e\u0437\u0434\u0430\u0435\u0442 \u0441\u0432\u043e\u0439 \u0441\u043f\u043e\u0441\u043e\u0431 \u0443\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0435\u043d\u0438\u044f, \u0438\u043b\u0438 \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438, \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432, \u043a\u0440\u0438\u043f\u0442\u043e\u0430\u043d\u0430\u043b\u0438\u0442\u0438\u043a \u043d\u0435 \u0437\u043d\u0430\u0435\u0442, \u043a\u0430\u043a"
                        " \u043d\u0443\u0436\u043d\u043e \u043f\u0435\u0440\u0435\u0443\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0442\u044c </span><span style=\" font-size:12pt; font-style:italic; color:#6a5acd;\">\u0448\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442</span><span style=\" font-size:12pt; color:#ffffff;\">, \u0447\u0442\u043e\u0431\u044b \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435. \u0427\u0442\u043e\u0431\u044b \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435, \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u043f\u0438\u0448\u0435\u0442\u0441\u044f \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e \u0432 \u0441\u0442\u0440\u043e\u043a\u0438 \u043d\u0430 \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0435 \u043a\u043e"
                        "\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432, \u0430 \u0448\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442 \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u043f\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430\u043c \u0441\u0432\u0435\u0440\u0445\u0443 \u0432\u043d\u0438\u0437. \u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0435 \u043a\u043b\u044e\u0447\u043e\u043c \u0431\u0443\u0434\u0435\u0442 \u044f\u0432\u043b\u044f\u0442\u044c\u0441\u044f \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 \u0432 \u043e\u0434\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435 (\u0448\u0438\u0440\u0438\u043d\u0430 \u043f\u043e\u043b\u0443\u0447\u0438\u0432\u0448\u0435\u0439\u0441\u044f \u0442\u0430\u0431\u043b\u0438\u0447\u043a\u0438). \u0414\u043b\u044f  \u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043d\u0435"
                        "\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0432\u0441\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043d\u0430\u043e\u0431\u043e\u0440\u043e\u0442: \u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0448\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442 \u043f\u043e \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u0438 \u0438 \u0441\u0447\u0438\u0442\u0430\u0442\u044c \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0440\u043e\u0447\u043d\u043e. \u0427\u0435\u043c \u0431\u043e\u043b\u044c\u0448\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432, \u0442\u0435\u043c \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u0439 \u0448\u0438\u0444\u0440 \u0442\u0440\u0443\u0434\u043d\u0435\u0435 \u043f\u043e\u0434\u0434\u0430\u0435\u0442\u0441\u044f \u0432\u0437\u043b\u043e\u043c\u0443 \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0433\u0440\u0443\u0431"
                        "\u043e\u0439 \u0441\u0438\u043b\u044b, \u043f\u043e\u0441\u043a\u043e\u043b\u044c\u043a\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u043a\u043b\u044e\u0447\u0435\u0439 \u0437\u0430\u0432\u0438\u0441\u0438\u0442 \u043e\u0442 \u0434\u043b\u0438\u043d\u044b \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f. \u0427\u0442\u043e\u0431\u044b \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435, \u043a\u043b\u044e\u0447 \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 1 \u0438 \u043c\u0435\u043d\u044c\u0448\u0435 \u0434\u043b\u0438\u043d\u044b \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430.</span></p></body></html>", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.textEdit_54.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442:</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447: </span></p></body></html>", None))
        self.textEdit_29.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.textEdit_45.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_46.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0427\u0442\u043e\u0431\u044b \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u043b\u044e\u0447 \u0434\u043b\u044f \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u043e\u0433\u043e \u0448\u0438\u0444\u0440\u0430, \u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0442\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f</s"
                        "pan></p></body></html>", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043a\u043b\u044e\u0447\u0430", None))
        self.label.setText("")
        self.textEdit_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:34pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#ffffff;\">\u0428\u0438\u0444\u0440 \u0412\u0438\u0436\u0435\u043d\u0435\u0440\u0430</span></p></body></html>", None))
        self.textEdit_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#747474;\">\u0418\u0441\u0442\u043e\u0440\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u043f\u0440\u0430\u0432\u043a\u0430</span></p></body></html>", None))
        self.textEdit_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">\u0428\u0438\u0444\u0440 \u0412\u0438\u0436\u0435\u043d\u0435\u0440\u0430 \u0431\u044b\u043b \u0432\u043f\u0435\u0440\u0432\u044b\u0435 \u043e\u043f\u0438\u0441\u0430\u043d \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0438\u043c \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u043e\u043c \u0414\u0436\u043e\u0432\u0430\u043d\u0438 \u0411\u0430\u0442\u0442\u0438\u0441\u0442\u0430 \u0411\u0435\u043b\u043b\u0430\u0441\u043e \u0432 1553 \u0433\u043e\u0434\u0443, \u043e\u0434"
                        "\u043d\u0430\u043a\u043e \u043f\u043e\u043b\u0443\u0447\u0438\u043b \u0438\u043c\u044f \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u043e\u0433\u043e \u0434\u0438\u043f\u043b\u043e\u043c\u0430\u0442\u0430 \u0411\u043b\u0435\u0437\u0430 \u0434\u0435 \u0412\u0438\u0436\u0435\u043d\u0435\u0440\u0430, \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u0437 \u043c\u043d\u043e\u0433\u0438\u0445 \u043b\u044e\u0434\u0435\u0439, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u043e\u0432\u0442\u043e\u0440\u043d\u043e \u0438\u0437\u043e\u0431\u0440\u0435\u0442\u0430\u043b\u0438 \u044d\u0442\u043e\u0442 \u0448\u0438\u0444\u0440 \u0432 \u043f\u043e\u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 \u0433\u043e\u0434\u044b</span></p></body></html>", None))
        self.textEdit_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#747474;\">\u041a\u0430\u043a \u044d\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442?</span></p></body></html>", None))
        self.textEdit_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">\u0412 \u043e\u0442\u043b\u0438\u0447\u0438\u0435 \u043e\u0442 \u0448\u0438\u0444\u0440\u0430 \u0426\u0435\u0437\u0430\u0440\u044f \u0448\u0438\u0444\u0440 \u0412\u0438\u0436\u0435\u043d\u0435\u0440\u0430 \u043e\u0431\u0440\u0430\u0437\u0443\u0435\u0442\u0441\u044f \u0446\u0435\u043f\u043e\u0447\u043a\u043e\u0439 \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u043a. \u041f\u043e\u0441\u043a\u043e\u043b\u044c\u043a\u0443 \u0432 \u043d\u0435\u043c \u0438\u0441\u043f\u043e\u043b\u044c"
                        "\u0437\u0443\u0435\u0442\u0441\u044f \u0431\u043e\u043b\u0435\u0435 \u043e\u0434\u043d\u043e\u0433\u043e \u043d\u0430\u0431\u043e\u0440\u0430 \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u043a, \u0435\u0433\u043e \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0442 \u043f\u043e\u043b\u0438\u0430\u043b\u0444\u0430\u0432\u0438\u0442\u043d\u044b\u043c \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u043c \u0448\u0438\u0444\u0440\u043e\u043c. \u0412\u043c\u0435\u0441\u0442\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u043e\u0433\u043e \u043a\u043b\u044e\u0447\u0430, \u043a\u0430\u043a \u0432 \u0448\u0438\u0444\u0440\u0435 \u0426\u0435\u0437\u0430\u0440\u044f, \u0432 \u0448\u0438\u0444\u0440\u0435 \u0412\u0438\u0436\u0435\u043d\u0435\u0440\u0430 \u043f\u0440\u0438\u043c\u0435\u043d\u044f\u0435\u0442\u0441\u044f \u0431\u0443\u043a\u0432\u0435\u043d\u043d\u044b\u0439 \u043a\u043b\u044e\u0447. \u041a\u043b\u044e\u0447 \u0448\u0438\u0444\u0440\u0430 \u0412\u0438\u0436\u0435\u043d"
                        "\u0435\u0440\u0430 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0441\u043e\u0431\u043e\u0439 \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0431\u0443\u043a\u0432 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u0435 \u0441\u043b\u043e\u0432\u043e), \u0440\u0430\u0437\u0431\u0438\u0432\u0430\u0435\u043c\u0443\u044e \u043d\u0430 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0432\u0441\u043f\u043e\u043c\u043e\u0433\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043e\u0434\u043d\u043e\u0431\u0443\u043a\u0432\u0435\u043d\u043d\u044b\u0445 \u043a\u043b\u044e\u0447\u0435\u0439 (</span><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">\u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u0439</span><span style=\" font-size:12pt; color:#ffffff;\">), \u043a\u043e\u0442\u043e\u0440\u044b\u043c\u0438 \u0448\u0438\u0444\u0440\u0443\u044e\u0442\u0441"
                        "\u044f \u0431\u0443\u043a\u0432\u044b \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0435\u0441\u043b\u0438 \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043a\u043b\u044e\u0447\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043e \u0441\u043b\u043e\u0432\u043e </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abQWERTY\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, \u0442\u043e \u043f\u0435\u0440\u0432\u044b\u043c \u043a\u043b\u044e\u0447\u043e\u043c \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abQ\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, \u0432\u0442\u043e\u0440\u044b\u043c \u2013 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abW\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, \u0442\u0440\u0435\u0442\u044c\u0438\u043c \u2013 </span><span style=\" font-size:12pt; color:#6a5"
                        "acd;\">\u00abE\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, \u0447\u0435\u0442\u0432\u0435\u0440\u0442\u044b\u043c \u2013 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abR\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, \u043f\u044f\u0442\u044b\u043c \u2013 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abT\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, \u0448\u0435\u0441\u0442\u044b\u043c \u2013 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abY\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">. \u041f\u0435\u0440\u0432\u044b\u043c \u043a\u043b\u044e\u0447\u043e\u043c \u0448\u0438\u0444\u0440\u0443\u0435\u0442\u0441\u044f \u043f\u0435\u0440\u0432\u0430\u044f \u0431\u0443\u043a\u0432\u0430 \u0441\u043b\u043e\u0432\u0430 \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430, \u0432\u0442\u043e\u0440\u044b\u043c \u2013 \u0432\u0442\u043e\u0440\u0430\u044f \u0431\u0443\u043a\u0432\u0430"
                        " \u0438 \u0442.\u0434. \u041a\u043e\u0433\u0434\u0430 \u043c\u044b \u0434\u043e\u0445\u043e\u0434\u0438\u043c \u0434\u043e \u0441\u0435\u0434\u044c\u043c\u043e\u0439 \u0431\u0443\u043a\u0432\u044b \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430, \u043c\u044b \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u043c\u0441\u044f \u043a \u043f\u0435\u0440\u0432\u043e\u043c\u0443 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0443. \u041a\u0430\u0436\u0434\u044b\u0439 \u043f\u043e\u0434\u043a\u043b\u044e\u0447 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u0443\u0435\u0442\u0441\u044f \u0432 \u0446\u0435\u043b\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u0438 \u0441\u043b\u0443\u0436\u0438\u0442 \u043a\u043b\u044e\u0447\u043e\u043c \u0448\u0438\u0444\u0440\u0430 \u0426\u0435\u0437\u0430\u0440\u044f. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0431\u0443\u043a\u0432\u0435 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00ab\u0410\u00bb</span><span styl"
                        "e=\" font-size:12pt; color:#ffffff;\"> \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043a\u043b\u044e\u0447 0 \u0448\u0438\u0444\u0440\u0430 \u0426\u0435\u0437\u0430\u0440\u044f, \u0431\u0443\u043a\u0432\u0435 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00ab\u0412\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\"> - \u043a\u043b\u044e\u0447 1 \u0438 \u0442\u0430\u043a \u0434\u0430\u043b\u0435\u0435 \u0432\u043f\u043b\u043e\u0442\u044c \u0434\u043e \u0431\u0443\u043a\u0432\u044b </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abZ\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">, \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043a\u043b\u044e\u0447 25. \u0427\u0442\u043e\u0431\u044b \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u0438\u043c\u0432\u043e\u043b \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0441\u043b"
                        "\u043e\u0436\u0438\u0442\u044c </span><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">\u0438\u043d\u0434\u0435\u043a\u0441</span><span style=\" font-size:12pt; color:#ffffff;\"> (\u043f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0431\u0443\u043a\u0432\u044b \u0432 \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0435, \u043d\u0430\u0447\u0438\u043d\u0430\u044f \u0441 0) \u0431\u0443\u043a\u0432\u044b \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430 \u0441 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u043e\u043c. \u0421\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e, \u0434\u043b\u044f </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abN\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\"> \u0431\u0443\u0434\u0435\u0442 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abQ\u00bb</span><span style=\" fon"
                        "t-size:12pt; color:#ffffff;\">, \u0434\u043b\u044f </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00ab\u041e\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\"> - </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abW\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\"> \u0438 \u0442\u0430\u043a \u0434\u0430\u043b\u0435\u0435. \u0422\u0430\u043a\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abNOBODY LIKES MONDAY MORNING\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\"> \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043e \u0432 </span><span style=\" font-size:12pt; color:#6a5acd;\">\u00abDKFFWW BEOVL KEJERR KENRZGE\u00bb</span><span style=\" font-size:12pt; color:#ffffff;\">. \u0414\u043b\u044f \u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043d\u0435\u043e\u0431\u0445\u043e"
                        "\u0434\u0438\u043c\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0432\u044b\u0447\u0438\u0442\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u043a\u044e\u0447\u0430 \u0438\u0437 \u0438\u043d\u0434\u0435\u043a\u0441\u0430 \u0431\u0443\u043a\u0432\u044b \u0448\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442\u0430.</span></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u041b\u044e\u0431\u043e\u0435 \u0441\u043b\u043e\u0432\u043e</span></p></body></html>", None))
        self.textEdit_19.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442:</span></p></body></html>", None))
        self.textEdit_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_18.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u041d\u0435 \u0437\u0430\u0431\u0443\u0434\u044c\u0442\u0435 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u044f\u0437\u044b\u043a \u043f\u0435\u0440\u0435\u0434 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435\u043c!</span></p></body></html>", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.textEdit_17.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043a\u043b\u044e\u0447\u0430", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:34pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u041f\u0440\u043e\u0441\u0442\u043e\u0439 \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u0439 \u0448\u0438\u0444\u0440</span></p></body></html>", None))
        self.textEdit_23.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#747474;\">\u0418\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u044b\u0435 \u0444\u0430\u043a\u0442\u044b</span></p></body></html>", None))
        self.textEdit_21.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u041f\u0440\u043e\u0441\u0442\u043e\u0439 \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u0439 \u0448\u0438\u0444\u0440 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043e\u0434\u043d\u0438\u043c \u0438\u0437 \u0442\u0435\u0445 \u0448\u0438\u0444\u0440\u043e\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0441\u043f\u043e\u0441\u043e\u0431\u043d\u044b \u0430\u043a\u0442\u0438\u0432\u043d\u043e \u043f\u0440\u043e\u0442\u0438\u0432\u043e\u0441\u0442\u043e\u044f\u0442\u044c"
                        " \u0430\u0442\u0430\u043a\u0430\u043c \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0433\u0440\u0443\u0431\u043e\u0439 \u0441\u0438\u043b\u044b, \u043f\u043e\u0441\u043a\u043e\u043b\u044c\u043a\u0443 \u043e\u043d \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0437\u0443\u0435\u0442\u0441\u044f \u043d\u0435\u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e \u0431\u043e\u043b\u044c\u0448\u0438\u043c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e\u043c \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u043a\u043b\u044e\u0447\u0435\u0439. \u041f\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u0430\u043c \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0442\u043e\u0440\u0438\u043a\u0438, \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u043a\u043b\u044e\u0447\u0435\u0439, \u0441\u043e\u0441\u0442\u043e\u044f\u0449\u0438\u0445 \u0442\u043e\u043b\u044c\u043a\u043e \u0438\u0437 \u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u0445 \u0431"
                        "\u0443\u043a\u0432, \u0431\u0443\u0434\u0435\u0442 \u0440\u0430\u0432\u043d\u043e \u0444\u0430\u043a\u0442\u043e\u0440\u0438\u0430\u043b\u0443 26 (\u044d\u0442\u043e 403 291 461 126 605 635 584 000 000). \u0414\u0430\u0436\u0435 \u0435\u0441\u043b\u0438 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440 \u043c\u043e\u0433 \u0435\u0436\u0435\u0441\u0435\u043a\u0443\u043d\u0434\u043d\u043e \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c \u0442\u0440\u0438\u043b\u043b\u0438\u043e\u043d \u043a\u043b\u044e\u0447\u0435\u0439, \u0434\u043b\u044f \u043f\u0435\u0440\u0435\u0431\u043e\u0440\u0430 \u0432\u0441\u0435\u0445 \u043a\u043b\u044e\u0447\u0435\u0439 \u0435\u043c\u0443 \u043f\u043e\u043d\u0430\u0434\u043e\u0431\u0438\u043b\u043e\u0441\u044c \u0431\u044b 12 \u043c\u0438\u043b\u043b\u0438\u043e\u043d\u043e\u0432 \u043b\u0435\u0442.</span></p></body></html>", None))
        self.textEdit_24.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#747474;\">\u041a\u0430\u043a \u044d\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442?</span></p></body></html>", None))
        self.textEdit_22.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 4 \u0442\u0438\u043f\u0430 \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u0445 \u0448\u0438\u0444\u0440\u043e\u0432: \u043e\u043c\u043e\u0444\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439, \u043f\u043e\u043b\u0438\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439, \u043f\u043e\u043b\u0438\u0430\u043b\u0444\u0430\u0432\u0438\u0442\u043d\u044b\u0439 \u0438 \u043f\u0440\u043e\u0441\u0442\u043e\u0439"
                        " \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u0439 \u0448\u0438\u0444\u0440. \u041c\u044b \u0440\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0438\u043c \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439. \u0412 \u043e\u0442\u043b\u0438\u0447\u0438\u0435 \u043e\u0442 \u0428\u0438\u0444\u0440\u0430 \u0426\u0435\u0437\u0430\u0440\u044f, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u043d\u0438\u0436\u043d\u0438\u0439 \u0440\u044f\u0434 \u0441\u0434\u0432\u0438\u043d\u0443\u0442, \u043d\u043e \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0435\u0442 \u043f\u0440\u0435\u0436\u043d\u0438\u0439 \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u043d\u044b\u0439 \u043f\u043e\u0440\u044f\u0434\u043a\u043e\u043a, \u0432 \u0434\u0430\u043d\u043d\u043e\u043c \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0435 \u043d\u0438\u0436\u043d\u0438\u0439 \u0440\u044f\u0434 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u043f\u0435\u0440\u0435\u043c\u0435\u0448\u0430\u043d. \u041f\u0440\u043e"
                        "\u0441\u0442\u043e\u0439 \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u0439 \u0448\u0438\u0444\u0440, \u0438\u043b\u0438 \u043c\u043e\u043d\u043e\u0430\u043b\u0444\u0430\u0432\u0438\u0442\u043d\u044b\u0439 \u0448\u0438\u0444\u0440, - \u044d\u0442\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0437\u0430\u043c\u0435\u043d\u044f\u0435\u0442 \u043a\u0430\u0436\u0434\u044b\u0439 \u0441\u0438\u043c\u0432\u043e\u043b \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u043c \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u043c \u0448\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442\u0430. \u041a\u043b\u044e\u0447\u043e\u043c \u0432 \u0442\u0430\u043a\u043e\u043c \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0435 \u0431\u0443\u0434\u0435\u0442 \u044f\u0432\u043b\u044f\u0442\u044c\u0441\u044f \u0446\u0435"
                        "\u043b\u044b\u0439 \u0430\u043b\u0444\u0430\u0432\u0438\u0442, \u043d\u043e \u0441 \u043f\u0435\u0440\u0435\u043c\u0435\u0448\u0430\u043d\u043d\u044b\u043c\u0438 \u0431\u0443\u043a\u0432\u0430\u043c\u0438. \u0425\u043e\u0442\u044c \u041f\u0440\u043e\u0441\u0442\u043e\u0439 \u041f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u0439 \u0448\u0438\u0444\u0440 \u0438 \u043e\u0431\u043b\u0430\u0434\u0430\u0435\u0442 \u0431\u043e\u043b\u044c\u0448\u0438\u043c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e\u043c \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u043a\u043b\u044e\u0447\u0435\u0439, \u043e\u043d \u043d\u0435 \u0441\u043c\u043e\u0436\u0435\u0442 \u043f\u0440\u043e\u0442\u0438\u0432\u043e\u0441\u0442\u043e\u044f\u0442\u044c </span><span style=\" font-size:12pt; font-style:italic; color:#6a5acd;\">\u0447\u0430\u0441\u0442\u043e\u0442\u043d\u043e\u043c\u0443 \u0430\u043d\u0430\u043b\u0438\u0437\u0443</span><span style=\" font-size:12pt; color:#ffffff;\"> (\u0441"
                        "\u043c\u043e\u0442\u0440\u0438 \u0432\u043a\u043b\u0430\u0434\u043a\u0443 &quot;\u0422\u0435\u0440\u043c\u0438\u043d\u044b&quot;!), \u0432\u0435\u0434\u044c \u0431\u0443\u043a\u0432\u044b \u0448\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442\u0430 \u0431\u0443\u0434\u0443\u0442 \u043f\u043e\u043f\u0430\u0434\u0430\u0442\u044c\u0441\u044f \u0441 \u0442\u043e\u0439 \u0436\u0435 \u0447\u0430\u0441\u0442\u043e\u0442\u043e\u0439, \u0447\u0442\u043e \u0438 \u0431\u0443\u043a\u0432\u044b \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f.</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u041f\u0435\u0440\u0435\u043c\u0435\u0448\u0430\u043d\u043d\u044b\u0439 \u0430\u043b\u0444\u0430\u0432\u0438\u0442</span></p></body></html>", None))
        self.textEdit_27.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442:</span></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.textEdit_26.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0411\u0443\u043a\u0432\u044b \u0432 \u043a\u043b\u044e\u0447\u0435 \u043d\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u043f\u043e\u0432\u0442\u043e\u0440\u044f\u0442\u0441\u044f, \u0438\u043d\u0430\u0447\u0435 \u043d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u0441\u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442!</span></p></body></html>", None))
        self.textEdit_20.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043a\u043b\u044e\u0447\u0430", None))
        self.textEdit_44.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_3.setText("")
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0430\u043b\u0444\u0430\u0432\u0438\u0442:</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u043a\u043b\u044e\u0447:</span></p></body></html>", None))
        self.textEdit_28.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u041f\u0440\u0438 \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u043c \u043a\u043b\u044e\u0447\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435</span><span style=\" color:#000000;\"> </span><span style=\" color:#6a5acd;\">\u00abNOBODY LIKES MORNING\u00bb</span><span style=\" color:#000000;\"> </span><span style=\" color:#ffffff;\">\u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043e \u0432</span><span style=\" color:#000000;\"> </span><span style=\" col"
                        "or:#6a5acd;\">\u00abXDJDBS TPIGU MDQXPXF\u00bb</span><span style=\" color:#000000;\">.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p></body></html>", None))
        self.textEdit_30.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:34pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u041e\u0442 \u0430\u0432\u0442\u043e\u0440\u0430</span></p></body></html>", None))
        self.textEdit_31.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u041f\u043e\u0437\u0434\u0440\u0430\u0432\u043b\u044f\u0435\u043c, \u0412\u044b \u0438\u0437\u0443\u0447\u0438\u043b\u0438 4 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430, \u0440\u0430\u0437\u043e\u0431\u0440\u0430\u043b\u0438 \u0441\u043b\u043e\u0436\u043d\u044b\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b \u0438 \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u0443\u0437\u043d\u0430\u043b\u0438 \u043e\u0431 \u043e\u0433\u0440\u043e\u043c"
                        "\u043d\u043e\u043c \u043c\u0438\u0440\u0435 \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438! \u041d\u043e \u0441\u0442\u043e\u0438\u0442 \u0443\u0447\u0435\u0441\u0442\u044c, \u0447\u0442\u043e \u0432\u0441\u0435 \u0440\u0430\u0437\u043e\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0448\u0438\u0444\u0440\u044b \u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430\u043c\u0438 \u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0431\u044b\u043b\u0430 \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u0430 \u0434\u043e \u0438\u0437\u043e\u0431\u0440\u0435\u0442\u0435\u043d\u0438\u044f \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043e"
                        "\u0432. \u041d\u043e \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u0448\u0430\u0433\u043d\u0443\u043b \u0434\u0430\u043b\u0435\u043a\u043e \u0432\u043f\u0435\u0440\u0435\u0434. \u0412 \u043d\u0430\u0448\u0435 \u0432\u0440\u0435\u043c\u044f - \u0432\u0440\u0435\u043c\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439 - \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 \u0431\u043e\u043b\u044c\u0448\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0447\u0435\u043d\u044c \u0441\u043b\u043e\u0436\u043d\u044b\u0445 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u043e\u0432 \u0438 \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u044b \u043f\u043e \u0441\u0435\u0439 \u0434\u0435\u043d\u044c \u0442\u0440\u0443\u0434\u044f\u0442\u0441\u044f \u043d\u0430\u0434 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435\u043c \u0435\u0449\u0435 \u0431\u043e\u043b\u0435\u0435"
                        " \u0441\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u044b\u0445 \u0448\u0438\u0444\u0440\u043e\u0432. \u0414\u043b\u044f \u0441\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0430 \u043d\u0435 \u0441\u043e\u0441\u0442\u0430\u0432\u0438\u0442 \u0442\u0440\u0443\u0434\u0430 \u0432\u0437\u043b\u043e\u043c\u0430\u0442\u044c \u0434\u0430\u0436\u0435 \u043c\u043e\u043d\u043e\u0430\u043b\u0444\u0430\u0432\u0438\u0442\u043d\u044b\u0439 \u0448\u0438\u0444\u0440, \u043f\u043e\u044d\u0442\u043e\u043c\u0443 \u043d\u0435 \u0441\u0442\u043e\u0438\u0442 \u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0434\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e, \u043e\u043f\u0438\u0440\u0430\u044f\u0441\u044c \u043d\u0430 \u0437\u0430\u0449\u0438\u0442\u0443 \u0448\u0438\u0444\u0440\u043e\u0432 \u0438\u0437 \u044d\u0442\u043e\u0433\u043e \u043f\u0440\u0438"
                        "\u043b\u043e\u0436\u0435\u043d\u0438\u044f. \u0426\u0435\u043b\u044c Cryptography for beginners - \u043f\u043e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0441 \u0443\u0434\u0438\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u043c \u043c\u0438\u0440\u043e\u043c \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0438 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u043f\u0440\u043e\u0446\u0435\u0441\u0441 \u0438\u0437\u0443\u0447\u0435\u043d\u0438\u044f \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u043b\u0435\u0433\u043a\u0438\u043c \u0438 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u044b\u043c.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0p"
                        "x; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0421\u043f\u0430\u0441\u0438\u0431\u043e, \u0447\u0442\u043e \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u043d\u0430\u0441.</span></p></body></html>", None))
        self.label_4.setText("")
        self.textEdit_38.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:34pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0435\u0440\u043c\u0438\u043d\u043e\u0432</span></p></body></html>", None))
        self.textEdit_41.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#6a5acd;\">\u041a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f</span><span style=\" font-size:12pt; color:#ffffff;\"> \u2013 \u044d\u0442\u043e \u043d\u0430\u0443\u043a\u0430, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0438\u0437\u0443\u0447\u0430\u0435\u0442 \u0441\u043f\u043e\u0441\u043e\u0431\u044b \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0445 \u043a\u043e"
                        "\u0434\u043e\u0432. \u041a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0438\u0441\u0442\u043e\u0440\u0438\u0447\u0435\u0441\u043a\u0438 \u0437\u0430\u0440\u043e\u0434\u0438\u043b\u0430\u0441\u044c \u0438\u0437 \u043f\u043e\u0442\u0440\u0435\u0431\u043d\u043e\u0441\u0442\u0438 \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0438 \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438. \u0421 \u043d\u0435\u0437\u0430\u043f\u0430\u043c\u044f\u0442\u043d\u044b\u0445 \u0432\u0440\u0435\u043c\u0435\u043d \u0432\u0441\u0435, \u043a\u043e\u043c\u0443 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043b\u043e\u0441\u044c \u043e\u0431\u043c\u0435\u043d\u0438\u0432\u0430\u0442\u044c\u0441\u044f \u0442\u0430\u0439\u043d\u044b\u043c\u0438 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f\u043c\u0438, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0448\u043f\u0438\u043e\u043d\u044b, \u0432\u043e\u0435\u043d\u043d\u044b\u0435, \u043f\u0438\u0440\u0430"
                        "\u0442\u044b, \u0442\u043e\u0440\u0433\u043e\u0432\u0446\u044b \u0438 \u0434\u0438\u043f\u043b\u043e\u043c\u0430\u0442\u044b \u043f\u0440\u0438\u0431\u0435\u0433\u0430\u043b\u0438 \u043a \u0437\u0430\u0441\u0435\u043a\u0440\u0435\u0447\u0438\u0432\u0430\u043d\u0438\u044e \u0441\u0432\u043e\u0438\u0445 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439, \u0447\u0442\u043e\u0431\u044b \u0442\u0430\u0439\u043d\u044b \u043e\u0441\u0442\u0430\u0432\u0430\u043b\u0438\u0441\u044c \u043d\u0430\u0434\u0435\u0436\u043d\u043e \u0441\u043a\u0440\u044b\u0442\u044b \u043e\u0442 \u043f\u043e\u0441\u0442\u043e\u0440\u043e\u043d\u043d\u0438\u0445 \u0433\u043b\u0430\u0437.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-size:12pt; color:#6a5acd;\">\u041a\u043b\u044e\u0447</span><span style=\" font-size:12pt; color:#ffffff;\"> - \u043d\u0430\u0431\u043e\u0440 \u043a\u0430\u043a\u0438\u0445-\u043b\u0438\u0431\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432, \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043c\u044b \u043c\u043e\u0436\u0435\u043c \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u0438\u043b\u0438 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f \u043a \u0443\u0436\u0435 \u0437\u0430\u0441\u0435\u043a\u0440\u0435\u0447\u0435\u043d\u043d\u043e\u043c\u0443 \u0442\u0435\u043a\u0441\u0442\u0443.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p alig"
                        "n=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#6a5acd;\">\u041f\u043e\u0434\u043a\u043b\u044e\u0447</span><span style=\" font-size:12pt; color:#ffffff;\"> - \u0447\u0430\u0441\u0442\u044c \u043a\u043b\u044e\u0447\u0430 \u0438\u043b\u0438 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0439 \u0435\u0433\u043e \u0441\u0438\u043c\u0432\u043e\u043b.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#6a5acd;\">\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u0442\u0435\u043a\u0441\u0442</span><span style=\" font-size:12pt; color:#ffffff;\"> - \u0438"
                        "\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#6a5acd;\">\u0428\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442</span><span style=\" font-size:12pt; color:#ffffff;\"> - \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0440\u0430\u0431\u043e\u0442\u044b \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f: \u0437\u0430\u0441"
                        "\u0435\u043a\u0440\u0435\u0447\u0435\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442, \u043a \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u043d\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u0443 \u043f\u043e\u0441\u0442\u043e\u0440\u043e\u043d\u043d\u0438\u0445 \u043b\u0438\u0446.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#6a5acd;\">\u041a\u0440\u0438\u043f\u0442\u043e\u0430\u043d\u0430\u043b\u0438\u0437</span><span style=\" font-size:12pt; color:#ffffff;\"> - \u043f\u0440\u043e\u0446\u0435\u0441\u0441 \u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0438 \u0437\u0430\u0448"
                        "\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u0431\u0435\u0437 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043b\u044f \u044d\u0442\u043e\u0433\u043e \u043a\u043b\u044e\u0447\u0430, &quot;\u0432\u0437\u043b\u043e\u043c&quot; \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#6a5acd;\">\u041c\u0435\u0442\u043e\u0434 \u0433\u0440\u0443\u0431\u043e\u0439 \u0441\u0438\u043b\u044b</span><span style=\" font-size:12pt; color:#ffffff;\"> - \u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432"
                        "\u0430\u043d\u0438\u0435 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0443\u0442\u0435\u043c \u043f\u0435\u0440\u0435\u0431\u043e\u0440\u0430 \u0432\u0441\u0435\u0445 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043a\u043b\u044e\u0447\u0435\u0439.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#6a5acd;\">\u0427\u0430\u0441\u0442\u043e\u0442\u043d\u044b\u0439 \u0430\u043d\u0430\u043b\u0438\u0437</span><span style=\" font-size:12pt; color:#ffffff;\"> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 \u043e\u043f\u0440\u0435\u0434"
                        "\u0435\u043b\u0435\u043d\u0438\u044f \u0442\u043e\u0433\u043e, \u043d\u0430\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0447\u0430\u0441\u0442\u043e \u0431\u0443\u043a\u0432\u044b \u043f\u043e\u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0432 \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0445 \u0442\u0435\u043a\u0441\u0442\u0430\u0445 \u0438 \u0448\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442\u0430\u0445. \u0415\u0441\u043b\u0438 \u043f\u0440\u043e\u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u043e\u0439, \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u043f\u0440\u043e\u0441\u0442\u044b\u043c \u043f\u043e\u0434\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u043c \u0448\u0438\u0444\u0440\u043e\u043c \u0442\u0435\u043a\u0441\u0442, \u0442\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u0432 \u044d\u0442\u043e\u043c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0438 \u0431\u0443\u0434"
                        "\u0443\u0442 \u0432\u0441\u0442\u0440\u0435\u0447\u0430\u0442\u044c\u0441\u044f \u0432 \u0442\u043e\u0439 \u0436\u0435 \u0447\u0430\u0441\u0442\u043e\u0442\u043e\u0439, \u043a\u0430\u043a \u0438 \u0431\u0443\u043a\u0432\u044b \u0432 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u043c \u0438\u043b\u0438 \u0440\u0443\u0441\u0441\u043a\u043e\u043c \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0435. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043d\u0430\u0438\u0431\u043e\u043b\u0435\u0435 \u0447\u0430\u0441\u0442\u043e \u0432\u0441\u0442\u0440\u0435\u0447\u0430\u0435\u043c\u0430\u044f \u0431\u0443\u043a\u0432\u0430 \u0432 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u043c \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0435 - &quot;\u0415&quot;, \u0432 \u0440\u0443\u0441\u0441\u043a\u043e\u043c - &quot;\u041e&quot;.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; fon"
                        "t-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u044b\u043c \u0438 \u0430\u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u044b\u043c. </span><span style=\" font-size:12pt; color:#6a5acd;\">\u0421\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e\u0435 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435</span><span style=\" font-size:12pt; color:#ffffff;\"> \u2013 \u044d\u0442\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c, \u0432 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0432 \u0431\u043e\u043b\u044c\u0448\u0438\u043d\u0441\u0442\u0432\u0435 \u0441\u043b\u0443"
                        "\u0447\u0430\u0435\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u043e\u0434\u043d\u0438 \u0438 \u0442\u0435 \u0436\u0435 \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043a\u043b\u044e\u0447\u0438 \u043a\u0430\u043a \u0434\u043b\u044f \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430, \u0442\u0430\u043a \u0438 \u0434\u043b\u044f \u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0448\u0438\u0444\u0440\u043e\u0442\u0435\u043a\u0441\u0442\u0430. \u0422\u0430\u043a\u0438\u0435 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u044b \u0442\u0440\u0435\u0431\u0443\u044e\u0442, \u0447\u0442\u043e\u0431\u044b \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c \u0438 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c \u0441\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043b\u0438"
                        " \u043a\u043b\u044e\u0447 \u0434\u043e \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0438 \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0445 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439. \u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c \u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e\u0433\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 \u0437\u0430\u0432\u0438\u0441\u0438\u0442 \u043e\u0442 \u043a\u043b\u044e\u0447\u0430. \u0415\u0433\u043e \u0440\u0430\u0441\u043a\u0440\u044b\u0442\u0438\u0435 \u043e\u0437\u043d\u0430\u0447\u0430\u0435\u0442, \u0447\u0442\u043e \u043a\u0442\u043e \u0443\u0433\u043e\u0434\u043d\u043e \u0441\u043c\u043e\u0436\u0435\u0442 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u0438 \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f. \u0412\u0441\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u043d\u044b"
                        "\u0435 \u0441\u043f\u043e\u0441\u043e\u0431\u044b \u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u044b\u043c\u0438, \u043f\u043e\u0442\u043e\u043c\u0443 \u0447\u0442\u043e \u043d\u0430 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u043c \u044d\u0442\u0430\u043f\u0435 \u0438\u0445 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430\u0438\u0431\u043e\u043b\u0435\u0435 \u043f\u043e\u043d\u044f\u0442\u0435\u043d. \u0410\u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e\u0435 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u0440\u0430\u0437\u0443\u043c\u0435\u0432\u0430\u0435\u0442 \u043f\u043e\u0434 \u0441\u043e\u0431\u043e\u0439 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u044b \u043a\u043b\u044e\u0447\u0435\u0439: \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u043a\u043b\u044e\u0447\u0430 \u2013"
                        " \u0434\u043b\u044f \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f, \u0438 \u0437\u0430\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u2013 \u0434\u043b\u044f \u0434\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p></body></html>", None))
    # retranslateUi
    def code_caesar_encrypt(self):
        text = self.textEdit_2.toPlainText()
        key = self.textEdit_43.toPlainText()
        self.textEdit_7.setPlainText(caesar_cipher_1(int(key), text, 'encrypt', self.checkBox.isChecked()))
    def code_caesar_decrypt(self):
        text = self.textEdit_2.toPlainText()
        key = self.textEdit_43.toPlainText()
        self.textEdit_7.setPlainText(caesar_cipher_1(int(key), text, 'decrypt', self.checkBox.isChecked()))
    def copy_text_1(self):
        pyperclip.copy(self.textEdit_7.toPlainText())
    def random_key_1(self):
        self.textEdit_43.setPlainText(str(getRandomKey_1(self.checkBox.isChecked())))
    def delete_1(self):
        self.textEdit_2.clear()

    def code_transposition_encrypt(self):
        text = self.textEdit_29.toPlainText()
        key = self.textEdit_34.toPlainText()
        self.textEdit_45.setPlainText(transposition(int(key), text, 'encrypt'))
    def code_transposition_decrypt(self):
        text = self.textEdit_29.toPlainText()
        key = self.textEdit_34.toPlainText()
        self.textEdit_45.setPlainText(transposition(int(key), text, 'decrypt'))
    def copy_text_2(self):
        pyperclip.copy(self.textEdit_45.toPlainText())
    def random_key_2(self):
        if len(self.textEdit_29.toPlainText())!=0:
                self.textEdit_34.setPlainText(str(getRandomKey_2(self.textEdit_29.toPlainText())))
        else:
                error=QMessageBox()
                error.setWindowTitle('Ошибка')
                error.setText('Введите текст сообщения')
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
                error.setDefaultButton(QMessageBox.Ok)
                error.setInformativeText('Чтобы сгенерировать ключ для перестановочного шифра, необходимо ввести текст :)')
                error.exec_()
    def delete_2(self):
        self.textEdit_29.clear()

    def code_vigenere_encrypt(self):
        text = self.textEdit_12.toPlainText()
        key = self.textEdit_42.toPlainText()
        self.textEdit_17.setPlainText(vigenere_cipher(str(key), text, 'encrypt', self.checkBox_3.isChecked()))
    def code_vigenere_decrypt(self):
        text = self.textEdit_12.toPlainText()
        key = self.textEdit_42.toPlainText()
        self.textEdit_17.setPlainText(vigenere_cipher(str(key), text, 'decrypt', self.checkBox_3.isChecked()))
    def copy_text_3(self):
        pyperclip.copy(self.textEdit_17.toPlainText())
    def random_key_3(self):
        self.textEdit_42.setPlainText(getRandomKey_3(self.checkBox_3.isChecked()))
    def delete_3(self):
        self.textEdit_12.clear()

    def code_sim_sub_encrypt(self):
        text = self.textEdit_20.toPlainText()
        key = self.textEdit_25.toPlainText()
        #and text[0].upper() in alphabet_4(self.checkBox_4.isChecked())
        if len(key)==len(alphabet_4(self.checkBox_4.isChecked())): 
                self.textEdit_44.setPlainText(simple_substitution_cipher_1(key, text, 'encrypt', self.checkBox_4.isChecked()))
        else:
                error=QMessageBox()
                error.setWindowTitle('Ошибка')
                error.setText('Ключ введен некоректно')
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
                error.setDefaultButton(QMessageBox.Ok)
                error.setInformativeText('Возможно, ваш ключ введен неверно или не совпадает с выбранным языком сообщения :)')
                error.exec_()
    def code_sim_sub_decrypt(self):
        text = self.textEdit_20.toPlainText()
        key = self.textEdit_25.toPlainText()
        if len(key)==len(alphabet_4(self.checkBox_4.isChecked())): 
                self.textEdit_44.setPlainText(simple_substitution_cipher_1(key, text, 'decrypt', self.checkBox_4.isChecked()))
        else:
                error=QMessageBox()
                error.setWindowTitle('Ошибка')
                error.setText('Ключ введен некоректно')
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
                error.setDefaultButton(QMessageBox.Ok)
                error.setInformativeText('Возможно, ваш ключ введен неверно или не совпадает с выбранным языком сообщения :)')
                error.exec_()
    def copy_text_4(self):
        pyperclip.copy(self.textEdit_44.toPlainText())
    def random_key_4(self):
        self.textEdit_25.setPlainText(getRandomKey_4(self.checkBox_4.isChecked()))
    def delete_4(self):
        self.textEdit_20.clear()
