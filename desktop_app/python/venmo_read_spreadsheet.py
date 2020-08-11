import xlrd 
import os
import array as arr 
from venmo_function import venmoFunc, bcolors, is_positive_float

# Give the location of the file 
path = ("assets/static/input.xlsx") 
try:
    # To open Workbook 
    workbook = xlrd.open_workbook(path) 
    sheet = workbook.sheet_by_index(0) 
    
    # For row 0 and column 0 
    # sheet.cell_value(0, 0)


    user_dictionary = {}

    # total_user is 0 indexed
    total_users = sheet.nrows

    if (total_users == 1):
        print(bcolors.WARNING + "Spreadsheet is empty" + bcolors.ENDC + " ... " + bcolors.OKGREEN + "Exiting" + bcolors.ENDC)
        quit()


    for user in range(1, total_users):
        single_user = {}
        for col in range(sheet.ncols): 
            # row '0' is the top row with column names
            column = str(sheet.cell_value(0, col)).lower()
            if (column == "username"):
                # print("Username col: ", end="")
                # print(sheet.cell_value(user, col))
                single_user['Username'] = sheet.cell_value(user, col)
            elif (column == "amount"):
                # print("Amount col: ", end="")
                # print(sheet.cell_value(user, col))
                try:
                    float(sheet.cell_value(user, col))
                except ValueError:
                    print(bcolors.FAIL + "ValueError for Amount in row: " + bcolors.ENDC + bcolors.WARNING + str(user + 1) + bcolors.ENDC)
                    quit()
                temp = is_positive_float(float(sheet.cell_value(user, col)))
                if (temp == 1):
                    print(bcolors.FAIL + "Amount cannot be '0' in row: " + bcolors.ENDC + bcolors.WARNING + str(user + 1) + bcolors.ENDC)
                    quit()
                elif (temp == 2):
                    print(bcolors.FAIL + "Not a Positive amount in row: " + bcolors.ENDC + bcolors.WARNING + str(user + 1) + bcolors.ENDC)
                    quit()

                single_user['Amount'] = float(sheet.cell_value(user, col))
            elif (column == "note"):
                # print("note col: ", end="")
                # print(sheet.cell_value(user, col))
                single_user['Note'] = sheet.cell_value(user, col)
            elif (column == "type"):
                # print("type col: ", end="")
                # print(sheet.cell_value(user, col))
                single_user['Type'] = sheet.cell_value(user, col)
            else:
                print("error")
        user_dictionary[user] = single_user

    for user in range(len(user_dictionary)):
        username = user_dictionary[(user + 1)]["Username"]
        amount = user_dictionary[(user + 1)]["Amount"]
        note = user_dictionary[(user + 1)]["Note"]
        action_type = user_dictionary[(user + 1)]["Type"]
        venmoFunc(action_type=action_type, username=username, f_amount=amount, note=note)

    print(bcolors.OKGREEN + "Complete" + bcolors.ENDC)
except:
    print("err_no_input")
    exit(69)

# removes the input file after running the script
os.remove(path)