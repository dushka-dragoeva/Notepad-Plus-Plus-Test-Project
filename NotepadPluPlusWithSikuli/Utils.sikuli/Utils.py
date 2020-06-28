from sikuli import *
import os
import subprocess
import time

def OpenNotepadPlusPlus():
    command  = r"C:\Program Files (x86)\Notepad++\notepad++.exe"
    subprocess.call(command)

def CloseNotepadPlusPlus():
    os.system("taskkill/f/im notepad++.exe")
    
def CloseAll():
   click("1593336579354.png")
   click("CloseAll.png")
    