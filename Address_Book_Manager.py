from Contact import Contact
from Address_Book import Address_Book
class Address_Book_Manager: #to manage mutlitple contacts
    def __init__(self):
        self.Address_Book_dict={}  # craeted dictinary to store multiple address book
        
    def add_Address_Book_to_dict(self,name):
        self.Address_Book_dict[name]=Address_Book()
    def display_Address_Book(self):
        print("**************")
        for name,val in self.Address_Book_dict.items():
            print("Name of Addresss book is: ",name)
            val.display_contact()

