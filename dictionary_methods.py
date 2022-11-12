#Seatwork 3 in DSA

#Write a python program for contact tracing:

#- Display a menu of options
#	Menu:
#		 1 -> Add an item
#		 2 -> Search
#		 3 -> Exit (y/n)
#- Allow user to select item in the menu (check if valid)
#- Perform the selected option
#		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
#				   Use dictionary to store the info
#				   Use the full name as key
#				   The value is another dictionary of personal information
#		- Option 2: Search, ask full name then display the record
#		- Option 3: Ask the user if want to exit or retry.

#Example Output:

#Menu:
# 1 -> Add an item
# 2 -> Search
# 3 -> Exit (y/n)

#What do you want to do? (1-3): 1
#Full name: Danilo Madrigalejos
#Age: 30
#Address: Eastwood
#Phone number: 1234567890
#Saved!
#What do you want to do? (1-3): 2
#Full name: Danilo Madrigalejos
#Age: 30
#Address: Eastwood
#Phone number: 1234567890 What do you want to do? (1-3): 3
#Exit? n

#1st Step: Display the Menu
print ("\n=======-MENU-=======\n")
print ("  1 --> Add an Item")
print ("  2 --> Search")
print ("  3 --> Exit\n")
print ("====================")
#2nd Step: Ask Input from the user 
while True:
    userInputFunct = int(input ("\nWhat do you want to do? [Enter the corresponding number only \033[92m(1-3)\033[0m from the MENU]: "))
    #3rd Step: Declaring a Dictionary
    personalDataDict = {
                "data1" : {
                    "Name" : "Ma. Jensen Nicole C. Dela Rosa",
                    "Age" : 19,
                    "Gender" : "F",
                    "Address" : "Quezon City",
                    "Phone Number" : "09238271212",
                    "Email Address" : "jensennics.dlrs@gmail.com",
                    "COVID 19 Vaccination Status" : "Fully Vaccinated"
                }
            }
    if userInputFunct not in range (1,4):
        print ("\n=====Sorry you have entered an invalid input.===== \n            Please Enter 1 to 3 only.")
    #4th Step: Add the condition
        #Option1
    elif userInputFunct == 1:
        name = input ("What is your Name? ")
        age = int (input("How old are you? "))
        gender = input ("What is your Gender? (F/N) ")
        address = input ("Where do you live? ")
        phoneNumber = input ("What is your phone number? ")
        emailAdd = input ("What is your email? ")
        vaccineStatus = input ("What is your COVID 19 Vaccine Status? ")

        #modifying existing item
        personalDataDict ["Name"] = name
        personalDataDict ["Age"] = age
        personalDataDict ["Gender"] = gender
        personalDataDict ["Address"] = address
        personalDataDict ["Phone Number"] = phoneNumber
        personalDataDict ["Email Address"] = emailAdd
        personalDataDict ["COVID 19 Vaccination Status"] = vaccineStatus

        print ("\n===-Personal Information is Saved-===\n")
        #display updated Info
        print ("\nThese are the information we received:\n")
        for key, value in personalDataDict.items():
            print(key, ":", value,"\n")
        #Option2
    elif userInputFunct == 2:
        nameSearch = input ("Please enter your full name: ")
        for key, value in personalDataDict["data1"].items():
            if value == nameSearch:
                print ("\nThese are what we found: \n")
        #display updated Info
                for key, value in personalDataDict["data1"].items():
                    print(key, ":", value,"\n")
        #option3
    elif userInputFunct == 3:
        exitVerification = input("Are you sure you want to exit? (Y/N) ")
        if exitVerification == "Y":
            print ("Thank you for using this program")
            break
        else:
            continue
