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
userInputFunct = int(input ("\nWhat do you want to do? [Enter the corresponding number only \033[92m(1-3)\033[0m from the MENU]: "))
#3rd Step: Declaring a Dictionary
personalDataDict = {
    "Name" : "Ma. Jensen Nicole C. Dela Rosa",
    "Age" : 19,
    "Gender" : "F",
    "Address" : "Quezon City",
    "Phone Number" : "09238271212",
    "Email Address" : "jensennics.dlrs@gmail.com",
    "COVID 19 Vaccination Status" : "Fully Vaccinated"
    }
#4th Step: Add the condition
    #Option1
if userInputFunct == 1:
    name = input ("What is your Name? ")
    age = int (input("How old are you? "))

    #modifying existing item
    personalDataDict ["Name"] = name
    personalDataDict ["Age"] = age
    print (personalDataDict)
    #Option2
    #Option3