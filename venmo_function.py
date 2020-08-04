from venmo_api import Client

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' # yellow
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def is_positive_float(f_input):
    if(f_input > 0):
        return 0
    elif (f_input == 0):
        print("Can't be '0'")
        return 1
    else:
        print("Not Postive")
        return 2

def requestMoney(person_request, amount = 0.01, note=""):
    try:
        users = venmo.user.search_for_users(query=person_request, page=1)
    except:
        print("No Access Token")
        return
    found_user = False
    for user in users:
        if person_request == user.username:
            found_user = True
            print(bcolors.OKBLUE + "username: " + bcolors.ENDC + bcolors.WARNING + user.username + bcolors.ENDC, end=", ")
            print(bcolors.OKBLUE + "display name: " + bcolors.ENDC + bcolors.WARNING +  user.display_name + bcolors.ENDC, end=", ")
            print(bcolors.OKBLUE + "id: " + bcolors.ENDC + bcolors.WARNING + user.id + bcolors.ENDC)
            # Request Money
            print("Sending Request ... ", end="")
            venmo.payment.request_money(amount, note, user.id)
            print(bcolors.OKGREEN + "Request sent" + bcolors.ENDC)
    if not found_user:
        print( bcolors.FAIL + "Error: No User Found" + bcolors.ENDC)

def sendMoney(person_request, amount = 0.01, note=""):
    try:
        users = venmo.user.search_for_users(query=person_request, page=1)
    except:
        print("No Access Token")
        return
    found_user = False
    for user in users:
        if person_request == user.username:
            found_user = True
            print(bcolors.OKBLUE + "username: " + bcolors.ENDC + bcolors.WARNING + user.username + bcolors.ENDC, end=", ")
            print(bcolors.OKBLUE + "display name: " + bcolors.ENDC + bcolors.WARNING +  user.display_name + bcolors.ENDC, end=", ")
            print(bcolors.OKBLUE + "id: " + bcolors.ENDC + bcolors.WARNING + user.id + bcolors.ENDC)
            # Send Money
            print("Sending Money ... ", end="")
            venmo.payment.send_money(amount, note, user.id)
            print(bcolors.OKGREEN + "Transaction Complete" + bcolors.ENDC)
    if not found_user:
        print( bcolors.FAIL + "Error: No User Found" + bcolors.ENDC)


def venmoFunc(action_type, username, f_amount, note):
    if (action_type == "R" or action_type == "r"):
        requestMoney(person_request=username,amount=f_amount, note=note)
    elif (action_type == "S" or action_type == "s"):
        sendMoney(person_request=username,amount=f_amount, note=note)
    else:
        print(bcolors.FAIL + "Transaction Type not discovered" + bcolors.ENDC)
    return


src =  open('access_token.txt', 'r')
access_token = str(src.read())


venmo = Client(access_token=access_token)