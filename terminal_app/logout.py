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

src =  open('access_token.txt', 'r')
access_token = str(src.read())

venmo = Client(access_token=access_token)

logout_sequence = "Bearer " + access_token

try:
    venmo.log_out(logout_sequence)
    dst = open("access_token.txt", "w")
    dst.write("")
    dst.close()
    print(bcolors.OKGREEN + "Logout Success, revoked token" + bcolors.ENDC)
except:
    print(bcolors.OKGREEN + "User Already Logged Out" + bcolors.ENDC)

