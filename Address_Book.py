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
        self.contact.sort(key=lambda x:x.first_name.lower())

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
    def save_data_to_file(self, books, filename):

        file_format = input("Save to file [1] TXT | [2] CSV : ")

        if file_format == "1":
            separator = " | "
            extension = ".txt"
        elif file_format == "2":
            separator = ","
            extension = ".csv"
        else:
            print("Enter valid option!")
            return
        with open(f"UserData\\{filename}{extension}", "w") as file:
            for book_name, book in books.Address_Book_dict.items():
                for contact in book.contact:
                    data =(f"{book_name}{separator}{contact.first_name}{separator}{contact.last_name}{separator}{contact.address}{separator}{contact.city}{separator}{contact.state}{separator}{contact.zip}{separator}{contact.phone}{separator}{contact.email}\n")

                    file.write(data)

        print("Contacts saved to file successfully!")
    # read data from file
    def load_data_from_file(self, books, filename):
        # print(filename)
        file_format = input("Enter 1 for TXT file and 2 for CSV file: ")

        if file_format == "1":
            separator = "|"
            extension = ".txt"
        elif file_format == "2":
            separator = ","
            extension = ".csv"
        else:
            print("Enter valid option!")
            return

        try:
            with open(f"UserData\\{filename}{extension}", "r") as file:
                for line in file:
                    data = line.strip().split(separator)
                    if len(data) == 9:
                        book_name = data[0]
                        books.add_Address_Book_to_dict(book_name)
                        book = books.Address_Book_dict[book_name]

                        new_contact = Contact(
                            data[1], data[2],
                            data[3], data[4],
                            data[5], data[6],
                            data[7], data[8]
                        )
                        book.add_Contact(new_contact)

            print("Contacts loaded from file successfully!")

        except FileNotFoundError:
            print("File not found!")