# coding: utf-8
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton
from PyQt5.QtGui import QFont


class EscapeWindow(QWidget):
    def __init__(self):
        super(EscapeWindow, self).__init__()

        # Window size
        self.WIDTH = 350
        self.HEIGHT = 250
        self.resize(self.WIDTH, self.HEIGHT)

        # Font
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(12)

        # Widget
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(self.WIDTH, self.HEIGHT)

        self.textEdit2 = QTextEdit(self)
        self.textEdit2.setGeometry(QRect(25, 50, 300, 100))
        self.textEdit2.setFont(font)
        self.textEdit2.setText("Вы точно хотите закрыть приложение?")
        self.textEdit2.setStyleSheet("""
        QTextEdit {
            background: rgb(35, 34, 44);
            color: white;
            border-radius: 20px;
        }""")
        self.textEdit2.setAlignment(Qt.AlignCenter)
        self.textEdit2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit2.setCursor(Qt.ArrowCursor)
        self.textEdit2.viewport().setCursor(Qt.ArrowCursor)

        # Buttons
        self.button1 = QPushButton(self)
        self.button1.setText(u"Да")
        self.button1.setGeometry(QRect(50,150,100,60))
        self.button1.setFont(font)
        #self.button1.setFocusPolicy()
        self.button1.setStyleSheet(u"""
        QPushButton {
            background: rgb(35, 34, 44);
            color: white;
            border-radius: 20px;
        }
        QPushButton:focus {
            background: rgb(127, 124, 150);
            color: white;
            border-width: 1px;
            border-style: outset;
            padding: 6px;
        }
        QPushButton:hover {
            color: white;
            border-width: 1px;
            border-style: outset;
            padding: 6px;
        }""") 

        self.button2 = QPushButton(self)
        self.button2.setText(u"Нет")
        self.button2.setGeometry(QRect(200,150,100,60))
        self.button2.setFont(font)
        self.button2.setStyleSheet(u"""
        QPushButton {
            background: rgb(35, 34, 44);
            color: white;
            border-radius: 20px;
        }
        QPushButton:focus {
            background: rgb(127, 124, 150);
            border-width: 1px;
            border-style: outset;
            padding: 6px;
        }
        QPushButton:hover {
            border-width: 1px;
            border-style: outset;
            padding: 6px;
        }"""
        )

        # Initial
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(1)

        radius = 30
        self.centralwidget.setStyleSheet(
            """
            background:rgb(35, 34, 44);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            border-width: 1px;
            border-style: outset;
            padding: 20px;
            border-color: rgb(127, 124, 150);
            """.format(radius)
        )
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
