from Contact import Contact
from Address_Book import Address_Book

cont1=Contact(
    "Shreyash",
    "Singh",
    "Varanasi",
    "Varanasi",
    "Uttar pradesh",
    "235",
    "123456",
    "vk18@gmail.com"

)

book1=Address_Book()
# addedd contact in address_Book using contact object cont1
print("\nUser details are:")
book1.add_Contact(cont1)
book1.display_contact()