### In this file i save a lot of small instruments

#resolution
from screeninfo import get_monitors
import ctypes
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from code_decode import *
from bd_deistv import *
import time
import re
import os

def get_resoluton():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    #screensize2 = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    #print(screensize, '\n', screensize2)

    #for m in get_monitors():
        #print(str(m))

    return screensize[0],screensize[1]

def exists_settings():
    if not os.path.isfile('settings.txt'):
        with open('settings.txt', 'w') as file:
            count = 0
            for line in range(4):
                if count == 0:
                    file.write('0' + '\n')
                elif count == 1:
                    file.write('1' + '\n')
                elif count == 2:
                    file.write('2' + '\n')
                else:
                    pass
                count += 1


def zagr_settings(str):
    file_read = open('settings.txt', 'r')
    file = file_read.read()
    file = file.split('\n')
    file_read.close()
    return file[int(str)]

def redact_settings(num_str, new_str):
    with open('settings.txt', 'r') as f1, open('temp.txt', 'w') as f2:
        lines = f1.readlines()
        count = 0
        for line in lines:
            line = line.strip()
            #print(line)
            if count == num_str:
                f2.write(new_str + '\n')
            else:
                f2.write(line + '\n')
            count += 1
    os.remove('settings.txt')
    os.rename('temp.txt', 'settings.txt')
    return True
class Use_screen_settings(object):
    WIDTH, HEIGHT = get_resoluton()
    WIDTH_window, HEIGHT_window = int(WIDTH//2.95), int(HEIGHT//1.42)
    # def __init__(self):
    #     self.WIDTH, self.HEIGHT = get_resoluton()
    def take_resolution(self):
        return self.WIDTH, self.HEIGHT
    def take_width(self):
        return self.WIDTH
    def take_height(self):
        return self.HEIGHT
    def take_resolution_window(self):
        return self.WIDTH_window, self.HEIGHT_window
    def take_width_window(self):
        return self.WIDTH_window
    def take_height_window(self):
        return self.HEIGHT_window

class maska_shablon(object):

    def loginus(self, obj):
        dlina = 6
        #str3 = 'a'
        sovp_dlin = False
        maska_rez = False
        if len(obj) >= dlina:
            sovp_dlin = True
        maska_rez = re.search("^[a-zA-Z0-9_-]+$", obj)
        return sovp_dlin and maska_rez

    def parolus(self, obj):
        dlina = 6
        sovp_dlin = False
        maska_rez = False
        if len(obj) >= dlina:
            sovp_dlin = True
        maska_rez = re.search("^[a-zA-Z0-9!_-]+$", obj)
        return sovp_dlin and maska_rez

    def emailus(self, obj):
        dlina = 6
        sovp_dlin = False
        maska_rez = False
        if len(obj) >= dlina:
            sovp_dlin = True
        maska_rez = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$", obj)
        return sovp_dlin and maska_rez

    def loginus_site(self, obj):
        dlina = 1
        sovp_dlin = False
        maska_rez = False
        if len(obj) >= dlina:
            sovp_dlin = True
        # maska_rez = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$", obj)
        # str = "^[a-zA-Z0-9@._-]+$"
        return sovp_dlin

    def nazvus_site(self, obj):
        dlina = 1
        sovp_dlin = False
        maska_rez = False
        if len(obj) >= dlina:
            sovp_dlin = True
        # maska_rez = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$", obj)
        # str = "^[а-яА-Яa-zA-Z0-9._-]+$"
        return sovp_dlin

    def parolus_site(self, obj):
        dlina = 1
        sovp_dlin = False
        maska_rez = False
        if len(obj) >= dlina:
            sovp_dlin = True
        # maska_rez = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$", obj)
        # rez2 = re.search("^[a-zA-Z0-9!_-]+$", str2)
        return sovp_dlin