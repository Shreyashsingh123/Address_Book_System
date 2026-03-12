from Contact import Contact
from Address_Book import Address_Book

# taken user input and add it to contact class
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

book1=Address_Book()
# addedd contact in address_Book using contact object cont1

book1.add_Contact(cont1)
book1.display_contact()

e1=input("If you want to e1 details choose y or choose n [y/n]")
if e1.upper()=='Y':
   #  if yes then edit existing contact person using their name or first name
    n=input("Enter the first name of user whose detail you want to edit: ")
    book1.editdetails(n)
book1.display_contact()

# enter user to delete 
deleteuser=input("Choose y to delete contact and n to not [Y/N]")
if deleteuser.upper()=='Y':
    n=input("Enter first name of user whose details you want to delete")
    book1.deleteDetails(n)
