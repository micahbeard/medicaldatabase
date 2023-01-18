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
'''
import time
import hashlib


# Data Base
data = [('Bob', 'Bobson','175', 'M', 'negative'), \
    ('John', 'Johnson','153', 'M', 'positive'), \
    ('Sara', 'Sarason','130', 'F', 'positive')]
data = list(data)
# Var
usr_id = ""
file = open("usr_list.txt", 'r')
auth = False
user_auth = True

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
    print("1: Add New Result, 2: Search the Database, 3: Exit Program")
    action = input("What do you want to do? ")
    
    
    # Adding Patients
    if action == "1":
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
                new_patient = add_patient_first, add_patient_last, add_patient_weight, add_patient_sex, add_patient_result
                data.insert(-1, new_patient)
                #print(data)
                tuple(data)

    
    # Searching for Patients
    elif action == "2":
        while True:
            print("What is their First name?")
            lookup_name = input("First Name ['q' to quit]: ")
            if lookup_name.lower() == 'q':
                break
            else:
                if (any(lookup_name in i for i in data)): # Check if patient exists
                    data_print = list(filter(lambda x: x[0] == lookup_name, data))
                    data_print_conv = map(list, zip(*data_print))
                    first, last, weight, sex, result = data_print_conv
                    print('First name:',first,'Last name:',last,'COVID Result:',result)
               
                # No patient error message
                else:
                    print("User Does Not Exist")

                                               
                # Error Code
                """if lookup == None:
                    print("404: Not Found")"""
    # Exit Program
    elif action == "3":
        print("Thank you! Come again soon,",user)
        auth = False
    # Error Code
    elif action != (1,2,3):
        print("Error: Option Not Found")
