from venmo_api import Client
import os

path = os.getcwd()
access_token_path = path + "/../../access_token.txt"
f = open("access_token.txt", "r")
access_token = f.read()
try:
    venmo = Client(access_token=access_token)
    venmo.my_profile()
    print("Success")
except:
    print("Invalid Access Token")

