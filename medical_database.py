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
Project 3: Improved medical database: error handling, hashed password, more data stored in tuple 
(first, last, weight, sex, result)

Project 5: Update the medical database with functions:
Create a branch and make all your changes on that branch
Update the medical database to use functions (you decide on what should be functions)
Add a new option to update user records (for example, changing a patient's status from "positive" to "negative")
Create a Pull Request on github to merge your changes (We will walk through the PR together)


'''
import time
import hashlib


# Data Base
data = {"Bob":('Bob', 'Bobson','175', 'M', 'negative'), "John":('John', 'Johnson','153', 'M', 'positive'), "Sara":('Sara', 'Sarason','130', 'F', 'positive')}

# Var
usr_id = ""
file = open("usr_list.txt", 'r')
auth = False
user_auth = True




def add_pat():
    while True:
        add_patient_first = input("Please give me the first name of the Patient ['q' to quit]: ")
        if add_patient_first.lower() == 'q':
            break
        else:
            #print(data)
            add_patient_last = input('Last Name: ')
            add_patient_weight = input('Weight: ')
            add_patient_sex = input('Sex (M/F): ')
            add_patient_result = input('Result (positive/negative): ')
            data[add_patient_first] = add_patient_first, add_patient_last, add_patient_weight, add_patient_sex, add_patient_result
            
            #print(data)
            tuple(data)
def search_pat():
 while True:
            print("What is their First name?")
            lookup_name = input("First Name ['q' to quit]: ")
            if lookup_name.lower() == 'q':
                break
            else:
                if (any(lookup_name in i for i in data)): # Check if patient exists
                    data_print = data[lookup_name]
                    first, last, weight, sex, result = data_print
                    print(data_print)
                    print('First name:',first,'\nLast name:',last,'\nCOVID Result:',result)
               
                # No patient error message
                else:
                    print("User Does Not Exist")
                    
def edit_pat():
    while True:
            print("What is their First name?")
            lookup_name = input("First Name ['q' to quit]: ")
            if lookup_name.lower() == 'q':
                break
            else:
                if (any(lookup_name in i for i in data)): # Check if patient exists
                    data_print = data[lookup_name]
                    first, last, weight, sex, result = data_print
                    change_data = input("What would you like to edit?\n 1: Result \n 2: Weight\n")

                    if change_data == "1":
                        print("Their existing result is:",result)
                        usr_change = input("What would you like to change it to (positive/negative): ")
                        if usr_change == 'positive' or usr_change == 'negative':
                            data[lookup_name] = first, last, weight, sex, usr_change
                            print(data[lookup_name])
                            
                        else:
                            print("Please input positive or negative")

                    if change_data == "2":
                        print("Their existing weight is:",weight)
                        usr_change = input("What would you like to change it to (only numbers): ")
                        data[lookup_name] = first, last, usr_change, sex, result

                    #print('First name:',first,'\nLast name:',last,'\nCOVID Result:',result)
                
                # No patient error message
                else:
                    print("User Does Not Exist")






# Welcome Message
print("Welcome to the Medical Database")
user = input("Username: ")

# Check if user exists
while user_auth:
    for lines in file:
       
        # Splicing User from Password Hash
        if user in lines:                                                                                         
            usr_id = lines.split(":")[1].strip()
            print("Please Enter Your Password")
    
    # Password Input
    for retry in range(3,0,-1):
        password_input = input("Password: ")
        pass_input_hash = hashlib.md5(password_input.encode())
        pass_input = pass_input_hash.hexdigest()
    
        # Correct Password
        if pass_input == usr_id:
            auth = True
            user_auth = False
            break
    
        # Incorrect Password
        if pass_input != usr_id:
            print('You have',retry - 1,'atempts remaining')
    
    # Break loop after 3 tries 
    if retry == 1:
        user_auth = False

time.sleep(.2)

# Main Menu Loop
while auth:
    
    # Menu Selector
    print("1: Add New Result, 2: Search the Database, 3: Edit Patient, 4: Exit Program")
    action = input("What do you want to do? ")
    
    
    # Adding Patients
    if action == "1":
        add_pat()


    # Searching for Patients
    elif action == "2":
        search_pat()
              
    # Edit Patient
    elif action == "3":
        edit_pat()

    # Exit Program
    elif action == "4":
        print("Thank you! Come again soon,",user)
        auth = False


    # Error Code
    elif action != (1,2,3,4):
        print("Error: Option Not Found")
