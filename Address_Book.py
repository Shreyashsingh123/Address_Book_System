from Contact import Contact

class Address_Book: #to manage mutlitple contacts
    def __init__(self):
        self.contact=[]
    def add_Contact(self,c):
        self.contact.append(c)
    def display_contact(self):
        for contacts in self.contact:
            print("\nUser Details are:")
            contacts.display() #calls display for each contact from list
            print("\n**************\n")

# created a contact details using contact class


