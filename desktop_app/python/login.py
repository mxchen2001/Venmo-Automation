from venmo_api import Client
import os, sys


access_token = sys.argv[1]

try:
    venmo = Client(access_token=access_token)
    venmo.my_profile()
    print("Success")
except:
    print("Invalid Access Token")
    access_token = ""
    # print("Success")

dst = open("access_token.txt", "w")
dst.write(access_token)
dst.close()