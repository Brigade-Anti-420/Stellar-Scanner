import pyfiglet
import sys
import socket
from datetime import datetime
import pystyle
from pystyle import *
from time import sleep
import os


# MADE BY Brigade Anti-420 !!#1418
# Using api of socket and module pyfliget in order to
# NO SKID AND FUCK SKIDDERS !!! #


Cyan = '\033[96m'
Green = '\033[92m'


# ascii_banner = pyfiglet.figlet_format("Stellar-Scanner")
# print(ascii_banner)

    
how ="""Common User Passwords Profiler

options:
  -h, --help         show this help message and exit
  -i, --interactive  Interactive questions for user password profiling
  -w FILENAME        Use this option to improve existing dictionary, or WyD.pl output to make some pwnsauce
  -l                 Download huge wordlists from repository
  -a                 Parse default usernames and passwords directly from Alecto DB. Project Alecto uses purified databases of
                     Phenoelit and CIRT which were merged and enhanced
  -v, --version      Show the version of this program.
  -q, --quiet        Quiet mode (don't print banner)
  
  """
  



def print_cow():
    print(" ___________ ")
    print(" \033[07m  Stellar-Scanner! \033[27m            # \033[07mN\033[27mmap")
    print("      \                     # \033[07mU\033[27mrllib")
    print("       \   \033[1;31m,__,\033[1;m             # \033[07mS\033[27mocket")
    print(
        "        \  \033[1;31m(\033[1;moo\033[1;31m)____\033[1;m         # \033[07mS\033[27mcan"
    )
    print("           \033[1;31m(__)    )\ \033[1;m  ")
    print(
        "           \033[1;31m   ||--|| \033[1;m\033[05m*\033[25m\033[1;m      [ Brigade Anti-420 !!#1418 | add me on discord ! ]"
    )
    print(28 * " " + "[ My Github | https://github.com/Brigade-Anti-420]\r\n")
    
    

#outdef

print_cow()
print(how)
choice = input(str("Choose method: "))



def trgIprdm():
    target = input(str("Target IP: "))
    print("=" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at : " + str(datetime.now()))
    print("=" * 50)

    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.000000001)
                    
            result = s.connect_ex((target,port))
            if result == 0:
                print(Green + "Port: [{}] -->  status :      open | Response:              RECEIVE RESPONSE".format(port))
                reask = input("A Port open has be found, Do you want to continue ?")
                if reask == 'y':
                    print(Green + "Port: [{}] -->  status :      open | Response:              RECEIVE RESPONSE".format(port))
                else:
                    print("Exiting...")
                    sleep(1)
                    sys.exit()
            else:
                print(Cyan + "Port: [{}] -->  status :      closed | Response:              NO RESPONSE".format(port))
                
    except KeyboardInterrupt:
        print(Colors.red + "\n Ctrl + C detected, Exiting...")
        sleep(2)
        sys.exit()
    
    except socket.error:
        print("\ Host not responding ! Check if you are connected or using a VPN ! ")
        sys.exit()
        
def trgself():
    cpt = socket.gethostname() 
    cptadrr = socket.gethostbyname(cpt)
    print("=" * 50)
    print("Scanning Target: " + cptadrr)
    print("Scanning started at : " + str(datetime.now()))
    print("=" * 50)

    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.00000000000000001)
                    
            result = s.connect_ex((cptadrr,port))
            if result == 0:
                print(Green + "Port: [{}] -->  status :      open | Response:              RECEIVE RESPONSE".format(port))
                reask = input(Colors.yellow + "A Port open has be found, Do you want to continue ?")
                if reask == 'y':
                    print(Green + "Port: [{}] -->  status :      open | Response:              RECEIVE RESPONSE".format(port))
                else:
                    print("Exitng...")
                    sleep(1)
                    sys.exit()
            else:
                print(Cyan + "Port: [{}] -->  status :      closed | Response:              NO RESPONSE".format(port))
                
    except KeyboardInterrupt:
        print(Colors.red + "\n Ctrl + C detected, Exiting...")
        sleep(2)
        sys.exit()
    
    except socket.error:
        print("\ Host not responding :( ")
        sys.exit()
     
     
def helpall():
    print(helpbanner)
    a = input("Do you want to return to the Hub ? (y/n)")
    if a == "y":
        print_cow()
        print(how)
        
    else:
        sys.exit()

helpbanner="""

How can I use Port scanner ?

1} You simply have to choose if you want to target YOUR ip address or IP address of people

2} You put the IP (IPV4) if you have an error, verify that you wrote an available IP ;)

3} That will show you all ports closed and all port open, if you find a port open, you simply have to writ "y" to continue or "n" to exit the program.


"""
    
def main():
    if choice == "target -self":
        trgself()
    elif choice == f'target -people':
        trgIprdm()
    elif choice == '-h' or choice == "--help":
        os.system('cls')
        helpall()
    else:
        sys.exit()
main()
