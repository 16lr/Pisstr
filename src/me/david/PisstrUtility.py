import os
import sys
import subprocess
import wmi
import multiprocessing
import mysql.connector
import nmap
import time
import requests
from pathlib import Path
import psutil
import win32api

def help():
  #we print the utilities inside the help() function
  print("\n"
      "1: Bash Command\n"
      "2: Network Protocols\n"
      "3: Server\n")

class debugging:
  def look() -> None:
   #we will make a user input request for a command to use in shell
   command: str = str(input("Enter the command: "))

   #we will get the Popen by using subprocess library(by using shell = True we use for windows)
   process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   #stdout, stderr will store thge result of the PIPE made a command above
   stdout,stderr = process.communicate()
   
   #if returns 0 than the execution runned successfully
   if process.returncode == 0:
    try:
        #we will enter a folder name by using a user input request
        folder_name: str = input(str("Enter the folder that you whould like to add the stdout: "))
        #we will open the file in append method
        file = open(f"{folder_name}","a")
        #we will write into the file the stdout(decode()) function is made for decoding the encoding method
        file.write(stdout.decode())
        #we will print into the console the result
        print(f"Command outputed on {os.getcwd()} as {folder_name}")
    except Exception as e:
       #else we will print the error
       print(e)
   else:
      #else(if the return code isnt an 0) we will print the stderr
      print("We have an error:",stderr)
      time.sleep(2) # sleep for 2 seconds
      print("The program will close in 3 seconds!") # announce that the program will close 
      time.sleep(3) #we will wait for 3 seconds
      sys.exit() # we will exit the program by using sys.exit() function

  def last() -> None:
   #it is using a user input request
   intrebare_path_exist:str = str(input("Do you want to use an extern path?(Y/N): "))
   #if intrebare_path_exist is true then we will run the if block
   if intrebare_path_exist == "Y" or intrebare_path_exist == "y" or intrebare_path_exist == "YES" or intrebare_path_exist == "yes":
     #first will store the command that runs the specify program
     #Ex: a (.py) file will use as extension python
     first: str = str(input("Enter the extension: "))
     #we enter the path that the file is in
     ext: str = str(input("Enter the path: "))
     #we will concatenate them
     final: str = first+" "+ext
     #we will run the command in shell
     try:
        os.system(final)
     except Exception as err:
       print(err)

   #it is using a user input request
   intrebare_path_formare:str = input(str("Do you want to make a custom path(Y/N): "))
   #if intrebare_path_formare is true then we will run the if block
   if intrebare_path_formare == "Y" or intrebare_path_formare == "y" or intrebare_path_formare == "YES" or intrebare_path_formare == "yes":
    #path_argv will store the current directory
    path_argv: str = str(os.getcwd())
     #path_extension will store the command that runs the specify program
     #Ex: a (.py) file will use as extension python
    path_extension: str = str(input("Enter the extension: "))
    #path_folder will store the file name
    path_folder: str = str(input("Enter the program name from the path: "))
    #we will concatenate them
    path_final: str = (path_extension+" "+path_argv+"\\"+path_folder)
    try:
      #we will run the command in shel
      os.system(path_final)
    except Exception as err:
      print(err)

  
  def check_paths() -> None:
    try:
      #ask variable store the result of the user input
      ask: str = input(str("Do you want to see if the path exists? (Y/N?) -> "))
      #if ask is true then we will run the if block
      if (ask == "Y" or ask == "y" or ask == "yes" or ask == "YES"):
        #path variable will store the user input 
        path: str = input(str("Enter the path to search: "))
        #we check if the path exists and if it does we will print the result "Path exist!"
        if(os.path.exists(path) == True):
          print("Path exist!")
        #else we will print "Path doesn't exist"
        else:
          print("Path doesn't exist!")
      #ask_cautare_path will store of the user input
      ask_cautare_path = input(str("Do you want to search for a folder (Y/N?) -> "))
      #ask_cautare_path is true then we will run the if block
      if ask_cautare_path == "Y" or ask_cautare_path == "y" or ask_cautare_path == "YES" or ask_cautare_path == "yes":
        try:
          #base will store the user input for a path
          base:str = input(str("Enter the path: "))
          #search will store the folder name user input
          search: str = input(str("Enter the folder name: "))
          #in the result will be printed a list of the folders/files/paths that we found
          result = []
          #we will use os.walk() function to walk through files
          for path,dirs,files in os.walk(base):
            #name will iterate through files
            for name in files:
              #if search(folder name that we want) in name then we will append into a path (path +  the file of name)
              if search in name:
                result.append(os.path.join(path,name))
            #name will iterate through dirs
            for name in dirs:
              #if search(folder name) = name(directory)
              if search in name:
                #if search(folder name that we want) in name then we will append into a path (path +  the file of name)
                result.append(os.path.join(path,name))
          
          #if result is null then we cant find any matching
          if len(result) == 0:
            print("We couldn`t find any matching result")
          #else we will print the result
          elif len(result) != 0:
            print(result)

        #if there is an exception at the try block then we will try to print it
        except Exception as e:
          raise(e)
    #if there is an exception at the try block then we will try to print it
    except Exception as err:
      raise(err)

  def execute() -> None:
   #question will store the user input for http request
   question: str = input(str("Enter the http request: "))
   #r will store the requests.get(http request)
   r = requests.get(f"{question}")
   try:
     #if status code == 200(worked perfectly)
     if r.status_code == 200:
       #we will tranform res_json into a json file so we can print them
       res_json = r.json()
       print(res_json)
     else:
       #else we will print the error
       print("Couldn't make the connection between request and http!")
   except Exception as http_err:
     raise(http_err)
  
  def checking():
    #we will print all the utilities that we have
    print("1: See all host names")
    print("2: See host state")
    print("3: See all protocols")
    print("4: See if a protocol is (up/down)")
    #we will make a while loop to loop through it till we want to stop
    while True:
       #we need to select what ot the utilities that we have
       check: str = input(str("Enter a utility: "))
       if check == "back":
         return
       #host will store the host name 
       host: str = input(str("Enter the host: "))
       if host == "back":
         return
       #in port we need to specify the number of ports(range) to scan. Ex: till 100 we need to type (100)
       port: str = input(str("Enter the number of ports: "))
       if port == "back":
         return
       #we will create an nmap port scan
       nm = nmap.PortScanner()
       #we will scan for the host and port
       nm.scan(host,port)

       #if we type into check 1 then it will print us the hosts of an specified ip
       if check == "1":
         print(nm[host].hostname())
       elif check == "2":
         #if we type 2 into check then it will print us state(UP or DOWN)
         print(nm[host].state())
       elif check == "3":
         #if we type 3 into check then it will print what hostname() function and state() does combined
         print(nm[host].all_protocols())
       elif check == "4":
         number:int = input(int("Enter the number of port that you want to scan"))
         #it checks for a port if it is open or not
         print(nm[host].has_tcp(number))
       
       #if we dont want to use another command we can print anything but no "Y" or "YES" or "y" or "yes" and it will exit 
       ans = input(str("Do you want to use another command: (Y/N)"))
       if ans != "Y" or ans != "yes" or ans != "YES" or ans != "y":
          break

