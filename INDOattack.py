#!/usr/bin/python
# -*- coding: utf-8 -*-
#####DONT CHANGE THIS########
import sys,os,platform
import time
from time import *
x = platform.system()
import requests
from tqdm import tqdm
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
#--- Color  ---#
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

now = strftime("%T")
bulan = strftime("%B")
tahun = strftime("%Y")
#--- Def menu ---#

os.system("clear")
def banner():
	print
print(""+R+"Please "+G+" Do NOT "+R+"use this tool for"+B+" illegal activity")
print(" [!] "+R+" Keep "+GR+"legal "+R+"don't illegal "+B+" [!]"+G+"")
print
os.system("pkg install wget")
os.system("pkg install python2")
os.system("rm -f /data/data/com.termux/files/usr/bin/INDOddos-Attack.py")
os.system("wget https://raw.githubusercontent.com/INDOnimous/INDOclon/master/INDOddos/INDOddos-Attack.py")
os.system("wget https://raw.githubusercontent.com/INDOnimous/INDOclon/master/INDOsee/tampil.py")
os.system("mv tampil.py /data/data/com.termux/files/usr/bin/")
os.system("mv INDOddos-Attack.py /data/data/com.termux/files/usr/bin/")
os.system("chmod +x /data/data/com.termux/files/usr/bin/INDOddos-Attack.py")
os.system("chmod +x /data/data/com.termux/files/usr/bin/tampil.py")
os.system("python2 /data/data/com.termux/files/usr/bin/INDOddos-Attack.py")
def banner():
	print
print(""+R+"Please "+G+" Do NOT "+R+"use this tool for"+B+" illegal activity")
print(" [!] "+R+" Keep "+GR+"legal "+R+"don't illegal "+B+" [!]"+G+"")
print

