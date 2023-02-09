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

Project 6: medical database update 3.0. Create a patient class to hold patient data rather than using a tuple. 
Add a height variable to the patient class, add a method to calculate and return bmi, add a method to “add” or “store” notes about a patient, 
add a method to retrive the notes on a patient.

'''
import time
import hashlib




class Patient:
    first_name = ""
    last_name = ""
    sex = ""
    height = 0
    weight = 0
    result = ""
    bmi = 0


    def cal_bmi(self):
        bmi_cal = int(self.weight) / int(self.height)**2
        self.bmi = round(bmi_cal * 703, 1)
        print("=====================")
        print (self.first_name,":",self.bmi,"bmi")
        print("=====================")

    def view_data(self):
        print("=====================")
        print("First Name: ",self.first_name)
        print("Last Name: ",self.last_name)
        print("Result: ",self.result)
        print("=====================")
    
    def add_pat(self):
        print("======Adding Patient======")
        self.first_name = input("First Name: ")
        self.last_name = input("Last Name: ")
        self.sex = input("Sex(M/F): ")
        self.height = input("Height in inches: ")
        self.weight = input("Weight in pounds: ")
        self.result = input("Positive/Negitive: ")
        success()

    def edit_pat(self):
        print("======Edit Patient======")
        print("What would you like to update?\n'1' to Update Height\n'2' to Update Weight\n'3' to Update result")
        update_pat = input()
        if update_pat == "1":
            print("---Update Height---")
            print("Current Height: ",self.height)
            update_pat_h = input("Height(in): ")
            self.height = int(update_pat_h)
            success()
        elif update_pat == "2":
            print("---Update Weight---")
            print("Current Weight: ",self.weight)
            update_pat_w = input("Weight(lb): ")
            self.weight = int(update_pat_w)
            success()
        elif update_pat == "3":
            print("---Update Result---")
            print("Current Result: ",self.result)
            update_pat_r = input("Result(positive/negative): ")
            if update_pat_r == "positive" or update_pat_r == "negative":
                self.result = update_pat_r
                success()
            else:
                pat_error()

def pat_error():
    print("-----ERROR-----")

def success():
    print("======Success======")


bob = Patient()
bob.first_name = "Bob"
bob.last_name = "Bobson"
bob.height = 70.8
bob.weight = 162.3
bob.result = "negative"
bob.sex = "M"

john = Patient()
john.first_name = "John"
john.last_name = "Johnson"
john.height = 65.3
john.weight = 146.23
john.result = "positive"
john.sex = "M"

sara = Patient()
sara.first_name = "Sara"
sara.last_name = "Sarason"
sara.height = 54.2
sara.weight = 103.4
sara.result = "negative"
sara.sex = "F"


# Data Base
data = {"Bob": bob, "John": john, "Sara": sara}
# Var
usr_id = ""
file = open("usr_list.txt", 'r')
auth = False
user_auth = True

def add_pat():
    print("=====================")
    add_patient_id = input("New Patient's Name: ")
    add_pat_def = add_patient_id
    add_pat_def = Patient()
    data[add_patient_id] = add_pat_def
    add_pat_def.add_pat()
        
            
def search_pat():
    print("=====================")
    lookup_name = input("What is the patient's name: ")
    if lookup_name in data.keys(): # Check if patient exists
        data_patient = data[lookup_name]
        data_patient.view_data()

    # No patient error message
    else:
        pat_error()
            
            
                        
def edit_pat():
    print("=====================")
    lookup_name = input("What is the patient's name: ")
    if lookup_name in data.keys(): # Check if patient exists
        data_patient = data[lookup_name]
        data_patient.edit_pat()

    # No patient error message
    else:
        pat_error()

def bmi_cal():
    print("=====================")
    lookup_name = input("What is the patient's name: ")
    if lookup_name in data.keys(): # Check if patient exists
        data_patient = data[lookup_name]
        data_patient.cal_bmi()

    # No patient error message
    else:
        pat_error()


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
    print("=====================")
    print("1: Add New Resultn\n2: Search the Database\n3: Edit Patient\n4: BMI Calculator of Patientn\n5: Exit Program")
    print("=====================")
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

    elif action == "4":
        bmi_cal()


     # Exit Program
    elif action == "5":
        print("Thank you! Come again soon,",user)
        print("=====================")
        auth = False


    # Error Code
    elif action != (1,2,3,4,5):
        print("Error: Option Not Found")