#prints every specify from your computer + processes that are running into a folder
def info() -> None:
    try:
          #we will create a wmi 
          c = wmi.WMI()

          #we will iterate through win32_BaseBoard 
          for mother_board in c.Win32_BaseBoard():
             #mother_board_str will store the serial number of c.win32_BaseBoard that we iterated through
             mother_board_str = mother_board.SerialNumber
             print(f"Mother_board_SerialNumber: {mother_board_str}\n")

          for hardisk in c.Win32_diskdrive():
            #hardisk_str will store the name of c.win32_diskdrive that we iterated through
            hardisk_str = hardisk.name
            print(f"hardisk_name: {hardisk_str}\n")

          for hd in c.Win32_OperatingSystem():
            #hd_str will store the build number of c.Win32_OperatingSystem that we iterated through
            hd_str = hd.BuildNumber
            #hd_SerialNumber will store the serial number of c.Win32_OperatingSysem that we iterated through
            hd_SerialNumber = hd.SerialNumber
            #Registered will store the Registered user of c.Win32_OperatingSystem that we iterated through
            Registered = hd.RegisteredUser
            print(f"hd_buildnumber: {hd_str}\n")
            print(f"hd_serialNumber: {hd_SerialNumber}\n")
            print(f"Registered: {Registered}\n")

          #we will print pcu cores
          multiprocessing_str = multiprocessing.cpu_count()
          print(f"cpu_core: {multiprocessing_str}\n")

          #we will get computer name by using win32api library
          computer: str = win32api.GetComputerName()
          print(f"computer_name: {computer}\n")
          #we will get username of the pc by using win32api library 
          name: str = win32api.GetUserName()
          print(f"name: {name}\n")

          #question will store a user input
          question: str = input(str("Do you want to print all the processes that are running(Y/N) -> "))
          #if question is yes then we will run if block
          if question == "Y" or question == "y" or question == "YES" or question == "yes":
            #we will add arr as a set to not have in the list the same catergory twice
            arr = set()
            
            #we will iterate thorugh psutil.process_iter to get current processes that are running 
            for process in psutil.process_iter():
              #we will append to arr the process.name() of current processes
              arr.add(process.name())

            #file_processes will be opened in append method
            file_processes = open("processes.txt","a")

            #we will iterate through arr
            for process_name in arr:
              #we will write to file_processes file the processes from arr that are stored to process_name
              file_processes.write(process_name)
              file_processes.write("\n")
            
            file_processes.close()

    #if we have an error in the try block we will raise an error
    except Exception as err:
        raise err

