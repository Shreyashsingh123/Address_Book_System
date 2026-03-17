from App.Utils.Searching import Searching
from App.Models.Contact import Contact
from App.Models.Address_Book import Address_Book
class Address_Book_Manager(Searching): #to manage mutlitple contacts
    def __init__(self):
        self.Address_Book_dict={}  # craeted dictinary to store multiple address book
        
    def add_Address_Book_to_dict(self,name):
        '''
        Add the Address book to dictionary (for unique address book  name)
        '''
        if name not in self.Address_Book_dict:
            self.Address_Book_dict[name]=Address_Book()

    def display_Address_Book(self):
        '''
        Display all the address book and details inside it

        '''
        print("\n **************")
        for name,val in self.Address_Book_dict.items():
            print("Name of Addresss book is: ",name)
            val.display_contact()

    