'''
Project 2: Create a “medical database” script that simulates a medical database that contains covid test results. 
Here is the expected behavior (all through the Terminal using what we have discussed thus far):
Welcome message when the program starts
The user is asked to authenticate with a password (The password is “Bg922!”)
If they fail 3 times the program automatically exits
If they successfully authenticate then they are given a screen with gives them 3 options. 
They can enter “1” to add a new result to the database, 
they can enter “2” to search the database for a person's results, or they can enter “3” to exit the program.
If they enter 1 they are asked to give the patient's name and their covid status (positive or negative)
If they enter 2 they are prompted to give a patients name and then they are given the status of that patient's results
After hitting 1 or 2 and filling out the information they are returned to the main menu.
If they enter 3 they are thanked for using the program and it exits


hash the password
error checking
'''
import time
from colorama import Fore
password_usr = "Bg922!"
# results = dict(John = "positive", Bob = "negative", George = "negative", Johnny = "negative", Keira = "positive", Sara = "positive", Marry = "negative")

# Data Base
john = ('John', )



user = input("Username: ")
auth = False
print(Fore.GREEN,"Welcome to the Medical Database.", "Please Enter Your Password.")
time.sleep(.2)
for retry in range(3):
    password_input = input("Password: ")
    if password_input == password_usr: 
        auth = True
        break
    if password_input != password_usr:
        print(Fore.RED,"Incorrect Password")
time.sleep(.5)
while auth:
    #usr_input = 0
    print(Fore.WHITE,"1: Add New Result, 2: Search the Database, 3: Exit Program")
    action = input("What do you want to do? ")
    #action = int(usr_input)
    if action == "1":
        while True:
            name = input("Please give me the name of the Patient ['q' to quit]: ")
            if name.lower() == 'q':
                break
            else:
                result_add = input("Give me their results (positive or negative): ")
                results[name]=result_add.lower()
    elif action == "2":
        #lookup = input("What is their name? ['q' to quit]: ") 
        while True:
            print(Fore.WHITE+"What is their name?")
            lookup = input("Name ['q' to quit]: ")
            if lookup.lower() == 'q':
                break
            else:
                results_look = results.get(lookup)
                if results_look == "negative":
                    print(Fore.GREEN+results.get(lookup))
                elif results_look == "positive":
                    print(Fore.RED+results.get(lookup))
                    results_look = results.get(lookup)
                if results_look == None:
                    print(Fore.RED+"404: Not Found")
    elif action == "3":
        print("Thank you! Come again soon,",user)
        auth = False
    elif action != (1,2,3):
        print(Fore.RED+"Error: Option Not Found")
