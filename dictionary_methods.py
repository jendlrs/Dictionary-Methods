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

#dictionary
personalDataDict = {
    "Ma. Jensen Nicole C. Dela Rosa" : {
        "Name" : "Ma. Jensen Nicole C. Dela Rosa",
        "Age" : 19,
        "Gender" : "F",
        "Address" : "Quezon City",
        "Phone Number" : "09238271212",
        "Email Address" : "jensennics.dlrs@gmail.com",
        "COVID 19 Vaccination Status" : "Fully Vaccinated"
    },
    "Placeholder2" : {
        "Name" : "Person2",
        "Age" : 1, #for int
        "Gender" : "",
        "Address" : "",
        "Phone Number" : "",
        "Email Address" : "",
        "COVID 19 Vaccination Status" : ""
    },
}
while True:
    userInputFunct = int(input ("\nWhat do you want to do? [Enter the corresponding number only \033[92m(1-3)\033[0m from the MENU]: "))
    #3rd Step: Declaring a Dictionary
    if userInputFunct not in range (1,4):
        print ("\n=====Sorry you have entered an invalid input.===== \n            Please Enter 1 to 3 only.")
    #4th Step: Add the condition
        #Option1
    elif userInputFunct == 1:
        name = input ("What is your Name? ")
        age = int (input("How old are you? "))
        gender = input ("What is your Gender? (F/M) ")
        address = input ("Where do you live? ")
        phoneNumber = input ("What is your phone number? ")
        emailAdd = input ("What is your email? ")
        vaccineStatus = input ("What is your COVID 19 Vaccine Status? ")

        #modifying existing item
        UpdateDict = dict({
                "Name" : name,
                "Age" : age, #for int
                "Gender" : gender,
                "Address" : address,
                "Phone Number" : phoneNumber,
                "Email Address" : emailAdd,
                "COVID 19 Vaccination Status" : vaccineStatus
                })
        personalDataDict[name] = personalDataDict["Placeholder2"]
        del personalDataDict["Placeholder2"]
        personalDataDict[name].update(UpdateDict)

        print ("\n===-Personal Information is Saved-===\n")
        #display updated Info
        #Option2
    elif userInputFunct == 2:
        print("option2")
        #option3
    elif userInputFunct == 3:
        exitVerification = input("Are you sure you want to exit? (Y/N) ")
        if exitVerification == "Y":
            print ("\nThank you for using this program\n")
            break
        else:
            continue
