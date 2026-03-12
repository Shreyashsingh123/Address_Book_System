from Contact import Contact

class Address_Book: #to manage mutlitple contacts
    def __init__(self):
        self.contact=[] #list of contact details
    def add_Contact(self,c):
        self.contact.append(c)
    def display_contact(self):
        for contacts in self.contact:
            print("\nUser Details are:")
            contacts.display() #calls display for each contact from list
            print("\n**************\n")

# created a contact details using contact class


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