from venmo_api import Client
from os import system, name 
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' # yellow
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        print("Not a float")
        return False

def is_positive_float(str):
    f_str = float(str)
    if(f_str > 0):
        return True
    elif (f_str == 0):
        print("Can't be '0'")
        return False
    else:
        print("Not Postive")
        return False

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def requestMoney(person_request="ishan0102", amount = 0.01, note=""):
    users = venmo.user.search_for_users(query=person_request, page=1)
    found_user = False
    for user in users:
        if person_request == user.username:
            found_user = True
            print("username: " + user.username)
            print("display name: " + user.display_name)
            print("id: " + user.id)
            # Request Money
            print("Sending Request ... ", end="")
            venmo.payment.request_money(amount, note, user.id)
            print("Request sent")
    if not found_user:
        print("Error: No User Found")

def sendMoney(person_request="ishan0102", amount = 0.01, note=""):
    users = venmo.user.search_for_users(query=person_request, page=1)
    found_user = False
    for user in users:
        if person_request == user.username:
            found_user = True
            print("username: " + user.username)
            print("display name: " + user.display_name)
            print("id: " + user.id)
            # Request Money
            print("Sending Money ... ", end="")
            # venmo.payment.send_money(amount, note, user.id)
            print("Transaction Complete")
    if not found_user:
        print("Error: No User Found")


def venmoFunc(action_type="Request"):

    word = str


    if (action_type == "Request"):
        word = "==============Request==============\n"
        bottom_bar = "==================================="

    else:
        word = "===============Send================\n"
        bottom_bar = "==================================="

    clear()
    print(word + "\n\n\n" + bottom_bar)

    # Username is a string
    username = input("Enter Username : ") 
    word += "Username: " + username + "\n"
    clear()
    print(word + "\n\n" + bottom_bar)

    # Note is a string
    note = input("Enter Note : ") 
    word += "Note: " + note + "\n"
    clear()
    print(word + "\n" + bottom_bar)

    # Amount is a positive float
    amount = str
    invalid_number = True
    while invalid_number:
        amount = input("Enter Amount (float) : ")
        invalid_number = not is_float_try(amount)
        if not invalid_number:
            invalid_number = not is_positive_float(amount)

    f_amount = float(amount)
    word += "Amount: " + amount + "\n"
    clear()
    print(word + bottom_bar)

    final_check = input("Are you sure you want to continue (Y/N): ")

    if not (final_check == "Y" or final_check == "y"):
        return False

    if (action_type == "Request"):
        requestMoney(person_request=username,amount=f_amount, note=note)
    else:
        sendMoney(person_request=username,amount=f_amount, note=note)
    
    return True

src =  open('access_token.txt', 'r')
access_token = str(src.read())


venmo = Client(access_token=access_token)

menu = '''What do you want to do:
1) Request Money
2) Send Money
3) Exit
'''


valid_selection_try_again = False
valid_selection_menu = False
clear()
while not valid_selection_try_again:

    print(menu)

    selection = input("I want to do: ")
    # apparently no switch statements in python????
    # not putting the loop inside a function in order to prevent sys.exit(0) from causing memory leaks
    success = True
    while not valid_selection_menu:
        if (selection == "1"):
            clear()
            success = venmoFunc(action_type="Request")
            valid_selection_menu = True
        elif (selection == "2"):
            clear()
            success = venmoFunc(action_type="Send")
            valid_selection_menu = True
        elif (selection == "3"):
            valid_selection_menu = True
            print(bcolors.OKGREEN + "Exiting ... " + bcolors.ENDC)
            # this one right hear 
            sys.exit(0)
        else:
            clear()
            print(menu)
            print(bcolors.FAIL + "Invalid choice, try again" + bcolors.ENDC)  
            selection = input("I want to do: ")


    if success:
        try_again = input("Do you want to keep going? (Y/N): ")
        if (try_again == "Y" or try_again == "y"):
            valid_selection_try_again = False
            valid_selection_menu = False
        elif (try_again == "N" or try_again == "n"):
            print("Exiting ... ")
            sys.exit(0)
        else:
            print("Invalid choice, try again")
            valid_selection_try_again = False
        clear()
    else:
        clear()
        valid_selection_menu = False
        print(bcolors.WARNING + "Oops, something went wrong\n" + bcolors.ENDC)

