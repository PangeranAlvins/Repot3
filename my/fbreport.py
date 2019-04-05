#!/usr/bin/python
# coding=utf-8
#/////.coded by: Pangeran Alvins
import re
import random
import time
import bs4
import os,sys
import mechanize
import cookielib
import requests

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


savefile = ("ids.txt")

filee = ('ids.txt')
    
    
    

         
    
    #// Main Class
class Repot3:
 def __init__(self):
		self.br=mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.set_cookiejar(cookielib.LWPCookieJar())
		self.br.addheaders = [
			(
			"User-Agent",random.choice(
			open("useragents.txt").read().splitlines())
			)
		]
		time.sleep(1)
		print
		time.sleep(2)

		print (green+'        [#] Login Facebook Account')
		print 
		print
		self.url=('https://m.facebook.com/login.php')
		self._email= raw_input(red+'[#]'+green+'Enter Email:    '+blue+red+'')
		self._passwr= raw_input(red+'[#]'+green+'Enter Password: '+blue+red+'')
		self.login()
		
          
    		 

 
		
		
		
		#//Login Checker
 def login(self):
     self.br.open(self.url)
     self.br.select_form(nr=0)
     self.br.form["email"] = "{}".format(self._email)
     self.br.form["pass"]  = "{}".format(self._passwr)
     self.br.submit()
     if "save-device" in self.br.geturl():
         print
         print(green+"[#] Login success √ ")
         print
         return self._cadow1()
     else:
         print
         print (red+'[#] login Gagal ')
         time.sleep(1)
         exit()
		
		

 def _cadow1(self):
     print
     self._id= raw_input(red+'[#]'+green+'Username Target:    '+blue+red+' ')
     my = ("https://m.facebook.com/"+self._id)
     url = my
     self.br.open(url)
     self.r=re.findall('<title>(.*?)</title>',self.br.response().read())
     if len(self.r) !=0:
        self._dray= raw_input(red+'[#]'+green+'Ketik Untuk Melanjutkan: :    '+red+blue+self.r[0]+' [y/yes]'+'')
        return self._lady()
      
                
                        
             
          
          
 def _lady(self):
     if(self._dray=='yes'):
         return self._indo()
     elif(self._dray=='y'):
         return self._indo()
     else:
         exit()
       
            
 def _indo(self):
     uoh= open(filee,'r')
     self.uhoh=uoh.read()
     if self._id in self.uhoh:
         print
         print (red+'.         Oops 405')
         print
         time.sleep(1)
         time.sleep(red+'Kesalahan saat memasukan ID')
         time.sleep(1)
         return self._cadow1()
     else:
          return self._cadow2()
                    
     
     
		      
		     
		      
  
		
		
 def _cadow2(self):
          _bs = self.br.response().read()
          bb=bs4.BeautifulSoup(_bs,
				features="html.parser"
			)
          if len(bb) !=0:
           for x in bb.find_all("a",href=True):
            if "rapid_report" in x["href"]:
             _cadow = x["href"]
             self.br.open(_cadow)
             return self._cadow3()
         
          
          
 def _cadow3(self):
          try:
           self.br._factory.is_html=True
           self.br.select_form(nr=0)
           self.br.form["tag"] = ["profile_fake_account"]
           self.br.submit()
           return self._cadow4()
          except Exception as f:
                 print ('    Bad404')
                
          
          
          
          
          
          
 def _cadow4(self):
          try:
           self.br._factory.is_html=True
           self.br.select_form(nr=0)
           self.br.form["action_key"] = ["FRX_PROFILE_REPORT_CONFIRMATION"]
           self.br.submit()
           return self._cadow5()
          except Exception as f:
                 print ('    Bad405')
                 
                 
                 
                 
                 
                 
 
 def _cadow5(self):
          try:
           self.br._factory.is_html=True
           self.br.select_form(nr=0)
           self.br.form["checked"] = ["yes"]
           self.br.submit()
           jj = open(filee,'w')
           jj.write(self._id)
           print
           time.sleep(2)
           print (C+green+'[#]Sukses Reported √ ')
           time.sleep(1)
           exit()
          except Exception as f:
                 print ('    Bad406')