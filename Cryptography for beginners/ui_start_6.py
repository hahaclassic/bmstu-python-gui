
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(880, 460)
        StartWindow.setMinimumSize(QSize(880, 460))
        StartWindow.setMaximumSize(QSize(880, 460))
        StartWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(114, 50, 651, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(32)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(185, 120, 511, 51))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(14)
        self.textEdit_2.setFont(font1)
        self.textEdit_2.setStyleSheet(u"color: #9a9a9a;")
        self.textEdit_2.setFrameShape(QFrame.NoFrame)
        self.textEdit_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(345, 310, 191, 61))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton.setFont(font2)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(106, 90, 205);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(72, 61, 139);     \n"
" }")
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 420, 181, 31))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(12)
        self.textEdit_3.setFont(font3)
        self.textEdit_3.setStyleSheet(u"color: rgb(154,154,154);")
        self.textEdit_3.setFrameShape(QFrame.NoFrame)
        self.textEdit_3.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(300, 200, 281, 71))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(20)
        self.textEdit_4.setFont(font4)
        self.textEdit_4.setFrameShape(QFrame.NoFrame)
        self.textEdit_4.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit_6 = QTextEdit(self.centralwidget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(640, 420, 241, 31))
        self.textEdit_6.setFont(font3)
        self.textEdit_6.setStyleSheet(u"color: rgb(106, 90, 205);")
        self.textEdit_6.setFrameShape(QFrame.NoFrame)
        self.textEdit_6.setTextInteractionFlags(Qt.NoTextInteraction)
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("StartWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#ffffff;\">Cryptography for beginners</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("StartWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#9a9a9a;\">\u041e\u0441\u043d\u043e\u0432\u044b \u043a\u0440\u0438\u043f\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0438 \u0448\u0438\u0444\u0440\u043e\u0432 \u0434\u043b\u044f \u043d\u0430\u0447\u0438\u043d\u0430\u044e\u0449\u0438\u0445</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("StartWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("StartWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c!</span></p></body></html>", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("StartWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Century Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#9a9a9a;\">made by Vladislav Gavrilyuk</span></p></body></html>", None))
    # retranslateUi