def connection() -> None:
    #use_db will store the user input 
    use_db: str = input(str("Do you want to connect to db(Y/N) -> "))
    #if use_db is "yes"or "y" or "YES" or "Y" we will run the f block
    if use_db == "Y" or use_db == "y" or use_db == "yes" or use_db == "YES":
        #we will make suer input for host, user, password, db name to connect to database using mysql connector
        h = input(str("Host -> "))
        u = input(str("user -> "))
        p = input(str("password -> "))
        d = input(str("DataBase -> "))
        #we will connect to database using mysql.connector.connect() function that takes as parameters the user input
        mydb = mysql.connector.connect(
          host=f"{h}",
          user=f"{u}",
          password=f"{p}",
          database = f"{d}"
        )
        curl = mydb.cursor()
    
    #path will store the current directory
    path = Path(os.getcwd())
    #we will run this block of code till we want to stop it using "back"
    while True:
       #command will store the user input 
       command = input(str(f"{__file__} -> "))
       #if command is db
       if command == "db":
          try:
             #we will execute the command
             curl.execute(command[2:])
          #else we will print the error
          except Exception as curl_error:
            print(curl_error)
       if command == "exit":
          break
       
       #if command is ls
       elif command == "ls":
           #file_path will iterate through path.iterdir()
           for file_path in path.iterdir():
             #we check if it is a file and then we print them
             if file_path.is_file():
               print(file_path.name)

       #if first 2 letters from the user input of the command is cd then we will run the try block
       elif command[0:2] == "cd":
         try:
            #we will try to remove white spaces
            new_path:str = command[2:].strip()
            #we will append to current directory the new path and if the os.chdir() function worked correctly 
            os.chdir(os.getcwd() + f"\\{new_path}")
            #we will print the current directory that we have changed
            print(os.getcwd())
         #if something happend in the try block that gave us an error then we will print it
         except Exception as err_path:
           print(err_path)

       #if we type info then we will run the info function
       elif command == "info":
         try:
           info()
         #if we got an error we will print the exception
         except Exception as info_exception:
           print(info_exception)

       #if the first 3 letter of the user input are run
       elif command[0:3] == "run":
         #we will try to run from the 3 letters to the finish the command that the user will type by using subprocess function. shell = True will be for windows kernel
         try:
           subprocess.run(command[3:], shell=True)   
         #if we got an error we will try to print it
         except Exception as command_err:
           print(command_err)
        
       #if the first 5 letter of the user input are popen
       elif command[0:5] == "popen":
         #we will use subprocess.popen(), cwe will take from the 5 letters of command till finish to run the shell comand, shell will be true for windows kernel, stdout,stderr wil create a pipe between them 
         process = subprocess.Popen(command[5:],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
         #stdout, stderr will cuse the process.comunicate() to get the result
         stdout,stderr = process.communicate()
         try:
           if stdout:
             #we will try to print the stdout using .decode() function to decode he UTF-8 or whatever encryptation we have
             print(stdout.decode())
           else:
             #else we will try to print the stderr
             print(stderr.decode())
         #if try block didn't work then we will try to print the error
         except Exception as popen_err:
           print(popen_err)
       
       #if we type back the while loop ends
       elif command == "back":
         break

if __name__ == "__main__" and sys.platform == "win32" and os.name == "nt":
  while True:
    #question for a better decoration when we type the user input will print the current directory + file name that runs
    question: str = input(str(f"{__file__} >>> "))
    #if we need help we can type help in the user input and it will show us the utilities inside the help() function
    if question == "help":
      help()
    
    #if we type 1 we will use 1 first it will print us the utilities 
    elif question == "1":
      print("\n"
            "1: Use a cmd command\n"
            "2: Run a path command\n"
            "3: Check a path command\n"
            "4: Make HTTP request\n")
      
      while True:
        #question_global for a better decoration when we type the user input will print the current directory + file name that runs
        question_global: str = input(str(f"{__file__} -> "))

        #if the user input is 1 we will run the look function that is inside the debugging class
        if question_global == "1":
          debugging.look()
        #if the user input is 2 we will run the last function that is inside the debugging class
        elif question_global == "2":
          debugging.last()
        #if the user input is 3 we will run the check_paths function that is inside the debugging class
        elif question_global == "3":
          debugging.check_paths()
        #if the user input is 4 we will run the execute function that is inside the debugging class
        elif question_global == "4":
          debugging.execute()
        #if the user input is 'back' then we will break the while loop
        elif question_global == "back":
          break
        else:
          print("Command unknown")

    #else if question is 2 we will run the checking() function that is inside the debugging class
    elif question == "2":
      debugging.checking()

    #elif question is 3 we will run the connection function()
    elif question == "3":
      connection()
    #else we will print command unknown
    else:
      print("Command unknown")
    
