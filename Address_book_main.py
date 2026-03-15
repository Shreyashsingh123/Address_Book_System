from Contact import Contact
from Address_Book import Address_Book
from Address_Book_Manager import Address_Book_Manager
# taken multiple user input and add it to contact class
books=Address_Book_Manager()
takeinput=True
while(takeinput):   
   n=input("Enter  Address book name: ")
   
   if n not in books.Address_Book_dict:
      books.add_Address_Book_to_dict(n)
   book1=books.Address_Book_dict[n]

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
   book1.add_Contact(cont1)
   print("\nContact added successfully!\n")

   print("Choose 1 to Display Contacts")
   print("Choose 2 to edit Contact")
   print("Choose 3 to Delete Contact")
   print("Choose 0 to Exit")
   choice = int(input("Enter your choice: "))
   match choice:
        case 0:
            break
        case 1:
            book1.display_contact()
            # print("****************")
        case 2:
            name=input("Enter the name of the contact you want to edit:")
            book1.editdetails(name)
            book1.display_contact()
            # print("***********")
        case 3:            
            name=input("Enter the name of the contact you want to delete:")
            book1.deleteDetails(name)

   addperson = input("Add another person? (y/n): ")
   if addperson.lower() != 'y':
      takeinput=False

d=input("Do you want to display Adress Book or not [Y/N]  ")
if d.lower()=='y':
    books.display_Address_Book()

# search by city
Search_city=input("Enter city name to search:")
Search_state=input("Enter name of state to search:")
books.Search_city(Search_city,Search_state)

# view person in city or state with help os dictionary
view=input("\nDo you want to view details based on city or state [Y/N]")
if view.upper()=='Y':
    viewcity=input("Enter city to view: ")
    viewstate=input("Enter state to view: ")
    viewbook=books.View_Person(viewcity,viewstate)
    print(viewbook)

# count person in city or state
view2=input("\nDo you want to count person in a particular city or state [Y/N]")
if view2.upper()=='Y':
    viewcity=input("Enter city name to count number of person :")
    viewstate=input("Enter state name to count number of person :")
    books.count_by_city(viewcity,viewstate)

sorte=input("\nDo you want sort details by first name [Y/N]")
if sorte.upper()=='Y':
    book1.sort_name()

sort2=input("\ndo you want to sort by state,city or zip [Y/N]")
if sort2.upper()=='Y':
    s=input("enter city or state or zip to which you want to sort  ")
    book1.sort_by_city_state(s)