# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_loginvtWKhu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
from need_functions import *
class Ui_MainWindow(object):
    def login_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 559)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -10, 481, 611))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.login_label = QLabel(self.frame)
        self.login_label.setObjectName(u"label")
        self.login_label.setGeometry(QRect(140, 40, 221, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.login_label.setFont(font1)
        self.login_label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.login_label_4 = QLabel(self.frame)
        self.login_label_4.setObjectName(u"label_4")
        self.login_label_4.setGeometry(QRect(130, 120, 231, 31))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(12)
        self.login_label_4.setFont(font2)
        self.login_label_4.setStyleSheet(u"color: rgb(149, 0, 0);")
        self.login_label_2 = QLabel(self.centralwidget)
        self.login_label_2.setObjectName(u"label_2")
        self.login_label_2.setGeometry(QRect(190, 160, 131, 31))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(22)
        font3.setBold(False)
        font3.setWeight(50)
        self.login_label_2.setFont(font3)
        self.login_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.login_label_3 = QLabel(self.centralwidget)
        self.login_label_3.setObjectName(u"label_3")
        self.login_label_3.setGeometry(QRect(180, 270, 131, 31))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(22)
        self.login_label_3.setFont(font4)
        self.login_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.login_frame_2 = QFrame(self.centralwidget)
        self.login_frame_2.setObjectName(u"frame_2")
        self.login_frame_2.setGeometry(QRect(19, 80, 421, 2))
        self.login_frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.login_frame_2.setFrameShape(QFrame.StyledPanel)
        self.login_frame_2.setFrameShadow(QFrame.Raised)
        self.login_lineEdit = QLineEdit(self.centralwidget)
        self.login_lineEdit.setObjectName(u"lineEdit")
        self.login_lineEdit.setGeometry(QRect(140, 200, 181, 31))
        font5 = QFont()
        font5.setFamily(u"Gill Sans")
        font5.setPointSize(8)
        self.login_lineEdit.setFont(font5)
        self.login_lineEdit.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                    "border: 2px solid rgb(53, 53, 173, 1);\n"
                                    "border-radius: 15;\n"
                                    "color: black")
        self.login_lineEdit.setAlignment(Qt.AlignCenter)
        self.login_lineEdit.setPlaceholderText("Sneaky pass")
        self.login_lineEdit.setMaxLength(24)
        #self.login_lineEdit.setInputMask()
        my_regex = QRegExp("^[a-zA-Z0-9_-]+$")
        my_validator = QRegExpValidator(my_regex, self.login_lineEdit)
        self.login_lineEdit.setValidator(my_validator)
        self.login_lineEdit_2 = QLineEdit(self.centralwidget)
        self.login_lineEdit_2.setObjectName(u"lineEdit_2")
        self.login_lineEdit_2.setGeometry(QRect(140, 310, 181, 31))
        self.login_lineEdit_2.setFont(font5)
        self.login_lineEdit_2.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.login_lineEdit_2.setAlignment(Qt.AlignCenter)

        self.login_lineEdit_2.setPlaceholderText("Sneaky pass")
        self.login_lineEdit_2.setEchoMode(QLineEdit.Password)
        self.login_lineEdit_2.setMaxLength(24)
        #self.login_lineEdit.setInputMask()
        my_regex_2 = QRegExp("^[a-zA-Z0-9!_-]+$")
        my_validator_2 = QRegExpValidator(my_regex_2, self.login_lineEdit_2)
        self.login_lineEdit_2.setValidator(my_validator_2)

        self.login_pushButton = QPushButton(self.centralwidget)
        self.login_pushButton.setObjectName(u"pushButton")
        self.login_pushButton.setGeometry(QRect(120, 430, 221, 41))
        font6 = QFont()
        font6.setFamily(u"Century Gothic")
        font6.setPointSize(22)
        font6.setBold(True)
        font6.setWeight(75)
        self.login_pushButton.setFont(font6)
        self.login_pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.login_pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.login_pushButton.setCheckable(False)
        self.login_pushButton.setAutoDefault(False)
        self.login_pushButton_2 = QPushButton(self.centralwidget)
        self.login_pushButton_2.setObjectName(u"pushButton_2")
        self.login_pushButton_2.setGeometry(QRect(140, 480, 181, 41))
        font7 = QFont()
        font7.setFamily(u"Century Gothic")
        font7.setPointSize(18)
        font7.setBold(True)
        font7.setWeight(75)
        self.login_pushButton_2.setFont(font7)
        self.login_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.login_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.login_pushButton_2.setCheckable(False)
        self.login_pushButton_2.setAutoDefault(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.login_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def login_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Авторизация", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"SNEAKY PASS", None))
        self.login_label_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u043b\u043e\u0433\u0438\u043d \u0438\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.login_label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_lineEdit.setText("")
        self.login_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0419\u0422\u0418", None))
        #if QT_CONFIG(shortcut)
        self.login_pushButton.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.login_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        #if QT_CONFIG(shortcut)
        self.login_pushButton_2.setShortcut("")


    def reg_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(460, 558)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-29, -30, 491, 601))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.reg_label = QLabel(self.frame)
        self.reg_label.setObjectName(u"label")
        self.reg_label.setGeometry(QRect(160, 60, 255, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.reg_label.setFont(font1)
        self.reg_label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.reg_frame_2 = QFrame(self.frame)
        self.reg_frame_2.setObjectName(u"frame_2")
        self.reg_frame_2.setGeometry(QRect(50, 110, 421, 2))
        self.reg_frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.reg_frame_2.setFrameShape(QFrame.StyledPanel)
        self.reg_frame_2.setFrameShadow(QFrame.Raised)
        self.reg_label_2 = QLabel(self.centralwidget)
        self.reg_label_2.setObjectName(u"label_2")
        self.reg_label_2.setGeometry(QRect(190, 100, 91, 31))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(22)
        self.reg_label_2.setFont(font2)
        self.reg_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.reg_label_3 = QLabel(self.centralwidget)
        self.reg_label_3.setObjectName(u"label_3")
        self.reg_label_3.setGeometry(QRect(180, 180, 111, 31))
        self.reg_label_3.setFont(font2)
        self.reg_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.reg_lineEdit = QLineEdit(self.centralwidget)
        self.reg_lineEdit.setObjectName(u"lineEdit")
        self.reg_lineEdit.setGeometry(QRect(140, 140, 181, 31))
        font3 = QFont()
        font3.setFamily(u"Gill Sans")
        font3.setPointSize(8)
        self.reg_lineEdit.setFont(font3)
        self.reg_lineEdit.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                    "border: 2px solid rgb(53, 53, 173, 1);\n"
                                    "border-radius: 15;\n"
                                    "color: black")
        self.reg_lineEdit.setAlignment(Qt.AlignCenter)
        self.reg_lineEdit.setPlaceholderText("Sneaky pass")
        self.reg_lineEdit.setMaxLength(24)
        my_regex = QRegExp("^[a-zA-Z0-9_-]+$")
        my_validator = QRegExpValidator(my_regex, self.reg_lineEdit)
        self.reg_lineEdit.setValidator(my_validator)
        self.reg_lineEdit_2 = QLineEdit(self.centralwidget)
        self.reg_lineEdit_2.setObjectName(u"lineEdit_2")
        self.reg_lineEdit_2.setGeometry(QRect(140, 220, 181, 31))
        self.reg_lineEdit_2.setFont(font3)
        self.reg_lineEdit_2.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.reg_lineEdit_2.setAlignment(Qt.AlignCenter)
        self.reg_lineEdit_2.setEchoMode(QLineEdit.Password)
        self.reg_lineEdit_2.setPlaceholderText("Sneaky pass")
        self.reg_lineEdit_2.setMaxLength(24)
        my_regex_2 = QRegExp("^[a-zA-Z0-9!_-]+$")
        my_validator_2 = QRegExpValidator(my_regex_2, self.reg_lineEdit_2)
        self.reg_lineEdit_2.setValidator(my_validator_2)
        self.reg_pushButton = QPushButton(self.centralwidget)
        self.reg_pushButton.setObjectName(u"pushButton")
        self.reg_pushButton.setGeometry(QRect(60, 430, 341, 41))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(22)
        font4.setBold(True)
        font4.setWeight(75)
        self.reg_pushButton.setFont(font4)
        self.reg_pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.reg_pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.reg_pushButton.setCheckable(False)
        self.reg_pushButton.setAutoDefault(False)
        self.reg_pushButton_2 = QPushButton(self.centralwidget)
        self.reg_pushButton_2.setObjectName(u"pushButton_2")
        self.reg_pushButton_2.setGeometry(QRect(160, 480, 141, 41))
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setWeight(75)
        self.reg_pushButton_2.setFont(font5)
        self.reg_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.reg_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.reg_pushButton_2.setCheckable(False)
        self.reg_pushButton_2.setAutoDefault(False)
        self.reg_lineEdit_3 = QLineEdit(self.centralwidget)
        self.reg_lineEdit_3.setObjectName(u"lineEdit_3")
        self.reg_lineEdit_3.setGeometry(QRect(140, 300, 181, 31))
        self.reg_lineEdit_3.setFont(font3)
        self.reg_lineEdit_3.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.reg_lineEdit_3.setAlignment(Qt.AlignCenter)
        self.reg_lineEdit_3.setEchoMode(QLineEdit.Password)
        self.reg_lineEdit_3.setPlaceholderText("Sneaky pass")
        self.reg_lineEdit_3.setMaxLength(24)
        my_regex_3 = QRegExp("^[a-zA-Z0-9!_-]+$")
        my_validator_3 = QRegExpValidator(my_regex_3, self.reg_lineEdit_3)
        self.reg_lineEdit_3.setValidator(my_validator_3)
        self.reg_label_5 = QLabel(self.centralwidget)
        self.reg_label_5.setObjectName(u"label_5")
        self.reg_label_5.setGeometry(QRect(80, 260, 311, 31))
        self.reg_label_5.setFont(font2)
        self.reg_label_5.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.reg_lineEdit_4 = QLineEdit(self.centralwidget)
        self.reg_lineEdit_4.setObjectName(u"lineEdit_4")
        self.reg_lineEdit_4.setGeometry(QRect(140, 380, 181, 31))
        self.reg_lineEdit_4.setFont(font3)
        self.reg_lineEdit_4.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.reg_lineEdit_4.setAlignment(Qt.AlignCenter)
        self.reg_lineEdit_4.setPlaceholderText("Sneaky pass")
        self.reg_lineEdit_4.setMaxLength(29)
        my_regex_4 = QRegExp("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$")
        my_validator_4 = QRegExpValidator(my_regex_4, self.reg_lineEdit_4)
        self.reg_lineEdit_4.setValidator(my_validator_4)
        self.reg_label_6 = QLabel(self.centralwidget)
        self.reg_label_6.setObjectName(u"label_6")
        self.reg_label_6.setGeometry(QRect(190, 340, 111, 31))
        self.reg_label_6.setFont(font2)
        self.reg_label_6.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        MainWindow.setCentralWidget(self.centralwidget)

        self.reg_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def reg_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Регистрация", None))
        self.reg_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.reg_label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.reg_label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.reg_lineEdit.setText("")
        self.reg_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        #if QT_CONFIG(shortcut)
        self.reg_pushButton.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.reg_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        #if QT_CONFIG(shortcut)
        self.reg_pushButton_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.reg_label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.reg_label_6.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))



    def entrys_all_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(462, 563)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-8, 0, 471, 621))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.entrys_all_label = QLabel(self.frame)
        self.entrys_all_label.setObjectName(u"label")
        self.entrys_all_label.setGeometry(QRect(150, 40, 181, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.entrys_all_label.setFont(font1)
        self.entrys_all_label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.entrys_all_frame_2 = QFrame(self.frame)
        self.entrys_all_frame_2.setObjectName(u"frame_2")
        self.entrys_all_frame_2.setGeometry(QRect(20, 100, 421, 2))
        self.entrys_all_frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.entrys_all_frame_2.setFrameShape(QFrame.StyledPanel)
        self.entrys_all_frame_2.setFrameShadow(QFrame.Raised)
        self.entrys_all_verticalLayoutWidget = QWidget(self.frame)
        self.entrys_all_verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.entrys_all_verticalLayoutWidget.setGeometry(QRect(70, 110, 331, 500))
        self.entrys_all_verticalLayout = QVBoxLayout(self.entrys_all_verticalLayoutWidget)
        self.entrys_all_verticalLayout.setObjectName(u"verticalLayout")
        self.entrys_all_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.entrys_all_pushButton_6 = QPushButton(self.entrys_all_verticalLayoutWidget)
        self.entrys_all_pushButton_6.setObjectName(u"pushButton_6")
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setWeight(75)
        self.entrys_all_pushButton_6.setFont(font2)
        self.entrys_all_pushButton_6.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_6.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_all_pushButton_6.setCheckable(False)
        self.entrys_all_pushButton_6.setAutoDefault(False)

        self.entrys_all_verticalLayout.addWidget(self.entrys_all_pushButton_6)

        self.entrys_all_pushButton_2 = QPushButton(self.entrys_all_verticalLayoutWidget)
        self.entrys_all_pushButton_2.setObjectName(u"pushButton_2")
        self.entrys_all_pushButton_2.setFont(font2)
        self.entrys_all_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_all_pushButton_2.setCheckable(False)
        self.entrys_all_pushButton_2.setAutoDefault(False)

        self.entrys_all_verticalLayout.addWidget(self.entrys_all_pushButton_2)

        self.entrys_all_pushButton_8 = QPushButton(self.entrys_all_verticalLayoutWidget)
        self.entrys_all_pushButton_8.setObjectName(u"pushButton_8")
        self.entrys_all_pushButton_8.setFont(font2)
        self.entrys_all_pushButton_8.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_8.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_all_pushButton_8.setCheckable(False)
        self.entrys_all_pushButton_8.setAutoDefault(False)

        self.entrys_all_verticalLayout.addWidget(self.entrys_all_pushButton_8)

        self.entrys_all_pushButton_5 = QPushButton(self.entrys_all_verticalLayoutWidget)
        self.entrys_all_pushButton_5.setObjectName(u"pushButton_5")
        self.entrys_all_pushButton_5.setFont(font2)
        self.entrys_all_pushButton_5.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_5.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_all_pushButton_5.setCheckable(False)
        self.entrys_all_pushButton_5.setAutoDefault(False)

        self.entrys_all_verticalLayout.addWidget(self.entrys_all_pushButton_5)

        self.entrys_all_pushButton_4 = QPushButton(self.entrys_all_verticalLayoutWidget)
        self.entrys_all_pushButton_4.setObjectName(u"pushButton_4")
        self.entrys_all_pushButton_4.setFont(font2)
        self.entrys_all_pushButton_4.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_4.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_all_pushButton_4.setCheckable(False)
        self.entrys_all_pushButton_4.setAutoDefault(False)

        self.entrys_all_verticalLayout.addWidget(self.entrys_all_pushButton_4)

        self.entrys_all_frame_3 = QFrame(self.frame)
        self.entrys_all_frame_3.setObjectName(u"frame_3")
        self.entrys_all_frame_3.setGeometry(QRect(0, 0, 471, 621))
        self.entrys_all_frame_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.entrys_all_frame_3.setFrameShape(QFrame.StyledPanel)
        self.entrys_all_frame_3.setFrameShadow(QFrame.Raised)
        self.entrys_all_label_2 = QLabel(self.entrys_all_frame_3)
        self.entrys_all_label_2.setObjectName(u"label_2")
        self.entrys_all_label_2.setGeometry(QRect(150, 30, 181, 41))
        self.entrys_all_label_2.setFont(font1)
        self.entrys_all_label_2.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.entrys_all_frame_4 = QFrame(self.entrys_all_frame_3)
        self.entrys_all_frame_4.setObjectName(u"frame_4")
        self.entrys_all_frame_4.setGeometry(QRect(20, 80, 421, 2))
        self.entrys_all_frame_4.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.entrys_all_frame_4.setFrameShape(QFrame.StyledPanel)
        self.entrys_all_frame_4.setFrameShadow(QFrame.Raised)




        self.entrys_all_verticalLayoutWidget_2 = QWidget(self.entrys_all_frame_3)
        self.entrys_all_verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.entrys_all_verticalLayoutWidget_2.setGeometry(QRect(70, 100, 331, 311))
        self.entrys_all_verticalLayout_2 = QVBoxLayout(self.entrys_all_verticalLayoutWidget_2)
        self.entrys_all_verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.entrys_all_verticalLayout_2.setContentsMargins(0, 0, 0, 0)


        self.entrys_all_pushButton_7 = QPushButton(self.entrys_all_verticalLayoutWidget_2)
        self.entrys_all_pushButton_7.setObjectName(u"pushButton_7")
        self.entrys_all_pushButton_7.setFont(font2)
        self.entrys_all_pushButton_7.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_7.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_all_pushButton_7.setCheckable(False)
        self.entrys_all_pushButton_7.setAutoDefault(False)

        self.entrys_all_verticalLayout_2.addWidget(self.entrys_all_pushButton_7)

        self.entrys_all_pushButton_3 = QPushButton(self.entrys_all_verticalLayoutWidget_2)
        self.entrys_all_pushButton_3.setObjectName(u"pushButton_3")
        self.entrys_all_pushButton_3.setFont(font2)
        self.entrys_all_pushButton_3.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_3.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_all_pushButton_3.setCheckable(False)
        self.entrys_all_pushButton_3.setAutoDefault(False)

        self.entrys_all_verticalLayout_2.addWidget(self.entrys_all_pushButton_3)

        self.entrys_all_pushButton_9 = QPushButton(self.entrys_all_verticalLayoutWidget_2)
        self.entrys_all_pushButton_9.setObjectName(u"pushButton_9")
        self.entrys_all_pushButton_9.setFont(font2)
        self.entrys_all_pushButton_9.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_9.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_all_pushButton_9.setCheckable(False)
        self.entrys_all_pushButton_9.setAutoDefault(False)

        self.entrys_all_verticalLayout_2.addWidget(self.entrys_all_pushButton_9)

        self.entrys_all_pushButton_10 = QPushButton(self.entrys_all_verticalLayoutWidget_2)
        self.entrys_all_pushButton_10.setObjectName(u"pushButton_10")
        self.entrys_all_pushButton_10.setFont(font2)
        self.entrys_all_pushButton_10.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_10.setStyleSheet(u"QPushButton{\n"
                                         "	color: white;\n"
                                         "	background-color: rgba(53, 53, 173, 1);\n"
                                         "	border-radius: 20;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton: pressed {\n"
                                         "\n"
                                         "	background-color: rgba(0, 255, 255, 144)\n"
                                         "}")
        self.entrys_all_pushButton_10.setCheckable(False)
        self.entrys_all_pushButton_10.setAutoDefault(False)

        self.entrys_all_verticalLayout_2.addWidget(self.entrys_all_pushButton_10)

        self.entrys_all_pushButton_11 = QPushButton(self.entrys_all_verticalLayoutWidget_2)
        self.entrys_all_pushButton_11.setObjectName(u"pushButton_11")
        self.entrys_all_pushButton_11.setFont(font2)
        self.entrys_all_pushButton_11.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_11.setStyleSheet(u"QPushButton{\n"
                                         "	color: white;\n"
                                         "	background-color: rgba(53, 53, 173, 1);\n"
                                         "	border-radius: 20;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton: pressed {\n"
                                         "\n"
                                         "	background-color: rgba(0, 255, 255, 144)\n"
                                         "}")
        self.entrys_all_pushButton_11.setCheckable(False)
        self.entrys_all_pushButton_11.setAutoDefault(False)
        self.entrys_all_verticalLayout_2.addWidget(self.entrys_all_pushButton_11)

        self.entrys_all_pushButton_12 = QPushButton(self.entrys_all_frame_3)
        self.entrys_all_pushButton_12.setObjectName(u"pushButton_12")
        self.entrys_all_pushButton_12.setGeometry(QRect(70, 415, 40, 40))
        self.entrys_all_pushButton_12.setFont(font2)
        self.entrys_all_pushButton_12.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_12.setStyleSheet(u"QPushButton{\n"
                                                 "	color: white;\n"
                                                 "	background-color: rgba(53, 53, 173, 1);\n"
                                                 "	border-radius: 20;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton: pressed {\n"
                                                 "\n"
                                                 "	background-color: rgba(0, 255, 255, 144)\n"
                                                 "}")
        self.entrys_all_pushButton_12.setCheckable(False)
        self.entrys_all_pushButton_12.setAutoDefault(False)
        #self.entrys_all_pushButton_12.setText('<')

        self.entrys_all_pushButton_13 = QPushButton(self.entrys_all_frame_3)
        self.entrys_all_pushButton_13.setObjectName(u"pushButton_13")
        self.entrys_all_pushButton_13.setGeometry(QRect(130, 415, 40, 40))
        self.entrys_all_pushButton_13.setFont(font2)
        self.entrys_all_pushButton_13.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_13.setStyleSheet(u"QPushButton{\n"
                                                    "	color: white;\n"
                                                    "	background-color: rgba(53, 53, 173, 1);\n"
                                                    "	border-radius: 20;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton: pressed {\n"
                                                    "\n"
                                                    "	background-color: rgba(0, 255, 255, 144)\n"
                                                    "}")
        self.entrys_all_pushButton_13.setCheckable(False)
        self.entrys_all_pushButton_13.setAutoDefault(False)

        self.entrys_all_pushButton_14 = QPushButton(self.entrys_all_frame_3)
        self.entrys_all_pushButton_14.setObjectName(u"pushButton_14")
        self.entrys_all_pushButton_14.setGeometry(QRect(360, 415, 40, 40))
        self.entrys_all_pushButton_14.setFont(font2)
        self.entrys_all_pushButton_14.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton_14.setStyleSheet(u"QPushButton{\n"
                                                    "	color: white;\n"
                                                    "	background-color: rgba(53, 53, 173, 1);\n"
                                                    "	border-radius: 20;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton: pressed {\n"
                                                    "\n"
                                                    "	background-color: rgba(0, 255, 255, 144)\n"
                                                    "}")
        self.entrys_all_pushButton_14.setCheckable(False)
        self.entrys_all_pushButton_14.setAutoDefault(False)
        self.entrys_all_pushButton_14.setDisabled(True)

        self.entrys_all_verticalScrollBar = QScrollBar(self.entrys_all_frame_3)
        self.entrys_all_verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.entrys_all_verticalScrollBar.setGeometry(QRect(440, 130, 20, 411))
        self.entrys_all_verticalScrollBar.setOrientation(Qt.Vertical)
        self.entrys_all_verticalScrollBar.hide()
        self.entrys_all_pushButton = QPushButton(self.entrys_all_frame_3)
        self.entrys_all_pushButton.setObjectName(u"pushButton")
        self.entrys_all_pushButton.setGeometry(QRect(120, 480, 231, 41))
        self.entrys_all_pushButton.setFont(font2)
        self.entrys_all_pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_all_pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.entrys_all_pushButton.setCheckable(False)
        self.entrys_all_pushButton.setAutoDefault(False)
        self.entrys_all_toolButton = QToolButton(self.entrys_all_frame_3)
        self.entrys_all_toolButton.setObjectName(u"toolButton")
        self.entrys_all_toolButton.setGeometry(QRect(360, 20, 91, 21))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(11)
        font3.setBold(True)
        #font3.setBold(False)
        font3.setWeight(50)
        self.entrys_all_toolButton.setFont(font3)
        self.entrys_all_toolButton.setStyleSheet(u"color: rgb(0, 0, 127);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.entrys_all_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def entrys_all_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Все записи", None))
        self.entrys_all_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.entrys_all_pushButton_6.setText(QCoreApplication.translate("MainWindow", u"VKONTAKTE", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_6.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0419\u0422\u0418", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0419\u0422\u0418", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_8.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CHTO TO", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_5.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_4.setText(QCoreApplication.translate("MainWindow", u"SLAAACk", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_4.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.entrys_all_pushButton_7.setText(QCoreApplication.translate("MainWindow", u"VKONTAKTE", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_7.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"ODNOKLASSNIKI", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_3.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0419\u0422\u0418", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_9.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_10.setText(QCoreApplication.translate("MainWindow", u"CHTO TO", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_10.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_11.setText(QCoreApplication.translate("MainWindow", u"SLAAACk", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_11.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        #self.entrys_all_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.entrys_all_pushButton.setText(QCoreApplication.translate("MainWindow", u"Новая запись", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_12.setText(QCoreApplication.translate("MainWindow", u"<", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_12.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_13.setText(QCoreApplication.translate("MainWindow", u">", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_13.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_pushButton_14.setText(QCoreApplication.translate("MainWindow", u"№", None))
        #if QT_CONFIG(shortcut)
        self.entrys_all_pushButton_14.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_all_toolButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))


    def entrys_show_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 423)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -10, 481, 611))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.entrys_show_label = QLabel(self.frame)
        self.entrys_show_label.setObjectName(u"label")
        self.entrys_show_label.setGeometry(QRect(40, 40, 400, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(23)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.entrys_show_label.setFont(font1)
        self.entrys_show_label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.entrys_show_pushButton_2 = QPushButton(self.frame)
        self.entrys_show_pushButton_2.setObjectName(u"pushButton_2")
        self.entrys_show_pushButton_2.setGeometry(QRect(180, 370, 131, 41))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.entrys_show_pushButton_2.setFont(font2)
        self.entrys_show_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_show_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_show_pushButton_2.setCheckable(False)
        self.entrys_show_pushButton_2.setAutoDefault(False)
        self.entrys_show_label_2 = QLabel(self.frame)
        self.entrys_show_label_2.setObjectName(u"label_2")
        self.entrys_show_label_2.setGeometry(QRect(90, 150, 311, 51))
        self.entrys_show_label_2.setFont(font2)
        self.entrys_show_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")


        self.entrys_show_label_3 = QLabel(self.frame)
        self.entrys_show_label_3.setObjectName(u"label_3")
        self.entrys_show_label_3.setGeometry(QRect(200, 120, 91, 31))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(17)
        self.entrys_show_label_3.setFont(font3)
        self.entrys_show_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.entrys_show_toolButton = QToolButton(self.frame)
        self.entrys_show_toolButton.setObjectName(u"toolButton")
        self.entrys_show_toolButton.setGeometry(QRect(190, 200, 111, 21))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setWeight(50)
        self.entrys_show_toolButton.setFont(font4)
        # self.entrys_show_toolButton.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.entrys_show_toolButton.setStyleSheet(u"QPushButton{\n	color: white;\n	background-color: rgba(53, 53, 173, 1);\n	border-radius: 20;\n}\n\nQPushButton: pressed {\n\n	background-color: rgba(0, 255, 255, 144)\n}")

        self.entrys_show_pushButton = QPushButton(self.frame)
        self.entrys_show_pushButton.setObjectName(u"pushButton")
        self.entrys_show_pushButton.setGeometry(QRect(120, 320, 251, 41))
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(22)
        font5.setBold(True)
        font5.setWeight(75)
        self.entrys_show_pushButton.setFont(font5)
        self.entrys_show_pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_show_pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.entrys_show_pushButton.setCheckable(False)
        self.entrys_show_pushButton.setAutoDefault(False)
        self.entrys_show_pushButton_3 = QPushButton(self.frame)
        self.entrys_show_pushButton_3.setObjectName(u"pushButton_3")
        self.entrys_show_pushButton_3.setGeometry(QRect(160, 270, 171, 41))
        self.entrys_show_pushButton_3.setFont(font5)
        self.entrys_show_pushButton_3.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_show_pushButton_3.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.entrys_show_pushButton_3.setCheckable(False)
        self.entrys_show_pushButton_3.setAutoDefault(False)
        self.entrys_show_toolButton_2 = QToolButton(self.frame)
        self.entrys_show_toolButton_2.setObjectName(u"toolButton_2")
        self.entrys_show_toolButton_2.setGeometry(QRect(30, 30, 31, 31))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        self.entrys_show_toolButton_2.setFont(font6)
        self.entrys_show_toolButton_2.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.entrys_show_frame_2 = QFrame(self.centralwidget)
        self.entrys_show_frame_2.setObjectName(u"frame_2")
        self.entrys_show_frame_2.setGeometry(QRect(19, 80, 421, 2))
        self.entrys_show_frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.entrys_show_frame_2.setFrameShape(QFrame.StyledPanel)
        self.entrys_show_frame_2.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.entrys_show_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def entrys_show_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Просмотр записи", None))
        self.entrys_show_label.setText(QCoreApplication.translate("MainWindow", u"VKONTAKTE", None))
        self.entrys_show_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a", None))
        #if QT_CONFIG(shortcut)
        self.entrys_show_pushButton_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_show_label_2.setText(QCoreApplication.translate("MainWindow", u"FKsdfksfws254534543fgl~!?!?#2BEK@bqeb2", None))
        self.entrys_show_label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.entrys_show_toolButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        #self.entrys_show_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.entrys_show_pushButton.setText(QCoreApplication.translate("MainWindow", u"Удалить запись", None))

        #if QT_CONFIG(shortcut)
        self.entrys_show_pushButton.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_show_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        #if QT_CONFIG(shortcut)
        self.entrys_show_pushButton_3.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_show_toolButton_2.setText(QCoreApplication.translate("MainWindow", u"<", None))


    def entrys_new_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 550)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-9, -10, 481, 621))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.entrys_new_label = QLabel(self.frame)
        self.entrys_new_label.setObjectName(u"label")
        self.entrys_new_label.setGeometry(QRect(130, 50, 241, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.entrys_new_label.setFont(font1)
        self.entrys_new_label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.entrys_new_label_4 = QLabel(self.frame)
        self.entrys_new_label_4.setObjectName(u"label_4")
        self.entrys_new_label_4.setGeometry(QRect(120, 140, 241, 31))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(22)
        self.entrys_new_label_4.setFont(font2)
        self.entrys_new_label_4.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.entrys_new_label_2 = QLabel(self.centralwidget)
        self.entrys_new_label_2.setObjectName(u"label_2")
        self.entrys_new_label_2.setGeometry(QRect(190, 220, 91, 31))
        self.entrys_new_label_2.setFont(font2)
        self.entrys_new_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.entrys_new_label_3 = QLabel(self.centralwidget)
        self.entrys_new_label_3.setObjectName(u"label_3")
        self.entrys_new_label_3.setGeometry(QRect(180, 310, 111, 31))
        self.entrys_new_label_3.setFont(font2)
        self.entrys_new_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.entrys_new_frame_2 = QFrame(self.centralwidget)
        self.entrys_new_frame_2.setObjectName(u"frame_2")
        self.entrys_new_frame_2.setGeometry(QRect(19, 90, 421, 2))
        self.entrys_new_frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.entrys_new_frame_2.setFrameShape(QFrame.StyledPanel)
        self.entrys_new_frame_2.setFrameShadow(QFrame.Raised)
        self.entrys_new_lineEdit = QLineEdit(self.centralwidget)
        self.entrys_new_lineEdit.setObjectName(u"lineEdit")
        self.entrys_new_lineEdit.setGeometry(QRect(140, 260, 181, 31))
        font3 = QFont()
        font3.setFamily(u"Gill Sans")
        font3.setPointSize(8)
        self.entrys_new_lineEdit.setFont(font3)
        self.entrys_new_lineEdit.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                    "border: 2px solid rgb(53, 53, 173, 1);\n"
                                    "border-radius: 15;\n"
                                    "color: black")
        self.entrys_new_lineEdit.setAlignment(Qt.AlignCenter)
        self.entrys_new_lineEdit.setPlaceholderText("Sneaky pass")
        self.entrys_new_lineEdit.setMaxLength(19)
        my_regex = QRegExp("^[a-zA-Z0-9@._-]+$")
        my_validator = QRegExpValidator(my_regex, self.entrys_new_lineEdit)
        self.entrys_new_lineEdit.setValidator(my_validator)

        self.entrys_new_lineEdit_2 = QLineEdit(self.centralwidget)
        self.entrys_new_lineEdit_2.setObjectName(u"lineEdit_2")
        self.entrys_new_lineEdit_2.setGeometry(QRect(140, 350, 181, 31))
        self.entrys_new_lineEdit_2.setFont(font3)
        self.entrys_new_lineEdit_2.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.entrys_new_lineEdit_2.setAlignment(Qt.AlignCenter)
        self.entrys_new_lineEdit_2.setEchoMode(QLineEdit.Password)
        self.entrys_new_lineEdit_2.setPlaceholderText("Sneaky pass")
        self.entrys_new_lineEdit_2.setMaxLength(50)
        my_regex_2 = QRegExp("^[a-zA-Z0-9!_-]+$")
        my_validator_2 = QRegExpValidator(my_regex_2, self.entrys_new_lineEdit_2)
        self.entrys_new_lineEdit_2.setValidator(my_validator_2)


        self.entrys_new_pushButton = QPushButton(self.centralwidget)
        self.entrys_new_pushButton.setObjectName(u"pushButton")
        self.entrys_new_pushButton.setGeometry(QRect(120, 430, 221, 41))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(22)
        font4.setBold(True)
        font4.setWeight(75)
        self.entrys_new_pushButton.setFont(font4)
        self.entrys_new_pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_new_pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.entrys_new_pushButton.setCheckable(False)
        self.entrys_new_pushButton.setAutoDefault(False)
        self.entrys_new_pushButton_2 = QPushButton(self.centralwidget)
        self.entrys_new_pushButton_2.setObjectName(u"pushButton_2")
        self.entrys_new_pushButton_2.setGeometry(QRect(160, 480, 141, 41))
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setWeight(75)
        self.entrys_new_pushButton_2.setFont(font5)
        self.entrys_new_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.entrys_new_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(247, 247, 235, 1)\n"
                                        "}")
        self.entrys_new_pushButton_2.setCheckable(False)
        self.entrys_new_pushButton_2.setAutoDefault(False)
        self.entrys_new_lineEdit_3 = QLineEdit(self.centralwidget)
        self.entrys_new_lineEdit_3.setObjectName(u"lineEdit_3")
        self.entrys_new_lineEdit_3.setGeometry(QRect(140, 170, 181, 31))
        self.entrys_new_lineEdit_3.setFont(font3)
        self.entrys_new_lineEdit_3.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.entrys_new_lineEdit_3.setAlignment(Qt.AlignCenter)
        self.entrys_new_lineEdit_3.setPlaceholderText("Sneaky pass")
        self.entrys_new_lineEdit_3.setMaxLength(29)
        my_regex_3 = QRegExp("^[а-яА-Яa-zA-Z0-9._-]+$")
        my_validator_3 = QRegExpValidator(my_regex_3, self.entrys_new_lineEdit_3)
        self.entrys_new_lineEdit_3.setValidator(my_validator_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.entrys_new_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def entrys_new_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Создание записи", None))
        self.entrys_new_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))

        #self.entrys_new_label_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0430\u0439\u0442\u0430", None))
        self.entrys_new_label_4.setText(QCoreApplication.translate("MainWindow", u"      Название", None))

        self.entrys_new_label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.entrys_new_label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.entrys_new_lineEdit.setText("")
        self.entrys_new_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0417\u0414\u0410\u0422\u042c", None))
        #if QT_CONFIG(shortcut)
        self.entrys_new_pushButton.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        #self.entrys_new_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.entrys_new_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Назад", None))
        #if QT_CONFIG(shortcut)
        self.entrys_new_pushButton_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.entrys_new_lineEdit_3.setText("")
    # retranslateUi



    def settings_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 548)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -10, 481, 611))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.settings_label = QLabel(self.frame)
        self.settings_label.setObjectName(u"label")
        self.settings_label.setGeometry(QRect(160, 40, 181, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.settings_label.setFont(font1)
        self.settings_label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.settings_pushButton_3 = QPushButton(self.frame)
        self.settings_pushButton_3.setObjectName(u"pushButton_3")
        self.settings_pushButton_3.setGeometry(QRect(90, 260, 311, 41))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setWeight(75)
        self.settings_pushButton_3.setFont(font2)
        self.settings_pushButton_3.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_pushButton_3.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.settings_pushButton_3.setCheckable(False)
        self.settings_pushButton_3.setAutoDefault(False)
        self.settings_pushButton = QPushButton(self.frame)
        self.settings_pushButton.setObjectName(u"pushButton")
        self.settings_pushButton.setGeometry(QRect(60, 310, 361, 41))
        self.settings_pushButton.setFont(font2)
        self.settings_pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.settings_pushButton.setCheckable(False)
        self.settings_pushButton.setAutoDefault(False)
        self.settings_pushButton_4 = QPushButton(self.frame)
        self.settings_pushButton_4.setObjectName(u"pushButton_4")
        self.settings_pushButton_4.setGeometry(QRect(120, 160, 251, 41))
        self.settings_pushButton_4.setFont(font2)
        self.settings_pushButton_4.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_pushButton_4.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.settings_pushButton_4.setCheckable(False)
        self.settings_pushButton_4.setAutoDefault(False)
        self.settings_pushButton_5 = QPushButton(self.frame)
        self.settings_pushButton_5.setObjectName(u"pushButton_5")
        self.settings_pushButton_5.setGeometry(QRect(110, 210, 271, 41))
        self.settings_pushButton_5.setFont(font2)
        self.settings_pushButton_5.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_pushButton_5.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.settings_pushButton_5.setCheckable(False)
        self.settings_pushButton_5.setAutoDefault(False)
        self.settings_pushButton_6 = QPushButton(self.frame)
        self.settings_pushButton_6.setObjectName(u"pushButton_6")
        self.settings_pushButton_6.setGeometry(QRect(40, 360, 401, 41))
        self.settings_pushButton_6.setFont(font2)
        self.settings_pushButton_6.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_pushButton_6.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.settings_pushButton_6.setCheckable(False)
        self.settings_pushButton_6.setAutoDefault(False)
        self.settings_pushButton_6.hide()
        self.settings_pushButton_6.setDisabled(True)

        self.settings_pushButton_2 = QPushButton(self.frame)
        self.settings_pushButton_2.setObjectName(u"pushButton_2")
        self.settings_pushButton_2.setGeometry(QRect(120, 490, 251, 41))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.settings_pushButton_2.setFont(font3)
        self.settings_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.settings_pushButton_2.setCheckable(False)
        self.settings_pushButton_2.setAutoDefault(False)
        self.settings_toolButton_2 = QToolButton(self.frame)
        self.settings_toolButton_2.setObjectName(u"toolButton_2")
        self.settings_toolButton_2.setGeometry(QRect(30, 30, 31, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.settings_toolButton_2.setFont(font4)
        self.settings_toolButton_2.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.settings_frame_2 = QFrame(self.centralwidget)
        self.settings_frame_2.setObjectName(u"frame_2")
        self.settings_frame_2.setGeometry(QRect(19, 80, 421, 2))
        self.settings_frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.settings_frame_2.setFrameShape(QFrame.StyledPanel)
        self.settings_frame_2.setFrameShadow(QFrame.Raised)
        self.settings_toolButton = QToolButton(self.centralwidget)
        self.settings_toolButton.setObjectName(u"toolButton")
        self.settings_toolButton.setGeometry(QRect(440, 460, 31, 31))
        self.settings_toolButton.setFont(font4)
        self.settings_toolButton.setStyleSheet(u"color: rgb(0, 0, 127);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.settings_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def settings_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Настройки", None))
        self.settings_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.settings_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        #if QT_CONFIG(shortcut)
        self.settings_pushButton_3.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        #if QT_CONFIG(shortcut)
        self.settings_pushButton.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        #if QT_CONFIG(shortcut)
        self.settings_pushButton_4.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c", None))
        #if QT_CONFIG(shortcut)
        self.settings_pushButton_5.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0441\u0435\u0440\u0432\u0435\u0440\u0443", None))
        #if QT_CONFIG(shortcut)
        self.settings_pushButton_6.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        #if QT_CONFIG(shortcut)
        self.settings_pushButton_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_toolButton_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.settings_toolButton.setText(QCoreApplication.translate("MainWindow", u"<", None))


    def settings_server_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(468, 540)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -10, 481, 611))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.settings_server_label_2 = QLabel(self.frame)
        self.settings_server_label_2.setObjectName(u"label_2")
        self.settings_server_label_2.setGeometry(QRect(210, 50, 71, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(22)
        font1.setBold(False)
        font1.setWeight(50)
        self.settings_server_label_2.setFont(font1)
        self.settings_server_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_server_label_3 = QLabel(self.frame)
        self.settings_server_label_3.setObjectName(u"label_3")
        self.settings_server_label_3.setGeometry(QRect(230, 130, 41, 71))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(22)
        self.settings_server_label_3.setFont(font2)
        self.settings_server_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_server_lineEdit_4 = QLineEdit(self.frame)
        self.settings_server_lineEdit_4.setObjectName(u"lineEdit_4")
        self.settings_server_lineEdit_4.setGeometry(QRect(150, 280, 181, 31))
        font3 = QFont()
        font3.setFamily(u"Gill Sans")
        font3.setPointSize(8)
        self.settings_server_lineEdit_4.setFont(font3)
        self.settings_server_lineEdit_4.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.settings_server_lineEdit_4.setAlignment(Qt.AlignCenter)
        self.settings_server_lineEdit_3 = QLineEdit(self.frame)
        self.settings_server_lineEdit_3.setObjectName(u"lineEdit_3")
        self.settings_server_lineEdit_3.setGeometry(QRect(150, 370, 181, 31))
        self.settings_server_lineEdit_3.setFont(font3)
        self.settings_server_lineEdit_3.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.settings_server_lineEdit_3.setAlignment(Qt.AlignCenter)
        self.settings_server_label_5 = QLabel(self.frame)
        self.settings_server_label_5.setObjectName(u"label_5")
        self.settings_server_label_5.setGeometry(QRect(190, 330, 111, 31))
        self.settings_server_label_5.setFont(font2)
        self.settings_server_label_5.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_server_label_6 = QLabel(self.frame)
        self.settings_server_label_6.setObjectName(u"label_6")
        self.settings_server_label_6.setGeometry(QRect(200, 240, 91, 31))
        self.settings_server_label_6.setFont(font2)
        self.settings_server_label_6.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_server_toolButton = QToolButton(self.frame)
        self.settings_server_toolButton.setObjectName(u"toolButton")
        self.settings_server_toolButton.setGeometry(QRect(30, 30, 31, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.settings_server_toolButton.setFont(font4)
        self.settings_server_toolButton.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.settings_server_lineEdit = QLineEdit(self.centralwidget)
        self.settings_server_lineEdit.setObjectName(u"lineEdit")
        self.settings_server_lineEdit.setGeometry(QRect(140, 90, 181, 31))
        self.settings_server_lineEdit.setFont(font3)
        self.settings_server_lineEdit.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                    "border: 2px solid rgb(53, 53, 173, 1);\n"
                                    "border-radius: 15;\n"
                                    "color: black")
        self.settings_server_lineEdit.setAlignment(Qt.AlignCenter)
        self.settings_server_lineEdit_2 = QLineEdit(self.centralwidget)
        self.settings_server_lineEdit_2.setObjectName(u"lineEdit_2")
        self.settings_server_lineEdit_2.setGeometry(QRect(140, 180, 181, 31))
        self.settings_server_lineEdit_2.setFont(font3)
        self.settings_server_lineEdit_2.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.settings_server_lineEdit_2.setAlignment(Qt.AlignCenter)
        self.settings_server_pushButton = QPushButton(self.centralwidget)
        self.settings_server_pushButton.setObjectName(u"pushButton")
        self.settings_server_pushButton.setGeometry(QRect(110, 430, 241, 41))
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(22)
        font5.setBold(True)
        font5.setWeight(75)
        self.settings_server_pushButton.setFont(font5)
        self.settings_server_pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_server_pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.settings_server_pushButton.setCheckable(False)
        self.settings_server_pushButton.setAutoDefault(False)
        self.settings_server_pushButton_2 = QPushButton(self.centralwidget)
        self.settings_server_pushButton_2.setObjectName(u"pushButton_2")
        self.settings_server_pushButton_2.setGeometry(QRect(140, 480, 181, 41))
        font6 = QFont()
        font6.setFamily(u"Century Gothic")
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setWeight(75)
        self.settings_server_pushButton_2.setFont(font6)
        self.settings_server_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_server_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.settings_server_pushButton_2.setCheckable(False)
        self.settings_server_pushButton_2.setAutoDefault(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.settings_server_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def settings_server_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Настройки - Смена сервера", None))
        self.settings_server_label_2.setText(QCoreApplication.translate("MainWindow", u"port", None))
        self.settings_server_label_3.setText(QCoreApplication.translate("MainWindow", u"ip", None))
        self.settings_server_label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.settings_server_label_6.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.settings_server_toolButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.settings_server_lineEdit.setText("")
        self.settings_server_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        #if QT_CONFIG(shortcut)
        self.settings_server_pushButton.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_server_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        #if QT_CONFIG(shortcut)
        self.settings_server_pushButton_2.setShortcut("")


    def settings_sec_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 548)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -10, 481, 611))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.settings_sec_label = QLabel(self.frame)
        self.settings_sec_label.setObjectName(u"label")
        self.settings_sec_label.setGeometry(QRect(160, 40, 186, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.settings_sec_label.setFont(font1)
        self.settings_sec_label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.settings_sec_pushButton_2 = QPushButton(self.frame)
        self.settings_sec_pushButton_2.setObjectName(u"pushButton_2")
        self.settings_sec_pushButton_2.setGeometry(QRect(120, 490, 251, 41))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.settings_sec_pushButton_2.setFont(font2)
        self.settings_sec_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_sec_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.settings_sec_pushButton_2.setCheckable(False)
        self.settings_sec_pushButton_2.setAutoDefault(False)

        self.settings_sec_pushButton_3 = QPushButton(self.frame)
        self.settings_sec_pushButton_3.setObjectName(u"pushButton_2")
        self.settings_sec_pushButton_3.setGeometry(QRect(80, 310, 311, 41))
        self.settings_sec_pushButton_3.setFont(font2)
        self.settings_sec_pushButton_3.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_sec_pushButton_3.setStyleSheet(u"QPushButton{\n"
                                                     "	color: white;\n"
                                                     "	background-color: rgba(53, 53, 173, 1);\n"
                                                     "	border-radius: 20;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton: pressed {\n"
                                                     "\n"
                                                     "	background-color: rgba(0, 255, 255, 144)\n"
                                                     "}")
        self.settings_sec_pushButton_3.setCheckable(False)
        self.settings_sec_pushButton_3.setAutoDefault(False)



        self.settings_sec_label_3 = QLabel(self.frame)
        self.settings_sec_label_3.setObjectName(u"label_3")
        self.settings_sec_label_3.setGeometry(QRect(170, 90, 171, 31))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(17)
        self.settings_sec_label_3.setFont(font3)
        self.settings_sec_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_sec_label_6 = QLabel(self.frame)
        self.settings_sec_label_6.setObjectName(u"label_6")
        self.settings_sec_label_6.setGeometry(QRect(120, 190, 171, 71))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.settings_sec_label_6.setFont(font4)
        self.settings_sec_label_6.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_sec_toolButton = QToolButton(self.frame)
        self.settings_sec_toolButton.setObjectName(u"toolButton")
        self.settings_sec_toolButton.setGeometry(QRect(30, 30, 31, 31))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.settings_sec_toolButton.setFont(font5)
        self.settings_sec_toolButton.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.settings_sec_label_7 = QLabel(self.frame)
        self.settings_sec_label_7.setObjectName(u"label_7")
        self.settings_sec_label_7.setGeometry(QRect(700, 300, 201, 71))
        self.settings_sec_label_7.setFont(font4)
        self.settings_sec_label_7.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_sec_label_7.hide()
        self.settings_sec_checkBox = QCheckBox(self.frame)
        self.settings_sec_checkBox.setObjectName(u"checkBox")
        self.settings_sec_checkBox.setGeometry(QRect(330, 220, 16, 17))
        self.settings_sec_checkBox_2 = QCheckBox(self.frame)
        self.settings_sec_checkBox_2.setObjectName(u"checkBox_2")
        self.settings_sec_checkBox_2.setGeometry(QRect(730, 330, 16, 17))
        self.settings_sec_checkBox_2.hide()
        self.settings_sec_frame_2 = QFrame(self.centralwidget)
        self.settings_sec_frame_2.setObjectName(u"frame_2")
        self.settings_sec_frame_2.setGeometry(QRect(19, 80, 421, 2))
        self.settings_sec_frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.settings_sec_frame_2.setFrameShape(QFrame.StyledPanel)
        self.settings_sec_frame_2.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.settings_sec_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def settings_sec_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Настройки - Безопасность", None))
        self.settings_sec_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.settings_sec_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        #if QT_CONFIG(shortcut)
        self.settings_sec_pushButton_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        #self.settings_sec_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.settings_sec_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Установить пин-код", None))

        #if QT_CONFIG(shortcut)
        self.settings_sec_pushButton_3.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_sec_label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c", None))
        # self.settings_sec_label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0443\u0445\u0444\u0430\u043a\u0442\u043e\u0440\u043d\u0430\u044f\n"
        #                                                               " \u0430\u0443\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.settings_sec_label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0443\u0445\u0444\u0430\u043a\u0442\u043e\u0440\u043d\u0430\u044f\n"
                                                                      "\u0430\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.settings_sec_toolButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.settings_sec_label_7.setText(QCoreApplication.translate("MainWindow", u"Sms \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435", None))
        self.settings_sec_checkBox.setText("")
        self.settings_sec_checkBox_2.setText("")


    def settings_chng_user_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 552)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -10, 481, 611))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 40, 181, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 490, 251, 41))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 90, 261, 31))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(17)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(30, 30, 31, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.toolButton.setFont(font4)
        self.toolButton.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 160, 291, 41))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 230, 111, 51))
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 300, 111, 51))
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(190, 370, 111, 51))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(19, 80, 421, 2))
        self.frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def settings_chng_user_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Настройки - Смена пользователя", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        #if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"admin1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"user34", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"alisa", None))


    def settings_chng_passwd_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 552)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -10, 481, 611))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.settings_chng_passwd_label = QLabel(self.frame)
        self.settings_chng_passwd_label.setObjectName(u"label")
        self.settings_chng_passwd_label.setGeometry(QRect(160, 40, 181, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.settings_chng_passwd_label.setFont(font1)
        self.settings_chng_passwd_label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.settings_chng_passwd_pushButton_2 = QPushButton(self.frame)
        self.settings_chng_passwd_pushButton_2.setObjectName(u"pushButton_2")
        self.settings_chng_passwd_pushButton_2.setGeometry(QRect(120, 490, 251, 41))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.settings_chng_passwd_pushButton_2.setFont(font2)
        self.settings_chng_passwd_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_chng_passwd_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.settings_chng_passwd_pushButton_2.setCheckable(False)
        self.settings_chng_passwd_pushButton_2.setAutoDefault(False)
        self.settings_chng_passwd_label_3 = QLabel(self.frame)
        self.settings_chng_passwd_label_3.setObjectName(u"label_3")
        self.settings_chng_passwd_label_3.setGeometry(QRect(140, 90, 211, 31))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(17)
        self.settings_chng_passwd_label_3.setFont(font3)
        self.settings_chng_passwd_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_chng_passwd_toolButton = QToolButton(self.frame)
        self.settings_chng_passwd_toolButton.setObjectName(u"toolButton")
        self.settings_chng_passwd_toolButton.setGeometry(QRect(30, 30, 31, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.settings_chng_passwd_toolButton.setFont(font4)
        self.settings_chng_passwd_toolButton.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.settings_chng_passwd_label_2 = QLabel(self.frame)
        self.settings_chng_passwd_label_2.setObjectName(u"label_2")
        self.settings_chng_passwd_label_2.setGeometry(QRect(110, 190, 281, 41))
        self.settings_chng_passwd_label_2.setFont(font2)
        self.settings_chng_passwd_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_chng_passwd_lineEdit = QLineEdit(self.frame)
        self.settings_chng_passwd_lineEdit.setObjectName(u"lineEdit")
        self.settings_chng_passwd_lineEdit.setGeometry(QRect(150, 240, 191, 31))
        font5 = QFont()
        font5.setFamily(u"Gill Sans")
        font5.setPointSize(8)
        self.settings_chng_passwd_lineEdit.setFont(font5)
        self.settings_chng_passwd_lineEdit.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                    "border: 2px solid rgb(53, 53, 173, 1);\n"
                                    "border-radius: 15;\n"
                                    "color: black")
        self.settings_chng_passwd_lineEdit.setAlignment(Qt.AlignCenter)
        self.settings_chng_passwd_lineEdit.setEchoMode(QLineEdit.Password)
        self.settings_chng_passwd_lineEdit.setPlaceholderText("Sneaky pass")
        self.settings_chng_passwd_lineEdit.setMaxLength(24)
        my_regex = QRegExp("^[a-zA-Z0-9!_-]+$")
        my_validator = QRegExpValidator(my_regex, self.settings_chng_passwd_lineEdit)
        self.settings_chng_passwd_lineEdit.setValidator(my_validator)

        self.settings_chng_passwd_label_4 = QLabel(self.frame)
        self.settings_chng_passwd_label_4.setObjectName(u"label_4")
        self.settings_chng_passwd_label_4.setGeometry(QRect(130, 320, 231, 41))
        self.settings_chng_passwd_label_4.setFont(font2)
        self.settings_chng_passwd_label_4.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_chng_passwd_lineEdit_2 = QLineEdit(self.frame)
        self.settings_chng_passwd_lineEdit_2.setObjectName(u"lineEdit_2")
        self.settings_chng_passwd_lineEdit_2.setGeometry(QRect(150, 370, 191, 31))
        self.settings_chng_passwd_lineEdit_2.setFont(font5)
        self.settings_chng_passwd_lineEdit_2.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.settings_chng_passwd_lineEdit_2.setAlignment(Qt.AlignCenter)
        self.settings_chng_passwd_lineEdit_2.setEchoMode(QLineEdit.Password)
        self.settings_chng_passwd_lineEdit_2.setPlaceholderText("Sneaky pass")
        self.settings_chng_passwd_lineEdit_2.setMaxLength(24)
        my_regex_2 = QRegExp("^[a-zA-Z0-9!_-]+$")
        my_validator_2 = QRegExpValidator(my_regex_2, self.settings_chng_passwd_lineEdit_2)
        self.settings_chng_passwd_lineEdit.setValidator(my_validator_2)

        self.settings_chng_passwd_frame_2 = QFrame(self.centralwidget)
        self.settings_chng_passwd_frame_2.setObjectName(u"frame_2")
        self.settings_chng_passwd_frame_2.setGeometry(QRect(19, 80, 421, 2))
        self.settings_chng_passwd_frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.settings_chng_passwd_frame_2.setFrameShape(QFrame.StyledPanel)
        self.settings_chng_passwd_frame_2.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.settings_chng_passwd_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def settings_chng_passwd_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Настройки - Смена пароля", None))
        self.settings_chng_passwd_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.settings_chng_passwd_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        #if QT_CONFIG(shortcut)
        self.settings_chng_passwd_pushButton_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_chng_passwd_label_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.settings_chng_passwd_toolButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.settings_chng_passwd_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.settings_chng_passwd_lineEdit.setText("")
        self.settings_chng_passwd_label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.settings_chng_passwd_lineEdit_2.setText("")


    def settings_chng_info_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 548)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -10, 481, 611))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.settings_chng_info_label = QLabel(self.frame)
        self.settings_chng_info_label.setObjectName(u"label")
        self.settings_chng_info_label.setGeometry(QRect(160, 40, 181, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.settings_chng_info_label.setFont(font1)
        self.settings_chng_info_label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.settings_chng_info_pushButton_2 = QPushButton(self.frame)
        self.settings_chng_info_pushButton_2.setObjectName(u"pushButton_2")
        self.settings_chng_info_pushButton_2.setGeometry(QRect(120, 490, 251, 41))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.settings_chng_info_pushButton_2.setFont(font2)
        self.settings_chng_info_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_chng_info_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.settings_chng_info_pushButton_2.setCheckable(False)
        self.settings_chng_info_pushButton_2.setAutoDefault(False)
        self.settings_chng_info_pushButton_2.hide()

        self.settings_chng_info_label_3 = QLabel(self.frame)
        self.settings_chng_info_label_3.setObjectName(u"label_3")
        self.settings_chng_info_label_3.setGeometry(QRect(160, 90, 181, 31))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(17)
        self.settings_chng_info_label_3.setFont(font3)
        self.settings_chng_info_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_chng_info_lineEdit = QLineEdit(self.frame)
        self.settings_chng_info_lineEdit.setObjectName(u"lineEdit")
        self.settings_chng_info_lineEdit.setGeometry(QRect(160, 190, 181, 31))
        font4 = QFont()
        font4.setFamily(u"Gill Sans")
        font4.setPointSize(8)
        self.settings_chng_info_lineEdit.setFont(font4)
        self.settings_chng_info_lineEdit.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                    "border: 2px solid rgb(53, 53, 173, 1);\n"
                                    "border-radius: 15;\n"
                                    "color: black")
        self.settings_chng_info_lineEdit.setAlignment(Qt.AlignCenter)
        self.settings_chng_info_lineEdit.setPlaceholderText("Sneaky pass")
        self.settings_chng_info_lineEdit.setMaxLength(24)
        my_regex = QRegExp("^[a-zA-Z0-9_-]+$")
        my_validator = QRegExpValidator(my_regex, self.settings_chng_info_lineEdit)
        self.settings_chng_info_lineEdit.setValidator(my_validator)
        self.settings_chng_info_lineEdit.setDisabled(True)


        self.settings_chng_info_lineEdit_3 = QLineEdit(self.frame)
        self.settings_chng_info_lineEdit_3.setObjectName(u"lineEdit_3")
        self.settings_chng_info_lineEdit_3.setGeometry(QRect(160, 370, 181, 31))
        self.settings_chng_info_lineEdit_3.setFont(font4)
        self.settings_chng_info_lineEdit_3.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.settings_chng_info_lineEdit_3.setAlignment(Qt.AlignCenter)
        self.settings_chng_info_lineEdit_3.hide()

        self.settings_chng_info_lineEdit_4 = QLineEdit(self.frame)
        self.settings_chng_info_lineEdit_4.setObjectName(u"lineEdit_4")
        self.settings_chng_info_lineEdit_4.setGeometry(QRect(160, 280, 181, 31))
        self.settings_chng_info_lineEdit_4.setFont(font4)
        self.settings_chng_info_lineEdit_4.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.settings_chng_info_lineEdit_4.setAlignment(Qt.AlignCenter)
        self.settings_chng_info_lineEdit_4.setPlaceholderText("Sneaky pass")
        self.settings_chng_info_lineEdit_4.setMaxLength(29)
        my_regex_4 = QRegExp("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$")
        my_validator_4 = QRegExpValidator(my_regex_4, self.settings_chng_info_lineEdit_4)
        self.settings_chng_info_lineEdit_4.setValidator(my_validator_4)
        self.settings_chng_info_lineEdit_4.setDisabled(True)

        self.settings_chng_info_label_4 = QLabel(self.frame)
        self.settings_chng_info_label_4.setObjectName(u"label_4")
        self.settings_chng_info_label_4.setGeometry(QRect(210, 240, 101, 31))
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(21)
        font5.setBold(False)
        font5.setWeight(50)
        self.settings_chng_info_label_4.setFont(font5)
        self.settings_chng_info_label_4.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_chng_info_label_5 = QLabel(self.frame)
        self.settings_chng_info_label_5.setObjectName(u"label_5")
        self.settings_chng_info_label_5.setGeometry(QRect(190, 330, 131, 31))
        self.settings_chng_info_label_5.setFont(font5)
        self.settings_chng_info_label_5.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_chng_info_label_5.hide()

        self.settings_chng_info_label_6 = QLabel(self.frame)
        self.settings_chng_info_label_6.setObjectName(u"label_6")
        self.settings_chng_info_label_6.setGeometry(QRect(210, 150, 101, 31))
        self.settings_chng_info_label_6.setFont(font5)
        self.settings_chng_info_label_6.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.settings_chng_info_toolButton = QToolButton(self.frame)
        self.settings_chng_info_toolButton.setObjectName(u"toolButton")
        self.settings_chng_info_toolButton.setGeometry(QRect(30, 30, 31, 31))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        self.settings_chng_info_toolButton.setFont(font6)
        self.settings_chng_info_toolButton.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.settings_chng_info_frame_2 = QFrame(self.centralwidget)
        self.settings_chng_info_frame_2.setObjectName(u"frame_2")
        self.settings_chng_info_frame_2.setGeometry(QRect(19, 80, 421, 2))
        self.settings_chng_info_frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.settings_chng_info_frame_2.setFrameShape(QFrame.StyledPanel)
        self.settings_chng_info_frame_2.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.settings_chng_info_retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def settings_chng_info_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Настройки - Личная информация", None))
        self.settings_chng_info_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.settings_chng_info_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        #if QT_CONFIG(shortcut)
        self.settings_chng_info_pushButton_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.settings_chng_info_label_3.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.settings_chng_info_lineEdit.setText("")
        self.settings_chng_info_lineEdit_3.setText("")
        self.settings_chng_info_lineEdit_4.setText("")
        self.settings_chng_info_label_4.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.settings_chng_info_label_5.setText(QCoreApplication.translate("MainWindow", u"\u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.settings_chng_info_label_6.setText(QCoreApplication.translate("MainWindow", u"Логин", None))
        self.settings_chng_info_toolButton.setText(QCoreApplication.translate("MainWindow", u"<", None))




class Ui_popup(object):
    def setupUi(self, popup):
        if not popup.objectName():
            popup.setObjectName(u"popup")
        popup.resize(271, 151)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        popup.setFont(font)
        self.centralwidget = QWidget(popup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, -10, 291, 181))
        self.widget.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 50, 251, 2))
        self.frame_2.setStyleSheet(u"background-color: rgba(53, 53, 173, 1)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 131, 21))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgba(53, 53, 173, 1)")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 70, 131, 31))
        font2 = QFont()
        font2.setFamily(u"Gill Sans")
        font2.setPointSize(8)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                    "border: 2px solid rgb(53, 53, 173, 1);\n"
                                    "border-radius: 15;\n"
                                    "color: black")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setMaxLength(24)
        my_regex_3 = QRegExp("^[a-zA-Z0-9!_-]+$")
        my_validator_3 = QRegExpValidator(my_regex_3, self.lineEdit)
        self.lineEdit.setValidator(my_validator_3)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 110, 91, 41))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton.setFont(font3)
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton")
        self.pushButton_2.setGeometry(QRect(700, 110, 91, 41))
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDisabled(True)
        self.pushButton_2.hide()


        popup.setCentralWidget(self.centralwidget)

        self.retranslateUi(popup)

        QMetaObject.connectSlotsByName(popup)
    # setupUi

    def retranslateUi(self, popup):
        popup.setWindowTitle(QCoreApplication.translate("popup", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("popup", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0434", None))
        self.lineEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("popup", u"\u0412\u043e\u0439\u0442\u0438", None))
        #if QT_CONFIG(shortcut)
        self.pushButton.setShortcut("")
        self.pushButton_2.setText(QCoreApplication.translate("popup", u"\u0412\u043e\u0439\u0442\u0438", None))
        #if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut("")

    def server_setupUi(self, popup):
        if not popup.objectName():
            popup.setObjectName(u"popup")
        popup.resize(468, 540)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(16)
        popup.setFont(font)
        self.centralwidget = QWidget(popup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -10, 481, 611))
        self.frame.setStyleSheet(u"background-color: rgba(247, 247, 235, 1)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.server_label_2 = QLabel(self.frame)
        self.server_label_2.setObjectName(u"label_2")
        self.server_label_2.setGeometry(QRect(210, 50, 71, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.server_label_2.setFont(font1)
        self.server_label_2.setTabletTracking(False)
        self.server_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.server_label_3 = QLabel(self.frame)
        self.server_label_3.setObjectName(u"label_3")
        self.server_label_3.setGeometry(QRect(210, 130, 81, 71))
        self.server_label_3.setFont(font1)
        self.server_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.server_lineEdit_4 = QLineEdit(self.frame)
        self.server_lineEdit_4.setObjectName(u"lineEdit_4")
        self.server_lineEdit_4.setGeometry(QRect(150, 280, 181, 31))
        font2 = QFont()
        font2.setFamily(u"Gill Sans")
        font2.setPointSize(8)
        self.server_lineEdit_4.setFont(font2)
        self.server_lineEdit_4.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.server_lineEdit_4.setAlignment(Qt.AlignCenter)
        self.server_lineEdit_4.setPlaceholderText("Sneaky pass")

        self.server_lineEdit_3 = QLineEdit(self.frame)
        self.server_lineEdit_3.setObjectName(u"lineEdit_3")
        self.server_lineEdit_3.setGeometry(QRect(150, 370, 181, 31))
        self.server_lineEdit_3.setFont(font2)
        self.server_lineEdit_3.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.server_lineEdit_3.setAlignment(Qt.AlignCenter)
        self.server_lineEdit_3.setEchoMode(QLineEdit.Password)
        self.server_lineEdit_3.setPlaceholderText("Sneaky pass")

        self.server_label_5 = QLabel(self.frame)
        self.server_label_5.setObjectName(u"label_5")
        self.server_label_5.setGeometry(QRect(190, 330, 111, 31))
        self.server_label_5.setFont(font1)
        self.server_label_5.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.server_label_6 = QLabel(self.frame)
        self.server_label_6.setObjectName(u"label_6")
        self.server_label_6.setGeometry(QRect(200, 240, 91, 31))
        self.server_label_6.setFont(font1)
        self.server_label_6.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
        self.server_toolButton = QToolButton(self.frame)
        self.server_toolButton.setObjectName(u"toolButton")
        self.server_toolButton.setGeometry(QRect(30, 30, 31, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.server_toolButton.setFont(font3)
        self.server_toolButton.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.server_toolButton.hide()
        self.server_toolButton.setDisabled(True)


        self.server_lineEdit = QLineEdit(self.centralwidget)
        self.server_lineEdit.setObjectName(u"lineEdit")
        self.server_lineEdit.setGeometry(QRect(140, 90, 181, 31))
        self.server_lineEdit.setFont(font2)
        self.server_lineEdit.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                    "border: 2px solid rgb(53, 53, 173, 1);\n"
                                    "border-radius: 15;\n"
                                    "color: black")
        self.server_lineEdit.setAlignment(Qt.AlignCenter)
        self.server_lineEdit.setPlaceholderText("Sneaky pass")

        self.server_lineEdit_2 = QLineEdit(self.centralwidget)
        self.server_lineEdit_2.setObjectName(u"lineEdit_2")
        self.server_lineEdit_2.setGeometry(QRect(140, 180, 181, 31))
        self.server_lineEdit_2.setFont(font2)
        self.server_lineEdit_2.setStyleSheet(u"background-color: rgb(247,247,242);\n"
                                      "border: 2px solid rgb(53, 53, 173, 1);\n"
                                      "border-radius: 15;\n"
                                      "color: black")
        self.server_lineEdit_2.setAlignment(Qt.AlignCenter)
        self.server_lineEdit_2.setPlaceholderText("Sneaky pass")

        self.server_pushButton = QPushButton(self.centralwidget)
        self.server_pushButton.setObjectName(u"pushButton")
        self.server_pushButton.setGeometry(QRect(110, 430, 241, 41))
        self.server_pushButton.setFont(font1)
        self.server_pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.server_pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	color: white;\n"
                                      "	background-color: rgba(53, 53, 173, 1);\n"
                                      "	border-radius: 20;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton: pressed {\n"
                                      "\n"
                                      "	background-color: rgba(0, 255, 255, 144)\n"
                                      "}")
        self.server_pushButton.setCheckable(False)
        self.server_pushButton.setAutoDefault(False)
        self.server_pushButton_2 = QPushButton(self.centralwidget)
        self.server_pushButton_2.setObjectName(u"pushButton_2")
        self.server_pushButton_2.setGeometry(QRect(140, 480, 181, 41))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setWeight(75)
        self.server_pushButton_2.setFont(font4)
        self.server_pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.server_pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "	color: white;\n"
                                        "	background-color: rgba(53, 53, 173, 1);\n"
                                        "	border-radius: 20;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton: pressed {\n"
                                        "\n"
                                        "	background-color: rgba(0, 255, 255, 144)\n"
                                        "}")
        self.server_pushButton_2.setCheckable(False)
        self.server_pushButton_2.setAutoDefault(False)
        self.server_pushButton_2.hide()
        self.server_pushButton_2.setDisabled(True)

        popup.setCentralWidget(self.centralwidget)

        self.server_retranslateUi(popup)

        QMetaObject.connectSlotsByName(popup)
    # setupUi

    def server_retranslateUi(self, popup):
        popup.setWindowTitle(QCoreApplication.translate("popup", u"Подключение к серверу", None))
        self.server_label_2.setText(QCoreApplication.translate("popup", u"\u041f\u043e\u0440\u0442", None))
        self.server_label_3.setText(QCoreApplication.translate("popup", u"\u0410\u0439\u043f\u0438", None))
        self.server_label_5.setText(QCoreApplication.translate("popup", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.server_label_6.setText(QCoreApplication.translate("popup", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.server_toolButton.setText(QCoreApplication.translate("popup", u"<", None))
        self.server_lineEdit.setText("")
        self.server_pushButton.setText(QCoreApplication.translate("popup", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        #if QT_CONFIG(shortcut)
        self.server_pushButton.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.server_pushButton_2.setText(QCoreApplication.translate("popup", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        #if QT_CONFIG(shortcut)
        self.server_pushButton_2.setShortcut("")

