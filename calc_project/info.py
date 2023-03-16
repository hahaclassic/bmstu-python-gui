# coding: utf-8
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton
from PyQt5.QtGui import QFont

class InfoWindow(QWidget):
    def __init__(self):
        super(InfoWindow, self).__init__()

        # Window size
        self.WIDTH = 497
        self.HEIGHT = 700
        self.resize(self.WIDTH, self.HEIGHT)

        # Widget
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(self.WIDTH, self.HEIGHT)

        # Fonts
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(16)

        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(12)

        # TextEdits
        self.textEdit2 = QTextEdit(self)
        self.textEdit2.setGeometry(QRect(20, 60, 360, 120))
        self.textEdit2.setFont(font3)
        self.textEdit2.setText("Приложение создано \nстудентом ИУ7-21Б \n\
Гаврилюком Владиславом")
        self.textEdit2.setStyleSheet("""
        QTextEdit {
            background: rgb(35, 34, 44);
            color: rgb(127, 124, 150);
            border-radius: 20px;
            border-width: 1px;
            border-style: outset;
            padding: 6px;
            border-color: rgb(127, 124, 150);
        }""")
        self.textEdit2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit2.setCursor(Qt.ArrowCursor)
        self.textEdit2.viewport().setCursor(Qt.ArrowCursor)

        textEdit3 = QTextEdit(self)
        textEdit3.setGeometry(QRect(20, 9, 360, 50))
        textEdit3.setFont(font3)
        textEdit3.setText("Converter by V.Gavrilyuk")
        textEdit3.setStyleSheet("""
        QTextEdit {
            background: rgb(35, 34, 44);
            color: white;
            border-radius: 20px;
        }""")
        textEdit3.setTextInteractionFlags(Qt.NoTextInteraction)
        textEdit3.setCursor(Qt.ArrowCursor)
        textEdit3.viewport().setCursor(Qt.ArrowCursor)

        textEdit4 = QTextEdit(self)
        textEdit4.setGeometry(QRect(20, 200, 360, 60))
        textEdit4.setFont(font3)
        textEdit4.setText("Функции приложения:")
        textEdit4.setStyleSheet("""
        QTextEdit {
            background: rgb(35, 34, 44);
            color: white;
            border-radius: 20px;
        }""")
        textEdit4.setTextInteractionFlags(Qt.NoTextInteraction)
        textEdit4.setCursor(Qt.ArrowCursor)
        textEdit4.viewport().setCursor(Qt.ArrowCursor)

        self.textEdit5 = QTextEdit(self)
        self.textEdit5.setGeometry(QRect(20, 250, 360, 180))
        self.textEdit5.setFont(font3)
        self.textEdit5.setText("Перевод вещественных \nчисел \
из десятичной системы счисления в \nшестиричную систему и обратно")
        self.textEdit5.setStyleSheet("""
        QTextEdit {
            background: rgb(35, 34, 44);
            color: rgb(127, 124, 150);
            border-radius: 20px;
            border-width: 1px;
            border-style: outset;
            padding: 6px;
            border-color: rgb(127, 124, 150);
        }
        """)
        self.textEdit5.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit5.setCursor(Qt.ArrowCursor)
        self.textEdit5.viewport().setCursor(Qt.ArrowCursor)

        textEdit6 = QTextEdit(self)
        textEdit6.setGeometry(QRect(20, 450, 360, 60))
        textEdit6.setFont(font3)
        textEdit6.setText("Help:")
        textEdit6.setStyleSheet("""
        QTextEdit {
            background: rgb(35, 34, 44);
            color: white;
            border-radius: 20px;
        }""")
        textEdit6.setTextInteractionFlags(Qt.NoTextInteraction)
        textEdit6.setCursor(Qt.ArrowCursor)
        textEdit6.viewport().setCursor(Qt.ArrowCursor)

        self.textEdit7 = QTextEdit(self)
        self.textEdit7.setGeometry(QRect(20, 500, 360, 180))
        self.textEdit7.setFont(font3)
        self.textEdit7.setText("10 n/s - 10 c/c, 6 n/s - 6 с/с\n\
clear - удаление всех символов\n<< - удаление последнего символа")
        self.textEdit7.setStyleSheet("""
        QTextEdit {
            background: rgb(35, 34, 44);
            color: rgb(127, 124, 150);
            border-radius: 20px;
            border-width: 1px;
            border-style: outset;
            padding: 6px;
            border-color: rgb(127, 124, 150);
        }
        """)
        self.textEdit7.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit7.setCursor(Qt.ArrowCursor)
        self.textEdit7.viewport().setCursor(Qt.ArrowCursor)

        self.button = QPushButton(self)
        self.button.setText(u"🛈")
        self.button.setGeometry(QRect(390,10,30,30))
        self.button.setFont(font)
        self.button.setStyleSheet(u"""
        QPushButton {
            background: rgb(35, 34, 44);
            color: rgb(127, 124, 150);
            border-radius: 20px;
        }
        QPushButton:pressed {
            color: rgb(35, 34, 44);
        }
        """)

        self.button.clicked.connect(self.close)

        # Initial
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        radius = 30
        self.centralwidget.setStyleSheet(
            """
            background:rgb(35, 34, 44);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            border-color: rgb(127, 124, 150);
            """.format(radius))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_I or event.key() == 1064:
            self.close()
