#!/usr/bin/python
# coding=utf-8
#///.coded by Pangeran Alvins
import time
import os,sys
from my import see
from my import fbreport
from my import fbbrute
from my import wordlist
from my import banner
os.system("clear")

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

green = '\033[32;1m'

gta = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
  #//Colors 
white = '\033[1;37m' # White 
red = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan

idgroup = []


idd = ("100022350489847")
duma = ("===========================================")
savefile = ("ids.txt")
banner= blue+red+"""____________  ______                      _   
|  ___| ___ \ | ___ \  Author by Alvins  | |  
| |_  | |_/ / | |_/ /___ _ __   ___  _ __| |_ 
|  _| | ___ \ |    // _ \ '_ \ / _ \| '__| __|
| |   | |_/ / | |\ \  __/ |_) | (_) | |  | |_ 
\_|   \____/  \_| \_\___| .__/ \___/|_|   \__|
                        |_| #Version 0.3"""+red+blue+"""
-------------------------------------------------
---T-O-O-L-S---F-A-C-E-B-O-O-K---P-R-I-V-A-T-E---
-------------------------------------------------
  # FBReport Tools Private
  # Create By Elang X-CoderID      """+blue+blue+"""            
  # YouTube : Pangeran Alvins            
  # WhatsApp : +62822475712**            
  # Facebook: Alvins 
-------------------------------------------------"""
print banner
me = (blue+red+'[🔴] Pilih Tools⏩')
oh= time.sleep(1)


class Repot3:
 def __init__(self):
     oh
     print (white+'  [[1]]⏩'+green+' Auto Report FB-v3')
     oh
     print (white+'  [[2]]⏩'+green+' Hack Live BruteForce Attack')
     oh
     print (white+'  [[3]]⏩'+green+' Auto Create Wordlist')
     oh
     print (white+'  [[0]]⏩'+green+' Keluar')
     time.sleep(2)
     print
     print
     self._check()




 def _check(self):
     try:
         inn = raw_input(me+(''))
         if(inn=='1'):
             print
             self.updown()
             print g
         elif(inn==''):
                 print
                 see.home()
         elif(inn=='3'):
             print 
             wordlist.you()
         elif(inn=='2'):
             print 
             fbbrute.shit()
         elif(inn=='4'):
             time.sleep(2)
             exit()
         elif(inn=='0'):
             exit()
     except Exception as g:
          print g
     else:
         return self._check()
 
       
       
 def updown(self):
     oh
     print (white+'  [[01]]⏩'+green+'  Target ID')
     oh
     print (white+'  [[02]]⏩'+green+'  Daftar ID')
     print (white+'  [[00]]⏩'+green+'  Kembali')
     print
     inn2 = raw_input(me+(''))
     if(inn2=='1'):
         fbreport.Repot3()
     elif(inn2=='2'):
         print (red+'[🔴]Tunggu Update Berikutnya')
         exit()
     elif(inn2=='0'):
         os.system('clear')
         os.system('python2 Repot3.py')
     else:
         return self.updown()
     
       
       

       
if __name__ == "__main__":
	Repot3()