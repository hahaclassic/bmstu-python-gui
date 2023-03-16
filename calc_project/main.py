# coding: utf-8
import sys
import converter
from info import InfoWindow
from warning import EscapeWindow
from PyQt5.QtCore import Qt, QRect, QRegularExpression, QRegularExpressionMatch, QPoint
from PyQt5.QtWidgets import QWidget, QTextEdit, QMainWindow, QPushButton, QMenu, QApplication
from PyQt5.QtGui import QFont, QTextCursor, QCursor, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
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

        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(22)

        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(12)

        # TextEdits
        self.textEdit1 = QTextEdit(self)
        self.textEdit1.setGeometry(QRect(20, 130, 460, 90))
        self.textEdit1.setFont(font2)
        self.textEdit1.setStyleSheet("""
        QTextEdit {
            background: rgb(127, 124, 150);
            color: white;
            border-radius: 20px;
        }""")
        self.textEdit1.setMouseTracking(True)
        self.textEdit1.setCursor(Qt.ArrowCursor)
        self.textEdit1.viewport().setCursor(Qt.ArrowCursor)
        self.textEdit1.setAcceptRichText(False)
        self.textEdit1.setTextInteractionFlags(Qt.NoTextInteraction)

        self.textEdit2 = QTextEdit(self)
        self.textEdit2.setGeometry(QRect(20, 80, 400, 50))
        self.textEdit2.setFont(font3)
        self.textEdit2.setText("")
        self.textEdit2.setStyleSheet("""
        QTextEdit {
            background: rgb(35, 34, 44);
            color: white;
            border-radius: 20px;
        }""")
        self.textEdit2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textEdit2.setCursor(Qt.ArrowCursor)
        self.textEdit2.viewport().setCursor(Qt.ArrowCursor)

        textEdit3 = QTextEdit(self)
        textEdit3.setGeometry(QRect(20, 9, 400, 60))
        textEdit3.setFont(font3)
        textEdit3.setText("Converter by V.Gavrilyuk")
        textEdit3.setStyleSheet("""
        QTextEdit {
            background: rgb(35, 34, 44);
            color: rgb(127, 124, 150);
            border-radius: 20px;
        }""")
        textEdit3.setTextInteractionFlags(Qt.NoTextInteraction)
        textEdit3.setCursor(Qt.ArrowCursor)
        textEdit3.viewport().setCursor(Qt.ArrowCursor)

        # Buttons
        self.button0 = QPushButton(self)
        self.button0.setText(u".")
        self.button0.setGeometry(QRect(20,600,65,80))
        self.button0.setFont(font)
        self.button0.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button1 = QPushButton(self)
        self.button1.setText(u"+/-")
        self.button1.setGeometry(QRect(95,600,65,80))
        self.button1.setFont(font)
        self.button1.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button2 = QPushButton(self)
        self.button2.setText(u"0")
        self.button2.setGeometry(QRect(180,600,140,80))
        self.button2.setFont(font)
        self.button2.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button3 = QPushButton(self)
        self.button3.setText(u"=")
        self.button3.setGeometry(QRect(340,600,140,80))
        self.button3.setFont(font)
        self.button3.setStyleSheet(u"""
        QPushButton {
            background: rgb(127, 124, 150);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(13, 11, 29);
        }
        """)

        self.button4 = QPushButton(self)
        self.button4.setText(u"7")
        self.button4.setGeometry(QRect(20,500,140,80))
        self.button4.setFont(font)
        self.button4.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button5 = QPushButton(self)
        self.button5.setText(u"8")
        self.button5.setGeometry(QRect(180,500,140,80))
        self.button5.setFont(font)
        self.button5.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button6 = QPushButton(self)
        self.button6.setText(u"9")
        self.button6.setGeometry(QRect(340,500,140,80))
        self.button6.setFont(font)
        self.button6.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button7 = QPushButton(self)
        self.button7.setText(u"4")
        self.button7.setGeometry(QRect(20,400,140,80))
        self.button7.setFont(font)
        self.button7.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button8 = QPushButton(self)
        self.button8.setText(u"5")
        self.button8.setGeometry(QRect(180,400,140,80))
        self.button8.setFont(font)
        self.button8.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button9 = QPushButton(self)
        self.button9.setText(u"6")
        self.button9.setGeometry(QRect(340,400,140,80))
        self.button9.setFont(font)
        self.button9.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button10 = QPushButton(self)
        self.button10.setText(u"1")
        self.button10.setGeometry(QRect(20,300,140,80))
        self.button10.setFont(font)
        self.button10.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button11 = QPushButton(self)
        self.button11.setText(u"2")
        self.button11.setGeometry(QRect(180,300,140,80))
        self.button11.setFont(font)
        self.button11.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button12 = QPushButton(self)
        self.button12.setText(u"3")
        self.button12.setGeometry(QRect(340,300,140,80))
        self.button12.setFont(font)
        self.button12.setStyleSheet(u"""
        QPushButton {
            background: rgb(13, 11, 29);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            background: rgb(127, 124, 150);
        }
        """)

        self.button13 = QPushButton(self)
        self.button13.setText(u"10 n/s")
        self.button13.setGeometry(QRect(20,230,140,60))
        self.button13.setFont(font)
        self.button13.setStyleSheet(u"""
        QPushButton {
            background: rgb(35, 34, 44);
            color: rgb(127, 124, 150);
            border-radius: 20px;
        }
        """)
        
        self.button14 = QPushButton(self)
        self.button14.setText(u"6 n/s")
        self.button14.setGeometry(QRect(180,230,140,60))
        self.button14.setFont(font)
        self.button14.setStyleSheet(u"""
        QPushButton {
            background: rgb(35, 34, 44);
            color: white;
            border-radius: 20px;
        }
        """)

        self.button15 = QPushButton(self)
        self.button15.setText(u"clear")
        self.button15.setGeometry(QRect(340,230,140,60))
        self.button15.setFont(font)
        self.button15.setStyleSheet(u"""
        QPushButton {
            background: rgb(35, 34, 44);
            color: white;
            border-radius: 20px;
        }
        QPushButton:pressed {
            color: rgb(127, 124, 150);
        }
        """)
        
        self.button16 = QPushButton(self)
        self.button16.setText(u"⮾")
        self.button16.setGeometry(QRect(455,10,30,30))
        self.button16.setFont(font)
        self.button16.setStyleSheet(u"""
        QPushButton {
            background: rgb(35, 34, 44);
            color: rgb(127, 124, 150);
            border-radius: 20px;
        }
        QPushButton:pressed {
            color: rgb(35, 34, 44);
        }
        """)

        self.button18 = QPushButton(self)
        self.button18.setText(u"🗗")
        self.button18.setGeometry(QRect(420,4,35,35))
        self.button18.setFont(font)
        self.button18.setStyleSheet(u"""
        QPushButton {
            background: rgb(35, 34, 44);
            color: rgb(127, 124, 150);
            border-radius: 20px;
        }
        QPushButton:pressed {
            color: rgb(35, 34, 44);
        }
        """)

        self.button19 = QPushButton(self)
        self.button19.setText(u"🛈")
        self.button19.setGeometry(QRect(390,10,30,30))
        self.button19.setFont(font)
        self.button19.setStyleSheet(u"""
        QPushButton {
            background: rgb(35, 34, 44);
            color: rgb(127, 124, 150);
            border-radius: 20px;
        }
        QPushButton:pressed {
            color: rgb(35, 34, 44);
        }
        """)

        self.button17 = QPushButton(self)
        self.button17.setText(u"<<")
        self.button17.setGeometry(QRect(420,145,50,50))
        self.button17.setFont(font)
        self.button17.setStyleSheet(u"""
        QPushButton {
            background: rgb(127, 124, 150);
            color: rgb(35, 34, 44);
            border-radius: 20px;
        }
        QPushButton:pressed {
            color: rgb(127, 124, 150);
        }
        """)

        # Button actions
        self.button13.setCheckable(True)
        self.button14.setCheckable(True)
        self.button13.clicked[bool].connect(self.set_number_system)
        self.button14.clicked[bool].connect(self.set_number_system)

        self.button16.clicked.connect(self.button_close_window)
        self.button3.clicked.connect(self.calculation)
        self.button15.clicked.connect(self.clear_all)
        self.button17.clicked.connect(self.delete_last)
        self.button18.clicked.connect(self.mini_window)
        self.button19.clicked.connect(self.show_info)

        self.button0.clicked.connect(self.print_nums)
        self.button1.clicked.connect(self.print_nums)
        self.button2.clicked.connect(self.print_nums)
        self.button3.clicked.connect(self.print_nums)
        self.button4.clicked.connect(self.print_nums)
        self.button5.clicked.connect(self.print_nums)
        self.button6.clicked.connect(self.print_nums)
        self.button7.clicked.connect(self.print_nums)
        self.button8.clicked.connect(self.print_nums)
        self.button9.clicked.connect(self.print_nums)
        self.button10.clicked.connect(self.print_nums)
        self.button11.clicked.connect(self.print_nums)
        self.button12.clicked.connect(self.print_nums)

        # Menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.menu)

        # Initial
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Main window style
        radius = 30
        self.centralwidget.setStyleSheet(
            """
            background:rgb(35, 34, 44);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius))
        self.moveFlag = True
        self.number_system = 10
        self.printFlag = True

    # Проверка входных значений
    def check(self, mode):
        regex = QRegularExpression()
        match_text = QRegularExpressionMatch()
        if self.number_system == 10:
            regex.setPattern("^[-]?(0|[1-9]\d*)([.]\d+)?$")
        else:
            regex.setPattern("^[-]?(0|[1-5][0-5]*)([.][0-5]+)?$")
        text = self.textEdit1.toPlainText()
        match_text = regex.match(text)
        valid_text = match_text.hasMatch()
        # if len(text) >= 20:
        #     self.printFlag = False
        # else:
        self.printFlag = True
        if (not valid_text and len(text) != 0): #or len(text) > 20:
            if mode == 'change':
                self.textEdit1.setStyleSheet("""
                    QTextEdit {
                        background: rgb(127, 124, 150);
                        color: rgb(67, 22, 22);
                        border-radius: 20px;
                    }""")
                self.button3.setStyleSheet(u"""
                    QPushButton {
                        background: rgb(13, 11, 29);
                        color: white;
                        border-radius: 20px; 
                    }
                    QPushButton:pressed {
                        background: rgb(13, 11, 29);
                    }""")
            elif mode == 'value':
                return False
        else:
            if mode == 'change':
                self.textEdit1.setStyleSheet("""
                    QTextEdit {
                        background: rgb(127, 124, 150);
                        color: white;
                        border-radius: 20px;
                    }""")
                self.button3.setStyleSheet(u"""
                    QPushButton {
                        background: rgb(127, 124, 150);
                        color: white;
                        border-radius: 20px; 
                    }
                    QPushButton:pressed {
                        background: rgb(13, 11, 29);
                    }""")
            elif mode == 'value':
                return True

    # Вывод чисел и точки нажатием клавиш
    def print_nums(self):
        button_text = self.sender().text()
        if button_text != '+/-' and button_text != '=':
            cursor = QTextCursor(self.textEdit1.document())
            cursor.setPosition(len(self.textEdit1.toPlainText()))
            self.textEdit1.setTextCursor(cursor)

            text = self.textEdit1.toPlainText()
            buttons6 = [str(x) for x in range(6)]
            buttons10 = [str(x) for x in range(10)]
            cond1 = (button_text == '.' and '.' not in text and len(text) > 0)
            cond2 = (self.number_system == 6 and button_text in buttons6)
            cond3 = (self.number_system == 10 and button_text in buttons10)

            if (cond1 or cond2 or cond3) and self.printFlag:
                self.textEdit1.insertPlainText(button_text)
        elif button_text == '+/-':
            text = self.textEdit1.toPlainText()
            if len(text) != 0:
                if text[0] == '-':
                    self.textEdit1.setPlainText(text[1:])
                else:
                    self.textEdit1.setPlainText("-"+text)
        self.check('change')

    # Очищение всех полей
    def clear_all(self):
        self.textEdit1.setPlainText('')
        self.textEdit2.setPlainText('')
        self.check('change')

    # Удаление последнего символа
    def delete_last(self):
        text = self.textEdit1.toPlainText()
        self.textEdit1.setPlainText(text[:-1])
        self.textEdit2.setPlainText('')
        self.check('change')
    
    # Перевод числа в другую систему счисления
    def calculation(self):
        text = self.textEdit1.toPlainText()
        if self.check('value') and len(text) != 0:
            if self.number_system == 10:
                result = converter.decimal_to_six(text)
                self.textEdit2.setPlainText(text + ' =')
                self.textEdit1.setPlainText(result)
            else:
                result = converter.six_to_decimal(text)
                self.textEdit2.setPlainText(text + ' =')
                self.textEdit1.setPlainText(result)
    
    # Изменение системы счисления
    def set_number_system(self):
        sender = self.sender()
        if sender.text() == "10 n/s":
            sender.setStyleSheet("""
            QPushButton {
                background: rgb(35, 34, 44);
                color: rgb(127, 124, 150);
                border-radius: 20px;
            }""")
            
            self.button14.setStyleSheet("""
            QPushButton {
                background: rgb(35, 34, 44);
                color: white;
                border-radius: 20px;
            }""")

            self.button4.setStyleSheet(u"""
            QPushButton {
                background: rgb(13, 11, 29);
                color: white;
                border-radius: 20px;
            }
             QPushButton:pressed {
            background: rgb(127, 124, 150);
            }
            """)

            self.button5.setStyleSheet(u"""
            QPushButton {
                background: rgb(13, 11, 29);
                color: white;
                border-radius: 20px;
            }
            QPushButton:pressed {
            background: rgb(127, 124, 150);
            }
            """)

            self.button6.setStyleSheet(u"""
            QPushButton {
                background: rgb(13, 11, 29);
                color: white;
                border-radius: 20px;
            }
             QPushButton:pressed {
            background: rgb(127, 124, 150);
            }
            """)

            self.button9.setStyleSheet(u"""
            QPushButton {
                background: rgb(13, 11, 29);
                color: white;
                border-radius: 20px;
            }
             QPushButton:pressed {
            background: rgb(127, 124, 150);
            }
            """)

            self.number_system = 10
            
        elif sender.text() == "6 n/s":
            sender.setStyleSheet("""
            QPushButton {
                background: rgb(35, 34, 44);
                color: rgb(127, 124, 150);
                border-radius: 20px;
            }""")
            
            self.button13.setStyleSheet("""
            QPushButton {
                background: rgb(35, 34, 44);
                color: white;
                border-radius: 20px;
            }""")

            self.button4.setStyleSheet(u"""
            QPushButton {
                background: rgba(13, 11, 29, 100);
                color: white;
                border-radius: 20px;
            }
            """)

            self.button5.setStyleSheet(u"""
            QPushButton {
                background: rgba(13, 11, 29, 100);
                color: white;
                border-radius: 20px;
            }
            """)

            self.button6.setStyleSheet(u"""
            QPushButton {
                background: rgba(13, 11, 29, 100);
                color: white;
                border-radius: 20px;
            }
            """)

            self.button9.setStyleSheet(u"""
            QPushButton {
                background: rgba(13, 11, 29, 100);
                color: white;
                border-radius: 20px;
            }
            """)

            self.number_system = 6
        self.textEdit2.setPlainText('')
        self.check('change')

    # Установка меню на правую клавишу мыши
    def menu(self, pos):
        menu = QMenu()
        exit_option = menu.addAction('Exit')
        exit_option.triggered.connect(lambda: exit())
        menu.exec_(self.mapToGlobal(pos))

    # Показывание информационного табло
    def show_info(self):
        self.info_widget = InfoWindow()
        self.info_widget.show()
        self.info_widget.move(self.pos())

    # Установка перемещения окна
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if Qt.LeftButton and self.moveFlag:
                self.move(event.globalPos() - self.movePosition)
                event.accept()
        except:
            pass       

    def mouseReleaseEvent(self, QMouseEvent):
        self.moveFlag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # Привязка клавиш
    def keyPressEvent(self, event): 
        cursor = QTextCursor(self.textEdit1.document())
        cursor.setPosition(len(self.textEdit1.toPlainText()))
        self.textEdit1.setTextCursor(cursor)
        text = self.textEdit1.toPlainText()
        
        match event.key():
            case Qt.Key_Escape:
                self.key_close_window()
            case 1064:
                self.show_info()
            case Qt.Key_I:
                self.show_info()
            case 16777219:
                self.delete_last()
            case 16777220:
                self.calculation()
            case 61:
                self.calculation()
            case 16777223:
                self.clear_all()
            case 45:
                if len(text) > 0:
                    if text[0] == '-':
                        self.textEdit1.setPlainText(text[1:])
                    else:
                        self.textEdit1.setPlainText("-"+text)
            case 46:
                if self.printFlag and '.' not in text and len(text) > 0:
                    self.textEdit1.insertPlainText('.')
            case 48:
                if self.printFlag:
                    self.textEdit1.insertPlainText('0')
            case 49:
                if self.printFlag:
                    self.textEdit1.insertPlainText('1')
            case 50:
                if self.printFlag:
                    self.textEdit1.insertPlainText('2')
            case 51:
                if self.printFlag:
                    self.textEdit1.insertPlainText('3')
            case 52:
                if self.printFlag:
                    self.textEdit1.insertPlainText('4')
            case 53:
                if self.printFlag:
                    self.textEdit1.insertPlainText('5')
            case 54:
                if self.printFlag and self.number_system == 10:
                    self.textEdit1.insertPlainText('6')
            case 55:
                if self.printFlag and self.number_system == 10:
                    self.textEdit1.insertPlainText('7')
            case 56:
                if self.printFlag and self.number_system == 10:
                    self.textEdit1.insertPlainText('8')
            case 57:
                if self.printFlag and self.number_system == 10:
                    self.textEdit1.insertPlainText('9')
        
        keys = [45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
        if event.key() in keys:
            self.textEdit2.setPlainText('')
        self.check('change')

    def key_close_window(self):
        self.escape_window = EscapeWindow()
        self.escape_window.show()
        self.escape_window.move(self.pos() + QPoint(75,200))
        self.escape_window.button1.clicked.connect(self.close_all)
        self.escape_window.button2.clicked.connect(self.close_warning)

        self.escape_window.button2.setFocus(Qt.ActiveWindowFocusReason)
        self.escape_window.button2.setAutoDefault(True)
        
        self.escape_window.button1.setFocus(Qt.ActiveWindowFocusReason)
        self.escape_window.button1.setAutoDefault(True)

    def button_close_window(self):
        try:
            self.info_widget.close()
            self.close()
        except:
            try:
                self.escape_window.close()
                self.close()
            except:
                self.close()

    def close_all(self):
        self.close()
        self.escape_window.close()
    
    def close_warning(self):
        self.escape_window.close()

    def mini_window(self):
        # def find_positions(distance):
        #     positions = [0.05*distance, 0.07*distance, 0.1*distance,
        #      0.15*distance, 0.25*distance, 0.35*distance, 0.50*distance,
        #      0.70*distance, 0.9*distance, 0.95*distance]
        #     return positions

        # self.desktop = QApplication.desktop()
        # self.screenRect = self.desktop.screenGeometry()
        # self.height = self.screenRect.height()
        # self.width = self.screenRect.width()

        # distance_x = self.height - self.x()
        # if self.y() < self.width//2:
        #     distance_y = self.width//2 - self.y()
        # else:
        #     distance_y = self.y() - self.width//2
        # positions_x = find_positions(distance_x)
        # positions_y = find_positions(distance_y)

        # for i in range(10):
        #     self.move(int(positions_x[i]), int(positions_y[i]))
        #     time.sleep(1)
        self.showMinimized()
        
    

if __name__ == '__main__':
    try:
        from PyQt5.QtWinExtras import QtWin                                       
        myappid = 'mycompany.myproduct.subproduct.version'                        
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)       
    except ImportError:
        pass
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QIcon('calc-icon.svg'))
    window.show()
    sys.exit(app.exec_())
