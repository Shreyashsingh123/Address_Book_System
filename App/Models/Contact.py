print("Welcome to  Address Book program")

class Contact:
    '''
    created constructor to Initialize the details of user 
    
    '''
    def __init__(self,first_name,last_name,address,city,state,zip,phone,email):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.phone=phone
        self.email=email
    def display(self):
        '''
        Display all Details of user which include:
        First name, Last name, Address,  City, State, Phone,zip,email

        '''
        print("First name is: {}".format(self.first_name))
        print("Last name is: {}".format(self.last_name))
        print("Address is: {}".format(self.address))
        print("City is: {}".format(self.city))
        print("State is: {}".format(self.state))
        print("Zip is: {}".format(self.zip))
        print("Phone number is: {}".format(self.phone))
        print("Email is: {}".format(self.email))

