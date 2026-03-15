from Contact import Contact
import json
class Address_Book: #to manage mutlitple contacts
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
        for i in self.contact:
            if i.first_name==c.first_name:# to check unique name should be there
                print("Contact is already present.") #one address book one name 
                return
           
        self.contact.append(c)
                
    def display_contact(self):
        for contacts in self.contact:
            print("User Details are:")
            contacts.display() #calls display method from contact file for each contact from list
            print("\n**************\n")

    def editdetails(self,name):
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
        found=False
        for i in self.contact:
            if i.first_name==name:
                self.contact.remove(i)
                found=True
                print("Contact deleted Successfully")
                break
        if not found:
            print("Contact not found")
    def sort_name(self):
        self.contact.sort(key=lambda x:x.first_name)

        print("\nContact Sorted Successfully by (first name)")

    # sort by city,stete or zip
     # input city,state or zip based on value get sorted
    def sort_by_city_state(self,s):
        if s=="city":
            self.contact.sort(key=lambda x:x.city)
        elif s=="state":
            self.contact.sort(key=lambda x:x.state)
        elif s=="zip":
            self.contact.sort(key=lambda x:x.zip)
        else:
            print("invalid value")
        print("contact sorted successfully based on",{s})
        
         
    # file read and write in data1.txt use case 13
    def save_data(self,filename):
        with open(f"UserData//{filename}", "w") as file:
            for cont in self.contact:
                data1=f"{cont.first_name},{cont.last_name},{cont.address},{cont.city},{cont.state},{cont.zip},{cont.phone},{cont.email}\n"
                file.write(data1)
        print("Contact saved to file successfully\n")
    
    def read_data(self,filename):
        try:
            with open(f"UserData//{filename}", "r") as data:
                for val in data:
                    data1 = val.strip().split("|")

                    if len(data1) == 8:
                        cont2 = self.contact(
                            data1[0], data1[1], data1[2],
                            data1[3], data1[4], data1[5],
                            data1[6], data1[7]
                        )
                        self.add_Contact(cont2)
                data.seek(0)
                print("Address book is",filename)
                print(data.read())

            print("Contacts displayed from file successfully!\n")

        except FileNotFoundError:
            print("File not found!")