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

    def Search_city(self,city,state):
        found=False
        for name,detail in self.Address_Book_dict.items():
            for i in detail.contact:
                if i.city==city:
                    print(name,":","City: ",city,":", "name:",i.first_name,i.last_name)
                    found=True
                if i.state==state:
                    print(name,":","State: ",state,":", "name:",i.first_name,i.last_name)
                    found=True

        if not found:
                print("No contact in this city or state")
    
    def View_Person(self,city,state):
        result={}
        for name,book in self.Address_Book_dict.items():
            city_dict={}
            state_dict={}
            for user in book.contact:
                if user.city==city:
                    city_dict[user.city]=city_dict.get(user.city,[])+[user.first_name]
                if user.state==state:
                    state_dict[user.state]=state_dict.get(user.state,[])+[user.first_name]
            
            result[name]=[city_dict,state_dict]
            print(result)


