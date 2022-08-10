#!/usr/bin/python
import sys, os
import subprocess as sp
import os.path

""" Restart """
def restart():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

""" Update Check """
def Update():
   print ("check github for update")

""" Install """
def Install():
   print ("Coming Soon")

""" Banner """
def Banner():
   print (" |======================|")
   print (" |  Discord Tool v0.01  |")
   print (" |======================|") 
   print ("--------------------------------------")
   print (" Coded By Allistar by Star Sec.")

""" Console """
def Console():
   os.system("clear")
   LatVer = "0.0.18"
   InstVer = "0.0.18"
   exist = os.path.exists("/usr/share/discord/Discord")
   if (exist == True):
          FileCheck = "Healthy"
          
   else:
          FileCheck = "Unhealthy" 
   OS = sp.getoutput("uname -r")
   min = sp.getoutput('date +"%I"')
   hour = sp.getoutput('date +"%m"')
   Time = hour + ":" + min 
   print (" ")      
   print ("   ===|[Discord Manager ]|===   ")
   print (" |============================| ")
   print (" |Time: %s                 | " %(Time))   
   print (" |Latest Version: %s      | " %(LatVer))
   print (" |Installed Version: %s   | " %(InstVer))
   print (" |File Integrity: %s     | " %(FileCheck))
   print (" |OS: %s       | " %(OS))
   print (" |============================| ")
   os.system("sleep 4")
   
""" Menu 1 """
def Menu1():
   print (" |============================| ")
   print (" |[01] Run Discord            | ")
   print (" |[02] Check Discord          | ")
   print (" |[03] Repair Discord         | ")
   print (" |[04] Console Mode           | ")
   print (" |[05] Update Tool            | ")
   print (" |[06] Exit                   | ")
   print (" |============================| ")

Banner()
Console()
Menu1() 
MenuOp1 = input(" Choose:  ")
if (MenuOp1 == '01' or MenuOp1 == '1'):
       os.system("clear")
       os.system("/usr/share/discord/Discord --no-sandbox")
       restart() 
     
elif (MenuOp1 == '02' or MenuOp1 == '2'):
       os.system("clear")
       exist = os.path.exists("/usr/share/discord/Discord")
       if (exist == True):
             Console()
             restart() 
             
       elif (exist == False):
             print ("Discord Not installed ")
             print ("Install Now(Y or N):  ")
             Install()
             
       else:
             os.system("clear")
             print ("\n[!] ERROR : Wrong Input")
             os.system("sleep 4")
             restart()     
       

elif (MenuOp1== '03' or MenuOp1 == '3'):
       os.system("clear")
       print ("Coming Soon")
       restart()  
       
elif (MenuOp1 == '04' or MenuOp1 == '4'):
       os.system("clear")
       try:
          while True:
              Console()
       except KeyboardInterrupt:
          pass
          sys.exit()
 
elif (MenuOp1 == '05' or MenuOp1 == '5'):
       os.system("clear")
       print ("Install Updater")
       print ("github here")
       restart() 
       
elif (MenuOp1 == '06' or MenuOp1 == '6'):
       os.system("clear")
       print ("\n[!] Exit the Program...")
       sys.exit()

else:
       os.system("clear")
       print ("\n[!] ERROR : Wrong Input")
       time.sleep(1)
       restart()
