import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
#from sneakyapp1 import Ui_MainWindow
#   from sneakyapp import Ui_MainWindow
from all_windows import *

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()

        self.bd_super = Svyaz_s_bd()

        self.id = False
        #1800
        self.time_wait = 1800
        self.time_nachalo = time.time()
        # self.popupus_waiting = False

        exists_settings()


        if zagr_settings(2) == Cripta.hasher(Cripta, 'Yes'):
            self.popupus_waiting = True
        else:
            self.popupus_waiting = False

        self.popup_enter_chng_info = False
        self.pin_enabled_for_id = False
        #self.pincode = '0'
        try:
            if len(zagr_settings(1)) < 2:
                #self.pincode = zagr_settings(1)
                redact_settings(1, Cripta.hasher(Cripta, '0'))
        except Exception as error:
            print(error, '123')
        self.start_gui()


    def closeEvent(self, e):
        self.popup_ui.not_exit_from_window = False
        self.popup_ui.close()
        if self.bd_super.connection:
            self.bd_super.konec_raboty()
            self.bd_super.connection.close()
        #e.ignore()
        #sys.exit(self.exec())


    def start_gui(self):

        #self.bd_super.connect(zagr_settings(0),zagr_settings(1),zagr_settings(2),zagr_settings(3),zagr_settings(4))
        self.bd_super.auto_conn()


        if self.bd_super.connection:
            #print('ok')
            self.login_first_log()
        else:

            self.popup_ui = popup_windows()
            self.popup_ui.server_error = True
            self.popup_ui.ui.server_setupUi(self.popup_ui)
            self.popup_ui.setMaximumSize(468, 540)
            self.popup_ui.setMinimumSize(468, 540)
            self.popup_ui.enabled_exit()

            self.popup_ui.ui.server_lineEdit.setText(self.bd_super.port)
            self.popup_ui.ui.server_lineEdit_2.setText(self.bd_super.address)

            self.popup_ui.ui.server_pushButton.clicked.connect(self.start_gui_2)



            self.popup_ui.show()
            #print('ne ok')

    def start_gui_2(self):
        port = self.popup_ui.ui.server_lineEdit.text()
        ip = self.popup_ui.ui.server_lineEdit_2.text()
        login = self.popup_ui.ui.server_lineEdit_4.text()
        passwd = self.popup_ui.ui.server_lineEdit_3.text()

        self.bd_super.connect(login, passwd, ip, port, self.bd_super.database)
        #self.bd_super.auto_conn()


        if self.bd_super.connection:
            #print('ok')
            self.popup_ui.server_error = False
            self.popup_ui.close()
            self.login_first_log()
        else:

            self.start_gui()
            #print('ne ok')



    def waiting_popup(self):
        if self.popupus_waiting:
            if self.time_wait < (time.time() - self.time_nachalo):
                self.popup_pincode()

    def showdialog(self):
        dlg = QDialog()
        b1 = QPushButton("ok",dlg)
        b1.move(50,50)
        dlg.setWindowTitle("Dialog")
        b1.clicked.connect(lambda : dlg.close())
        dlg.setWindowModality(Qt.ApplicationModal)
        dlg.exec_()

    def popup_pincode(self):
        self.popup_ui = popup_windows()
        self.popup_ui.show()
        try:
            #print(self.popup_ui.closeEvent())
            self.popup_ui.ui.pushButton.clicked.connect(lambda: self.popup_unblock())
            self.popup_ui.ui.lineEdit.setMaxLength(8)
            #self.popup_ui.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            self.setDisabled(True)

        except Exception as error:
            print(error)

    def popup_unblock(self):
        pin = self.popup_ui.ui.lineEdit.text()
        #print(pin)
        self.time_nachalo = time.time()
        if Cripta.hasher(Cripta, str(pin)) == zagr_settings(1):
            self.popup_ui.not_exit_from_window = False
            self.popup_ui.close()
            self.setDisabled(False)
        else:
            self.setDisabled(False)
            self.popup_ui.not_exit_from_window = False
            self.popup_ui.close()
            self.login_first_log()

    def error_popup(self, type_er):
        #print(type_er)
        pass

    def login_first_log(self):
        try:
            self.bd_super.konec_raboty()
            self.table = ''
            self.ui.login_setupUi(self)

            self.ui.login_label_4.hide()
            self.ui.login_pushButton.clicked.connect(lambda: self.login_bd())

            self.ui.login_pushButton_2.clicked.connect(lambda: self.reg_first())
        except Exception as error:
            print("Ошибка:", error)

    def login_bd(self):

        try:
            passwrd = Cripta.hasher(Cripta, self.ui.login_lineEdit_2.text())

            #passwrd = self.ui.login_lineEdit_2.text()
            #print(passwrd)
        except Exception as error:
            print(error)
        result = self.bd_super.login_user(self.ui.login_lineEdit.text(), passwrd)
        if result:
            #print(result, ' id hash')
            self.id = result
            try:
                self.hash_super = Cripta.hasher(Cripta, (self.ui.login_lineEdit_2.text()+ 'SALT'))
                self.time_nachalo = time.time()
                self.entrys_first_log()
            except Exception as error:
                print(error)
        else:
            result = self.bd_super.login_user(self.ui.login_lineEdit.text(), self.ui.login_lineEdit_2.text())
            if result:
                #print(result, ' id')
                self.id = result
                try:
                    self.hash_super = Cripta.hasher(Cripta, (self.ui.login_lineEdit_2.text()+ 'SALT'))
                    self.time_nachalo = time.time()
                    self.entrys_first_log()
                except Exception as error:
                    print(error)
            else:
                #print('popa')
                self.ui.login_label_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u043b\u043e\u0433\u0438\u043d \u0438\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c", None))
                self.ui.login_label_4.show()

    def entrys_first_log(self):
        try:

            self.bd_super.start_paswd(self.id, self.hash_super)


            self.pin_enabled_for_id = redact_settings(0, Cripta.hasher(Cripta, str(self.id)))
            self.waiting_popup()

            self.entrys_perelist_true = False

            self.ui.entrys_all_setupUi(self)

            self.ui.entrys_all_pushButton.clicked.connect(lambda: self.new_entry())

            #self.ui.entrys_all_pushButton.hide()
            self.table = self.bd_super.show_zap(self.id)



            self.super_table = self.table
            self.count_lang = len(self.table)
            self.zap_na_str = 7
            self.count_str = self.count_lang // self.zap_na_str
            self.count_ost = self.count_lang - self.count_str * self.zap_na_str
            if self.count_ost == 0:
                self.count_str -= 1


            # print(self.count_lang, ' Записей')
            # print(self.count_str, ' Страниц')
            # print(self.count_ost, ' Оставшихся')
            self.ui.entrys_all_toolButton.clicked.connect(lambda: self.settings())



            self.ui.entrys_all_verticalLayoutWidget_2 = QWidget(self.ui.entrys_all_frame_3)
            self.ui.entrys_all_verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
            self.ui.entrys_all_verticalLayoutWidget_2.setGeometry(QRect(70, 100, 331, 311))
            self.ui.entrys_all_verticalLayout_2 = QVBoxLayout(self.ui.entrys_all_verticalLayoutWidget_2)
            self.ui.entrys_all_verticalLayout_2.setObjectName(u"verticalLayout_2")
            self.ui.entrys_all_verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            font2 = QFont()
            font2.setFamily(u"Century Gothic")
            font2.setPointSize(22)
            font2.setBold(True)
            font2.setWeight(75)


            if self.count_str > 0:
                self.count_stran_now = 0
                def perelist(str_now, col_na_str):



                    self.ui.entrys_all_pushButton_14.setText(str(str_now + 1))
                    pushbuttons = []

                    zap_now = str_now * col_na_str
                    #print(zap_now)
                    count = 0
                    for zap in self.super_table[zap_now: zap_now + col_na_str]:
                        pushbuttons.append('')
                    #print(pushbuttons)
                    for zapis in self.super_table[zap_now: zap_now + col_na_str]:

                        pushbuttons[count] = QPushButton(self.ui.entrys_all_verticalLayoutWidget_2)
                        # objectname = u'a' + zapis[1]
                        # print(objectname)
                        pushbuttons[count].setObjectName(u"" + str(zapis[0]))
                        #pushbuttons[count].setObjectName(u"" + zapis[2].replace(' ',''))
                        pushbuttons[count].setFont(font2)
                        pushbuttons[count].setCursor(QCursor(Qt.ArrowCursor))
                        pushbuttons[count].setStyleSheet(u"QPushButton{\n"
                                                         "	color: white;\n"
                                                         "	background-color: rgba(53, 53, 173, 1);\n"
                                                         "	border-radius: 20;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QPushButton: pressed {\n"
                                                         "\n"
                                                         "	background-color: rgba(0, 255, 255, 144)\n"
                                                         "}")
                        #print(zapis)
                        pushbuttons[count].setText(zapis[1].replace(' ',''))
                        # for i in str(zap):
                        #     print(i)
                        #entrys_all_pushButton_7.setText(zapis[1])
                        pushbuttons[count].setCheckable(False)
                        pushbuttons[count].setAutoDefault(False)

                        #pushbuttons.append(entrys_all_pushButton_7)
                        pushbuttons[count].clicked.connect(self.obrabotka_entrys)
                        self.ui.entrys_all_verticalLayout_2.addWidget(pushbuttons[count])
                        #print(pushbuttons[count].text())
                        #
                        count += 1
                self.ui.entrys_all_pushButton_12.setObjectName('-1')
                self.ui.entrys_all_pushButton_13.setObjectName('1')
                perelist(self.count_stran_now, self.zap_na_str)
                self.ui.entrys_all_pushButton_12.clicked.connect(self.entrys_perelist)
                self.ui.entrys_all_pushButton_13.clicked.connect(self.entrys_perelist)


            #print(self.count_str)
            if self.count_str < 1:
                self.entrys_perelist_true = False
                pushbuttons = []

                count = 0
                for zap in self.table:
                    pushbuttons.append('')
                #print(pushbuttons)
                for zapis in self.table:

                    pushbuttons[count] = QPushButton(self.ui.entrys_all_verticalLayoutWidget_2)
                    # objectname = u'a' + zapis[1]
                    # print(objectname)
                    pushbuttons[count].setObjectName(u"" + str(zapis[0]))
                    #pushbuttons[count].setObjectName(u"" + zapis[2].replace(' ',''))
                    pushbuttons[count].setFont(font2)
                    pushbuttons[count].setCursor(QCursor(Qt.ArrowCursor))
                    pushbuttons[count].setStyleSheet(u"QPushButton{\n"
                                                               "	color: white;\n"
                                                               "	background-color: rgba(53, 53, 173, 1);\n"
                                                               "	border-radius: 20;\n"
                                                               "}\n"
                                                               "\n"
                                                               "QPushButton: pressed {\n"
                                                               "\n"
                                                               "	background-color: rgba(0, 255, 255, 144)\n"
                                                               "}")
                    #print(zapis)
                    pushbuttons[count].setText(zapis[1].replace(' ',''))
                    # for i in str(zap):
                    #     print(i)
                    #entrys_all_pushButton_7.setText(zapis[1])
                    pushbuttons[count].setCheckable(False)
                    pushbuttons[count].setAutoDefault(False)

                    #pushbuttons.append(entrys_all_pushButton_7)
                    pushbuttons[count].clicked.connect(self.obrabotka_entrys)
                    self.ui.entrys_all_verticalLayout_2.addWidget(pushbuttons[count])
                    #print(pushbuttons[count].text())
                    #
                    count += 1

                self.ui.entrys_all_pushButton_14.hide()
                self.ui.entrys_all_pushButton_13.hide()
                self.ui.entrys_all_pushButton_12.hide()


            # for i in pushbuttons:
            #     print(i.text())
            #     i.clicked.connect(lambda: print(count))
            #     count += 1


            #self.obrabotka_entrys(pushbuttons[count].text())

        except Exception as error:
            print(error)

    def entrys_perelist(self):
        self.waiting_popup()
        try:

            if self.sender():
                now = self.sender()


                deistvie = int(now.objectName())
                #print(now.text(), now.objectName())
        except:
            deistvie = 0
        self.entrys_perelist_true = True
        try:
            self.ui.entrys_all_setupUi(self)
            self.ui.entrys_all_pushButton.clicked.connect(lambda: self.new_entry())
            #self.ui.entrys_all_pushButton.hide()

            # print( self.count_lang, ' Записей')
            # print( self.count_str, ' Страниц')
            # print( self.count_ost, ' Оставшихся')
            self.ui.entrys_all_toolButton.clicked.connect(lambda: self.settings())


            self.ui.entrys_all_verticalLayoutWidget_2 = QWidget(self.ui.entrys_all_frame_3)
            self.ui.entrys_all_verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
            self.ui.entrys_all_verticalLayoutWidget_2.setGeometry(QRect(70, 100, 331, 311))
            self.ui.entrys_all_verticalLayout_2 = QVBoxLayout(self.ui.entrys_all_verticalLayoutWidget_2)
            self.ui.entrys_all_verticalLayout_2.setObjectName(u"verticalLayout_2")
            self.ui.entrys_all_verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            font2 = QFont()
            font2.setFamily(u"Century Gothic")
            font2.setPointSize(22)
            font2.setBold(True)
            font2.setWeight(75)


            if self.count_stran_now == 0 and deistvie == (-1):
                self.count_stran_now = self.count_str
            elif self.count_stran_now == self.count_str and deistvie == 1:
                self.count_stran_now = 0
            else:
                self.count_stran_now += deistvie

            self.ui.entrys_all_pushButton_14.setText(str(self.count_stran_now + 1))
            pushbuttons = []

            zap_now = self.count_stran_now * self.zap_na_str
            #print(zap_now)
            count = 0
            for zap in self.super_table[zap_now: zap_now + self.zap_na_str]:
                pushbuttons.append('')
            #print(pushbuttons)
            for zapis in self.super_table[zap_now: zap_now + self.zap_na_str]:

                pushbuttons[count] = QPushButton(self.ui.entrys_all_verticalLayoutWidget_2)
                # objectname = u'a' + zapis[1]
                # print(objectname)
                pushbuttons[count].setObjectName(u"" + str(zapis[0]))
                #pushbuttons[count].setObjectName(u"" + zapis[2].replace(' ',''))
                pushbuttons[count].setFont(font2)
                pushbuttons[count].setCursor(QCursor(Qt.ArrowCursor))
                pushbuttons[count].setStyleSheet(u"QPushButton{\n"
                                                 "	color: white;\n"
                                                 "	background-color: rgba(53, 53, 173, 1);\n"
                                                 "	border-radius: 20;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton: pressed {\n"
                                                 "\n"
                                                 "	background-color: rgba(0, 255, 255, 144)\n"
                                                 "}")
                #print(zapis)
                pushbuttons[count].setText(zapis[1].replace(' ',''))
                # for i in str(zap):
                #     print(i)
                #entrys_all_pushButton_7.setText(zapis[1])
                pushbuttons[count].setCheckable(False)
                pushbuttons[count].setAutoDefault(False)

                #pushbuttons.append(entrys_all_pushButton_7)
                pushbuttons[count].clicked.connect(self.obrabotka_entrys)
                self.ui.entrys_all_verticalLayout_2.addWidget(pushbuttons[count])
                #print(pushbuttons[count].text())
                #
                count += 1

            self.ui.entrys_all_pushButton_12.setObjectName('-1')
            self.ui.entrys_all_pushButton_13.setObjectName('1')
            self.ui.entrys_all_pushButton_12.clicked.connect(self.entrys_perelist)
            self.ui.entrys_all_pushButton_13.clicked.connect(self.entrys_perelist)


            #print(self.count_stran_now)




        except Exception as error:
            print(error)

    def obrabotka_entrys(self):
        obj = self.sender()
        #print('obj', obj.objectName())
        for zap in self.super_table:
            if int(zap[0]) == int(obj.objectName()):
                #print(zap)
                self.entrys_show(zap)
        
    def entrys_show(self, obj):
        try:
            self.waiting_popup()
            self.ui.entrys_show_setupUi(self)
            self.ui.entrys_show_toolButton_2.hide()
            #self.ui.entrys_show_pushButton.clicked.connect(lambda: self.showdialog())
            id_zap = (str(obj[0]))

            self.ui.entrys_show_pushButton_3.clicked.connect(lambda: self.chng_entry(id_zap))
            self.ui.entrys_show_pushButton.clicked.connect(lambda: self.bd_super.del_zap(id_zap))
            self.ui.entrys_show_pushButton.clicked.connect(lambda: self.entrys_first_log())
            if self.entrys_perelist_true:
                #self.ui.entrys_show_pushButton.clicked.connect(lambda: self.entrys_perelist())
                self.ui.entrys_show_pushButton_2.clicked.connect(lambda: self.entrys_perelist())
                #self.ui.entrys_show_pushButton_2.clicked.connect(lambda: print('nazad'))
            else:

                self.ui.entrys_show_pushButton_2.clicked.connect(lambda: self.entrys_first_log())
        except Exception as error:
            print(error)
        #print(obj.text(), obj.objectName())
        id = obj[0]
        nazv = obj[1].replace(' ', '')
        log = obj[2]
        #parol = obj[3].replace(' ', '')
        parol = self.bd_super.deshifrator(self.id, id)
        #parol = obj[3].replace(' ', '')
        #print(id, nazv, log, parol)
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sneaky Pass - Просмотр записи - " + nazv, None))
        self.ui.entrys_show_label.setText(log)
        #print('*' * len(parol))
        self.ui.entrys_show_label_2.setText('*******')
        #self.ui.entrys_show_label_2.setText('*' * len(parol))
        #self.ui.entrys_show_label_2.setText(parol)

        self.ui.entrys_show_toolButton.clicked.connect(lambda: self.copy_buff(parol))

    def copy_buff(self, parol):
        self.waiting_popup()

        QApplication.clipboard().setText(parol)

    def chng_entry(self, id_zap):
        self.popup_ui = popup_windows()
        self.popup_ui.show()
        self.popup_enter_chng_info = True
        try:
            try:
                if self.popup_enter_chng_info:
                    #self.ui.entrys_show_pushButton_3.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.entrys_show_pushButton_2.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.entrys_show_pushButton.clicked.connect(lambda: self.popup_ui.close())
            except:
                print('error')
            #print(id_zap)
            self.popup_ui.enabled_exit()
            #print(self.popup_ui.closeEvent())
            #self.popup_ui.ui.pushButton.clicked.connect(self.popup_ui.enabled_exit)
            self.popup_ui.setWindowTitle('Изменение записи')
            self.popup_ui.ui.label.setGeometry(QRect(20, 20, 250, 21))
            self.popup_ui.ui.label.setText(' Что хотите поменять?')
            self.popup_ui.ui.pushButton.clicked.connect(lambda: self.chng_entry_log_pass(id_zap, 'log'))
            self.popup_ui.ui.pushButton.setGeometry(QRect(20, 95, 91, 41))
            self.popup_ui.ui.pushButton.setText('Логин')

            self.popup_ui.ui.pushButton_2.clicked.connect(lambda: self.chng_entry_log_pass(id_zap, 'pass'))
            self.popup_ui.ui.pushButton_2.setGeometry(QRect(180, 95, 91, 41))
            self.popup_ui.ui.pushButton_2.show()
            self.popup_ui.ui.pushButton_2.setDisabled(False)
            self.popup_ui.ui.pushButton_2.setText('Пароль')

            self.popup_ui.ui.lineEdit.setDisabled(True)
            self.popup_ui.ui.lineEdit.hide()

            #self.popup_ui.ui.lineEdit.setMaxLength(8)
            #self.popup_ui.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            #self.setDisabled(True)

        except Exception as error:
            print(error)

    def chng_entry_log_pass(self, id_zap, choise):
        if choise == 'log':
            self.popup_ui.setWindowTitle('Изменение логина записи')

            self.popup_ui.ui.label.setText('  Введите новый логин')

            self.popup_ui.ui.lineEdit.setEchoMode(False)
            self.popup_ui.ui.lineEdit.setPlaceholderText("Sneaky pass")
            self.popup_ui.ui.lineEdit.setMaxLength(19)
            my_regex = QRegExp("^[a-zA-Z0-9@._-]+$")
            my_validator = QRegExpValidator(my_regex, self.popup_ui.ui.lineEdit)
            self.popup_ui.ui.lineEdit.setValidator(my_validator)


            self.popup_ui.ui.lineEdit.setDisabled(False)
            self.popup_ui.ui.lineEdit.show()
            self.popup_ui.ui.lineEdit.setGeometry(QRect(60, 70, 172, 31))


            self.popup_ui.ui.pushButton.clicked.disconnect()

            self.popup_ui.ui.pushButton.clicked.connect(lambda: self.chng_entry_login_end(id_zap))
            self.popup_ui.ui.pushButton.setText('Применить')
            self.popup_ui.ui.pushButton.setGeometry(QRect(85, 110, 121, 41))
            self.popup_ui.ui.pushButton_2.setDisabled(True)
            self.popup_ui.ui.pushButton_2.hide()
            self.popup_ui.ui.pushButton_2.setGeometry(QRect(700, 95, 91, 41))

            #print('login', id_zap)
        elif choise == 'pass':
            self.popup_ui.setWindowTitle('Изменение пароля записи')

            self.popup_ui.ui.label.setText('Введите новый пароль')

            self.popup_ui.ui.lineEdit.setEchoMode(QLineEdit.Password)
            self.popup_ui.ui.lineEdit.setPlaceholderText("Sneaky pass")
            self.popup_ui.ui.lineEdit.setMaxLength(19)
            my_regex = QRegExp("^[a-zA-Z0-9!_-]+$")
            my_validator = QRegExpValidator(my_regex, self.popup_ui.ui.lineEdit)
            self.popup_ui.ui.lineEdit.setValidator(my_validator)

            self.popup_ui.ui.lineEdit.setDisabled(False)
            self.popup_ui.ui.lineEdit.show()
            self.popup_ui.ui.lineEdit.setGeometry(QRect(60, 70, 172, 31))

            self.popup_ui.ui.pushButton.clicked.disconnect()
            self.popup_ui.ui.pushButton.clicked.connect(lambda: self.chng_entry_pass_end(id_zap))
            self.popup_ui.ui.pushButton.setText('Применить')
            self.popup_ui.ui.pushButton.setGeometry(QRect(85, 110, 121, 41))
            self.popup_ui.ui.pushButton_2.setDisabled(True)
            self.popup_ui.ui.pushButton_2.hide()
            self.popup_ui.ui.pushButton_2.setGeometry(QRect(700, 95, 91, 41))

            #print('login', id_zap)

    def chng_entry_login_end(self, id_zap):
        try:
            new_info = self.popup_ui.ui.lineEdit.text()
            new_info_log_prov = maska_shablon.loginus_site(maska_shablon, new_info)
            if not new_info_log_prov:
                self.popup_ui.ui.label.setText('  Логин не подходит')
            else:
                self.bd_super.edit_log_zap(self.id,id_zap, new_info)
                self.popup_ui.close()
                self.entrys_first_log()
                # self.entrys_first_log()
        except Exception as error:
            print(error)

    def chng_entry_pass_end(self, id_zap):
        try:
            new_info = self.popup_ui.ui.lineEdit.text()
            new_info_log_prov = maska_shablon.parolus_site(maska_shablon, new_info)
            if not new_info_log_prov:
                self.popup_ui.ui.label.setText('  Пароль не подходит')
            else:
                self.bd_super.edit_pass_zap(self.id,id_zap, new_info)
                self.popup_ui.close()
                self.entrys_first_log()
        except Exception as error:
            print(error)

    def new_entry(self):
        self.waiting_popup()
        self.ui.entrys_new_setupUi(self)
        self.ui.entrys_new_pushButton_2.clicked.connect(lambda: self.entrys_first_log())
        self.ui.entrys_new_pushButton.clicked.connect(lambda: self.new_entry_add())

    def new_entry_add(self):
        try:
            self.waiting_popup()


            prov_nazv = maska_shablon.nazvus_site(maska_shablon, self.ui.entrys_new_lineEdit_3.text())
            prov_log = maska_shablon.loginus_site(maska_shablon, self.ui.entrys_new_lineEdit.text())
            prov_par = maska_shablon.parolus_site(maska_shablon, self.ui.entrys_new_lineEdit_2.text())

            if prov_nazv:
                self.ui.entrys_new_label_4.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
            if prov_log:
                self.ui.entrys_new_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
            if prov_par:
                self.ui.entrys_new_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")

            if not prov_nazv or not prov_log or not prov_par:
                if not prov_nazv:
                    self.ui.entrys_new_label_4.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(149, 0, 0, 1)")
                    self.ui.entrys_new_label.setText('Безуспешно')
                if not prov_log:
                    self.ui.entrys_new_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(149, 0, 0, 1)")
                    self.ui.entrys_new_label.setText('Безуспешно')
                if not prov_par:
                    self.ui.entrys_new_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(149, 0, 0, 1)")
                    self.ui.entrys_new_label.setText('Безуспешно')

            else:
                # (u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
                #color: rgb(149, 0, 0) красный
                if prov_nazv:
                    self.ui.entrys_new_label_4.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
                if prov_log:
                    self.ui.entrys_new_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
                if prov_par:
                    self.ui.entrys_new_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")

                self.bd_super.add_zap(self.id, self.ui.entrys_new_lineEdit_3.text(), self.ui.entrys_new_lineEdit.text(), self.ui.entrys_new_lineEdit_2.text())

                self.ui.entrys_new_label.setText('   Успешно')
                self.ui.entrys_new_lineEdit.setText('')
                self.ui.entrys_new_lineEdit_2.setText('')
                self.ui.entrys_new_lineEdit_3.setText('')
        except Exception as error:
            self.ui.entrys_new_label.setText('Безуспешно')
            print(error)

    def btnClicked(self):
        #print('a')
        self.ui.login_label.setText("  Успешно!")
        self.ui.login_label.adjustSize()
        self.ui.reg_setupUi(self)
        self.ui.reg_pushButton_2.clicked.connect(lambda: self.btnClicked2())

    def reg_first(self):
        self.ui.reg_setupUi(self)
        self.ui.reg_pushButton.clicked.connect(lambda: self.reg_new())
        self.ui.reg_pushButton_2.clicked.connect(lambda: self.login_first_log())

    def reg_new(self):
        try:
            prov_logi = maska_shablon.loginus(maska_shablon, self.ui.reg_lineEdit.text())
            prov_pass1 = maska_shablon.parolus(maska_shablon, self.ui.reg_lineEdit_2.text())
            prov_pass2 = maska_shablon.parolus(maska_shablon, self.ui.reg_lineEdit_3.text())
            prov_email = maska_shablon.emailus(maska_shablon, self.ui.reg_lineEdit_4.text())

            prov_login_exists = self.bd_super.proverka_login(self.ui.reg_lineEdit.text())
            prov_email_exists = self.bd_super.proverka_email(self.ui.reg_lineEdit_4.text())
            #print(prov_login_exists)
            if prov_logi:
                self.ui.reg_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
            if prov_pass1:
                self.ui.reg_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
            if prov_pass2:
                self.ui.reg_label_5.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
            if prov_email:
                self.ui.reg_label_6.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")

            if not prov_logi or not prov_pass1 or not prov_pass2 or not prov_email:
                #print(prov_login_exists, prov_email_exists)
                if prov_login_exists or prov_email_exists:
                    if prov_login_exists:
                        self.ui.reg_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(149, 0, 0, 1)")
                        self.ui.reg_label.setText('Логин занят')
                    if prov_email_exists:
                        self.ui.reg_label_6.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(149, 0, 0, 1)")
                        self.ui.reg_label.setText('E-mail занят')
                    if prov_login_exists and prov_email_exists:
                        self.ui.reg_label.setText('Заняты')
                        self.ui.reg_label.setGeometry(QRect(210, 60, 255, 41))

                else:
                    self.ui.reg_label.setText('Регистрация')
                    if not prov_logi:
                        self.ui.reg_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(149, 0, 0, 1)")
                    if not prov_pass1:
                        self.ui.reg_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(149, 0, 0, 1)")
                    if not prov_pass2:
                        self.ui.reg_label_5.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(149, 0, 0, 1)")
                    if not prov_email:
                        self.ui.reg_label_6.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(149, 0, 0, 1)")



            else:
                # (u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
                #
                #color: rgb(149, 0, 0) красный
                if prov_logi:
                    self.ui.reg_label_2.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
                if prov_pass1:
                    self.ui.reg_label_3.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
                if prov_pass2:
                    self.ui.reg_label_5.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")
                if prov_email:
                    self.ui.reg_label_6.setStyleSheet(u"background-color: rgba(247, 247, 235, 1); color:rgba(53, 53, 173, 1)")

                #self.waiting_popup()
                if self.ui.reg_lineEdit_2.text() == self.ui.reg_lineEdit_3.text():
                    passwrd = Cripta.hasher(Cripta, self.ui.reg_lineEdit_2.text())
                    #passwrd = self.ui.reg_lineEdit_2.text()
                    self.bd_super.reg_polz(self.ui.reg_lineEdit.text(), passwrd, self.ui.reg_lineEdit_4.text())
                    self.login_first_log()
                    self.ui.login_label_4.setText('  Успешная регистрация')
                    self.ui.login_label_4.show()
                else:
                    self.ui.reg_label.setText('Пароли разные')

        except Exception as error:
            print(error)

    def settings(self):
        try:
            self.waiting_popup()
            self.ui.settings_setupUi(self)
            self.ui.settings_pushButton.hide()
            self.ui.settings_pushButton_2.clicked.connect(self.settings_exit_account)
            self.ui.settings_toolButton_2.clicked.connect(lambda: self.entrys_first_log())
            self.ui.settings_toolButton.hide()
            self.ui.settings_pushButton_6.clicked.connect(lambda: self.settings_server())
            self.ui.settings_pushButton_3.clicked.connect(lambda: self.settings_passwd_chng())
            self.ui.settings_pushButton_4.clicked.connect(lambda: self.settings_dannye())
            self.ui.settings_pushButton_5.clicked.connect(lambda: self.settings_security())
        except Exception as error:
            print(error)

    def settings_exit_account(self):
        self.popup_ui = popup_windows()
        self.popup_ui.show()
        self.popup_enter_chng_info = True
        try:
            try:
                if self.popup_enter_chng_info:
                    #self.ui.entrys_show_pushButton_3.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.settings_toolButton_2.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.settings_pushButton_6.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.settings_pushButton_3.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.settings_pushButton_4.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.settings_pushButton_5.clicked.connect(lambda: self.popup_ui.close())
            except:
                print('error')
            #print(id_zap)
            self.popup_ui.enabled_exit()
            #print(self.popup_ui.closeEvent())
            #self.popup_ui.ui.pushButton.clicked.connect(self.popup_ui.enabled_exit)
            self.popup_ui.setWindowTitle('Выход из аккаунта')
            self.popup_ui.ui.label.setGeometry(QRect(20, 20, 250, 21))
            self.popup_ui.ui.label.setText('Вы точно хотите выйти?')
            self.popup_ui.ui.pushButton.clicked.connect(lambda: self.login_first_log())
            self.popup_ui.ui.pushButton.clicked.connect(lambda: self.popup_ui.close())
            self.popup_ui.ui.pushButton.setText('Да')
            self.popup_ui.ui.pushButton.setGeometry(QRect(20, 95, 91, 41))

            self.popup_ui.ui.pushButton_2.clicked.connect(lambda: self.popup_ui.close())
            self.popup_ui.ui.pushButton_2.setGeometry(QRect(180, 95, 91, 41))
            self.popup_ui.ui.pushButton_2.show()
            self.popup_ui.ui.pushButton_2.setDisabled(False)
            self.popup_ui.ui.pushButton_2.setText('Отмена')

            self.popup_ui.ui.lineEdit.setDisabled(True)
            self.popup_ui.ui.lineEdit.hide()

            #self.popup_ui.ui.lineEdit.setMaxLength(8)
            #self.popup_ui.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            #self.setDisabled(True)

        except Exception as error:
            print(error)

    def settings_server(self):
        self.waiting_popup()
        self.ui.settings_server_setupUi(self)
        self.ui.settings_server_toolButton.hide()
        self.ui.settings_server_pushButton_2.clicked.connect(lambda: self.settings())

    def settings_passwd_chng(self):
        try:
            self.waiting_popup()
            self.ui.settings_chng_passwd_setupUi(self)
            self.ui.settings_chng_passwd_toolButton.clicked.connect(lambda: self.settings())
            self.ui.settings_chng_passwd_pushButton_2.clicked.connect(lambda: self.settings_passwd_chng_conec())
        except Exception as error:
            print(error)

    def settings_passwd_chng_conec(self):

        self.ui.settings_chng_passwd_label.setText('Настройки')
        proverka_vvoda = maska_shablon.parolus(maska_shablon, self.ui.settings_chng_passwd_lineEdit.text())
        if self.ui.settings_chng_passwd_lineEdit.text() == self.ui.settings_chng_passwd_lineEdit_2.text():
            if proverka_vvoda:
                passwrd = Cripta.hasher(Cripta, self.ui.settings_chng_passwd_lineEdit.text())
                self.settings_passwd_chng_popup(passwrd)

                #print('Меняем пароль. Понарошку')
            else:
                self.ui.settings_chng_passwd_label.setText('Не вышло')
        else:
            self.ui.settings_chng_passwd_label.setText('Пароли разные')
            #print('Либо пароли разные, либо хз')

    def settings_passwd_chng_popup(self, passwrd):
        self.popup_ui = popup_windows()
        self.popup_ui.show()
        self.popup_enter_chng_info = True
        try:
            try:
                if self.popup_enter_chng_info:
                    #self.ui.entrys_show_pushButton_3.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.settings_chng_passwd_toolButton.clicked.connect(lambda: self.popup_ui.close())
                    #self.ui.entrys_show_pushButton.clicked.connect(lambda: self.popup_ui.close())
            except:
                print('error')
            #print(id_zap)
            self.popup_ui.enabled_exit()
            #print(self.popup_ui.closeEvent())
            #self.popup_ui.ui.pushButton.clicked.connect(self.popup_ui.enabled_exit)
            self.popup_ui.setWindowTitle('Изменение пароля')
            self.popup_ui.ui.label.setGeometry(QRect(20, 20, 250, 21))
            self.popup_ui.ui.label.setText('Введите старый пароль')
            self.popup_ui.ui.pushButton.clicked.connect(lambda: self.settings_passwd_chng_popup_konec(passwrd))
            self.popup_ui.ui.pushButton.setText('Ввести')



            #self.popup_ui.ui.lineEdit.setMaxLength(8)
            #self.popup_ui.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            #self.setDisabled(True)

        except Exception as error:
            print(error)


    def settings_passwd_chng_popup_konec(self, passwrd):
        try:
            old_passwrd = self.popup_ui.ui.lineEdit.text()
            old_passwrd_1 = Cripta.hasher(Cripta, old_passwrd)
            dannye = self.bd_super.take_info(self.id)

            dannye = dannye[0]
            logi = dannye[1].replace(' ', '')

            otvet = self.bd_super.change_pass_user(self.id, logi, old_passwrd, passwrd)[0]
            otvet_2 = None
            #print(self.id, logi, old_passwrd, passwrd)
            if not otvet:
                otvet_2 = self.bd_super.change_pass_user(self.id, logi, old_passwrd_1, passwrd)[0]

            if otvet or otvet_2:
                self.settings_passwd_chng()
                self.ui.settings_chng_passwd_label_3.setText('Успешно')
                self.popup_ui.close()
            else:
                self.popup_ui.ui.label.setText('Неверный пароль')
            #print(otvet, otvet_2)
        except Exception as error:
            print(error)


    def settings_security(self):
        self.waiting_popup()
        self.ui.settings_sec_setupUi(self)
        self.ui.settings_sec_checkBox.setCheckState(self.popupus_waiting)
        if self.popupus_waiting == True:
            self.ui.settings_sec_checkBox.setCheckState(2)
            #print('da')
        if self.popupus_waiting == False:
            self.ui.settings_sec_checkBox.setCheckState(0)
            #print('net')
        self.ui.settings_sec_toolButton.clicked.connect(lambda: self.settings())
        self.ui.settings_sec_pushButton_2.clicked.connect(lambda: self.settings_security_save(self.ui.settings_sec_checkBox.checkState()))
        self.ui.settings_sec_pushButton_3.clicked.connect(self.settings_security_pin)
    def settings_security_save(self, check):
        self.ui.settings_sec_label.setText('Применено')
        if check == 2:
            redact_settings(2, Cripta.hasher(Cripta, 'Yes'))
            self.popupus_waiting = True
            #print(check, 'da')
        if check == 0:
            redact_settings(2, Cripta.hasher(Cripta, 'No'))
            self.popupus_waiting = False
            #print(check, 'net')

    def settings_security_pin(self):
        self.popup_ui = popup_windows()
        self.popup_ui.show()
        self.popup_enter_chng_info = True
        try:
            try:
                if self.popup_enter_chng_info:
                    #self.ui.entrys_show_pushButton_3.clicked.connect(lambda: self.popup_ui.close())
                    #self.ui.settings_chng_passwd_toolButton.clicked.connect(lambda: self.popup_ui.close())
                    #self.ui.entrys_show_pushButton.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.settings_sec_toolButton.clicked.connect(lambda: self.popup_ui.close())
                    self.ui.settings_sec_pushButton_2.clicked.connect(lambda: self.popup_ui.close())

            except:
                print('error')
            #print(id_zap)
            self.popup_ui.enabled_exit()
            #print(self.popup_ui.closeEvent())
            #self.popup_ui.ui.pushButton.clicked.connect(self.popup_ui.enabled_exit)
            self.popup_ui.setWindowTitle('Добавление пин-кода')
            self.popup_ui.ui.label.setGeometry(QRect(20, 20, 250, 21))
            self.popup_ui.ui.label.setText('          Введите пин')
            self.popup_ui.ui.pushButton.clicked.connect(lambda: self.settings_security_save_pin())
            self.popup_ui.ui.pushButton.setText('Ввести')
            self.popup_ui.ui.pushButton.setGeometry(QRect(20, 115, 91, 41))

            self.popup_ui.ui.pushButton_2.clicked.connect(lambda: self.popup_ui.close())
            self.popup_ui.ui.pushButton_2.setGeometry(QRect(180, 115, 91, 41))
            self.popup_ui.ui.pushButton_2.show()
            self.popup_ui.ui.pushButton_2.setDisabled(False)
            self.popup_ui.ui.pushButton_2.setText('Отмена')

            # self.popup_ui.ui.lineEdit.setDisabled(True)
            # self.popup_ui.ui.lineEdit.hide()


            #self.popup_ui.ui.lineEdit.setMaxLength(8)
            #self.popup_ui.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            #self.setDisabled(True)

        except Exception as error:
            print(error)

    def settings_security_save_pin(self):
        #self.pincode = self.popup_ui.ui.lineEdit.text()
        redact_settings(1, Cripta.hasher(Cripta, self.popup_ui.ui.lineEdit.text()))
        self.popup_ui.close()

    def settings_dannye(self):
        try:
            self.waiting_popup()
            self.ui.settings_chng_info_setupUi(self)
            dannye = self.bd_super.take_info(self.id)

            dannye = dannye[0]
            logi = dannye[1].replace(' ', '')
            email = dannye[3].replace(' ', '')
            #print(logi, email)
            self.ui.settings_chng_info_lineEdit.setPlaceholderText(logi)
            self.ui.settings_chng_info_lineEdit_4.setPlaceholderText(email)
            #(self.ui.settings_chng_info_lineEdit.placeholderText())
            self.ui.settings_chng_info_toolButton.clicked.connect(lambda: self.settings())
            self.ui.settings_chng_info_pushButton_2.clicked.connect(self.settings_dannye_save)
        except Exception as error:
            print(error)

    def settings_dannye_save(self):
        log_do = self.ui.settings_chng_info_lineEdit.placeholderText()
        email_do = self.ui.settings_chng_info_lineEdit_4.placeholderText()

        log_posle = self.ui.settings_chng_info_lineEdit.text()
        email_posle = self.ui.settings_chng_info_lineEdit_4.text()

        print(log_do, log_posle)
        print(email_do, email_posle)

class popup_windows(QtWidgets.QMainWindow):
    def __init__(self):
        super(popup_windows, self).__init__()
        self.ui = Ui_popup()
        self.ui.setupUi(self)
        self.setMinimumSize(271, 151)
        self.setMaximumSize(271, 151)
        self.setWindowTitle('Sneaky Pass')
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.not_exit_from_window = True
        self.server_error = False

    def closeEvent(self, e):
        if self.not_exit_from_window:
            e.ignore()
        if self.server_error:
            sys.exit(self.exec())

    def enabled_exit(self):
        self.not_exit_from_window = False
    def disabled_exit(self):
        self.not_exit_from_window = True


def start():
    app = QtWidgets.QApplication([])

    application = mywindow()
    application.setMinimumSize(463, 540)
    application.setMaximumSize(463, 540)
    #application.setMinimumSize(Use_screen_settings.take_width_window(Use_screen_settings), Use_screen_settings.take_height_window(Use_screen_settings))
    #application.setMaximumSize(Use_screen_settings.take_width_window(Use_screen_settings), Use_screen_settings.take_height_window(Use_screen_settings))
    application.setWindowTitle('Sneaky Pass')
    application.setWindowIcon(QIcon("icon.png"))
    application.show()
    sys.exit(app.exec())


