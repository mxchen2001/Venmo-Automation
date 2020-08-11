from venmo_api import Client
from os import system, name 
import getpass


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' # yellow
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


clear()
title = '''===================
    Venmo Login
===================
'''


print(title)
username = input("Email: ")
password = input("Password: ")

try:
    access_token = Client.get_access_token(username=username, password=password)
    dst = open("access_token.txt", "w")
    dst.write(access_token)
    dst.close()
    print(bcolors.OKGREEN + "Login Success" + bcolors.ENDC)
except:
    print(bcolors.FAIL + "Error: Login Failed, incorrect Email or Password" + bcolors.ENDC)
