import os

user_phonebook = {}

def MainMenu():
    while True:
        try:
            First_choice = int(input("What Would you like to do? Add a new contact(1), Edit an existing contact(2), Delete a contact(3), search for a contact(4), Display all contacts(5), Export Contacts to a text file(6), Import Contacts from a text file(7), Quit(8)"))
            if First_choice == 1:
                AddContact()
            elif First_choice == 2:
                EditContact()
            elif First_choice == 3:
                DeleteContact()
            elif First_choice == 4:
                ContactSearch()
            elif First_choice == 5:
                DisplayContacts()
            elif First_choice == 6:
                ExportContacts()
            elif First_choice == 7:
                ImportContacts()
            elif First_choice == 8:
                print("Thanks for using our phonebook!\nHave a great day.")
                break

def AddContact():
    pass

def EditContact():
    pass

def DeleteContact():
    pass

def ContactSearch():
    pass

def DisplayContacts():
    pass

def ExportContacts():
    pass

def ImportContacts():
    pass


MainMenu()
