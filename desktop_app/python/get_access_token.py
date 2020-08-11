from venmo_api import Client
import os
import getpass, sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' # yellow
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    # access_token = Client.get_access_token(username=sys.argv[1], password=sys.argv[2])
    access_token = "hello world"
    print(access_token)
    # print(code + "\13")
    path = os.getcwd()
    access_token_path = path + "/../../access_token.txt"
    dst = open("access_token.txt", "w")
    dst.write(access_token)
    dst.close()
    print(bcolors.OKGREEN + "Login Success" + bcolors.ENDC)
except:
    print(bcolors.FAIL + "Error: Login Failed, incorrect Email or Password" + bcolors.ENDC)
