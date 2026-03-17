from App.Models.Contact import Contact
from App.Utils.File_Handler import File_Handling
from App.Utils.Sorting import Sorting
import json
class Address_Book(File_Handling,Sorting): #to manage mutlitple contacts
    def __init__(self):
        self.contact=[] #list of contact details
    
    def create_new_contact(self):
        F_name=input("Enter first name:")
        L_name=input("Enter Last name:")
        address=input("Enter your Address:")
        city=input("Enter your city:")
        state=input("Enter your State:")
        zip=input("Enter your zip code: ")
        phone=int(input("Enter phone number:"))
        email=input("Enter your email:")
     
        cont1=Contact(
              F_name,
              L_name,
              address,
              city,
              state,
              zip,
              phone,
              email
        )
    # addedd contact in address_Book using contact object cont1
        self.add_Contact(cont1)
        print("\nContact added successfully!\n")

        
    def add_Contact(self,c):
        '''
        If first name of contact is not present then add contact

        '''
        for i in self.contact:
            if i.first_name==c.first_name:
                print("Contact is already present.") #one address book one name 
                return
           
        self.contact.append(c)
                
    def display_contact(self):
        '''
        To Display all the contact means user details
        '''
        for contacts in self.contact:
            print("User Details are:")
            contacts.display() #calls display method from contact file for each contact from list
            print("\n**************\n")

    def editdetails(self,name):
        '''
        To Edit the details of user using first name access user then edit details

        '''
        for i in self.contact: #address book contact details accessed here
            
            if i.first_name==name: # check that user exist in contact using first name
                user=True
                while(user):
                    print("Choose 1 to Edit first name")
                    print("Choose 2 to edit last name")
                    print("Choose 3 to edit address")
                    print("Choose 4 to edit city")
                    print("Choose 5 to edit state")
                    print("Choose 6 to edit zip")
                    print("Choose 7 to edit phone number")
                    print("Choose 8 to edit email")
                    print("Choose 0 to exit ")
                    choice =int(input("Enter option to edit:"))

                    match choice:
                        case 1:
                            n=input("enter updated first name  ")
                            i.first_name=n
                        case 2:
                            n=input("enter updated last name  ")
                            i.last_name=n
                        case 3:
                            n=input("enter updated Address  ")
                            i.address=n
                        case 4:
                            n=input("enter updated city  ")
                            i.city=n
                        case 5:
                            n=input("Enter updated state  ")
                            i.state=n

                        case 6:
                            n=input("enter updated zip  ")
                            i.zip=n
                        case 7:
                            n=int(input("Enter updated phone  "))
                            i.phone=n
                        case 8:
                            n=input("Enter updated email ")
                            i.email=n
                        case 0:
                            break
                                           
    def deleteDetails(self,name):
        '''
        To Delete the user using first name of user
        
        '''
        found=False
        for i in self.contact:
            if i.first_name==name:
                self.contact.remove(i)
                found=True
                print("Contact deleted Successfully")
                break
        if not found:
            print("Contact not found")
   