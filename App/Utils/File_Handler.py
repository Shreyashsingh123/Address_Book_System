        
import json
from App.Models.Contact import Contact  
class File_Handling:  

    def save_data_to_file(self, books, filename):
        ''' 
        Save the data to file 
        '''
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
        with open(f"UserData//{filename}{extension}", "w") as file:
            for book_name, book in books.Address_Book_dict.items():
                for contact in book.contact:
                    data =(f"{book_name}{separator}{contact.first_name}{separator}{contact.last_name}{separator}{contact.address}{separator}{contact.city}{separator}{contact.state}{separator}{contact.zip}{separator}{contact.phone}{separator}{contact.email}\n")

                    file.write(data)

        print("Contacts saved to file successfully!")
        
    def load_data_from_file(self, books, filename):
        '''
        To Load all data from file 
        '''
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
            with open(f"UserData//{filename}{extension}", "r") as file:
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
    
    def save_to_json(self,books,filename):
        '''
        Save the data to Json
        '''
        address_books_dict = {}
        for name_ab, book in books.Address_Book_dict.items():
            address_books_dict[name_ab] = []
            for contact in book.contact:
                data = {
                    "first_name": contact.first_name,
                    "last_name": contact.last_name,
                    "address": contact.address,
                    "city": contact.city,
                    "state": contact.state,
                    "zip": contact.zip,
                    "phone": contact.phone,
                    "email": contact.email
                }
                address_books_dict[name_ab].append(data)
        with open(f"UserData//{filename}", "w") as file:
            json.dump(address_books_dict,file,indent=4)
        
        print("Contacts saved to JSON successfully!")
    
 
    def load_from_json(self, books, filename):
        '''
        To Load data from Json 
        '''
        try:
            with open(f"UserData//{filename}", "r") as file:
                data1 = json.load(file)

            for name_ab, b in data1.items():
                books.add_Address_Book_to_dict(name_ab)
                book = books.Address_Book_dict[name_ab]

                for data in b:
                    new_contact = Contact(
                        data["first_name"],
                        data["last_name"],
                        data["address"],
                        data["city"],
                        data["state"],
                        data["zip"],
                        data["phone"],
                        data["email"]
                    )

                    book.add_Contact(new_contact)

            print("Contacts loaded from JSON successfully!")

        except FileNotFoundError:
            print("File not found!")