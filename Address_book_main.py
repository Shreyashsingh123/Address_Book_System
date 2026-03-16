from Contact import Contact
from Address_Book import Address_Book
from Address_Book_Manager import Address_Book_Manager
# taken multiple user input and add it to contact class
books=Address_Book_Manager()
book1=None
takeinput=True
while(True):   
   print("Choose 1 to Add a new Address Book ")
   print("Choose 2 to Add a new Contact")
   print("Choose 3 to Display Contacts")
   print("Choose 4 to edit Contact")
   print("Choose 5 to Delete Contact")
   print("Choose 6 to display address book")
   print("Choose 7 to Search by city")
   print("Choose 8 to view details based on city or state")
   print("Choose 9 to count person in a particular city or state")
   print("Choose 10 to sort details by first name")
   print("Choose 11 to sort details by state,city or zip")
   print("Choose 12 to Add contact into files")
   print("Choose 13 to load Contact from files")
#    print("Choose 9 to save contact to file")
   print("Choose 0 to Exit")
   choice = int(input("Enter your choice: "))
   match choice:
        case 0:
            break
        case 3:
            book1.display_contact()
        case 4:
            name=input("Enter the first name of the contact you want to edit:")
            book1.editdetails(name)
            book1.display_contact()
            # print("***********")
        case 5:            
            name=input("Enter the name of the contact you want to delete:")
            book1.deleteDetails(name)
        case 1:
           n=input("Enter  Address book name: ")
           if n not in books.Address_Book_dict:
             books.add_Address_Book_to_dict(n)
           book1=books.Address_Book_dict[n]
        case 6:
           books.display_Address_Book()
        case 7:
           # search by city
            Search_city=input("Enter city name to search:")
            Search_state=input("Enter name of state to search:")
            books.Search_city(Search_city,Search_state)
        case 8:
            viewcity=input("Enter city to view: ")
            viewstate=input("Enter state to view: ")
            viewbook=books.View_Person(viewcity,viewstate)
            print(viewbook)
        case 9:
            viewcity=input("Enter city name to count number of person :")
            viewstate=input("Enter state name to count number of person :")
            books.count_by_city(viewcity,viewstate)
        case 10:
           book1.sort_name()
        case 11:
           s=input("enter city or state or zip to which you want to sort  ")
           book1.sort_by_city_state(s)
        case 2:
           book1.create_new_contact()
        case 12:
            if book1!=None:
                book1.save_data_to_file(books,"address book")
            else:
                print("Initialize Address Book first.")
        case 13:
            if book1!=None:
                book1.load_data_from_file(books,"address book")
            else:
                print("Initialize Address Book first.")







