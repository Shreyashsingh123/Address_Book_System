class Sorting:
         def sort_name(self):
            '''
            Sort the details based on first name of user 

            '''
            self.contact.sort(key=lambda x:x.first_name.lower())
        
            print("\nContact Sorted Successfully by (first name)")

   
         def sort_by_city_state(self,s):
            '''
            Sorted the details based on either city or state or zip 
            
            '''
            if s=="city":
                self.contact.sort(key=lambda x:x.city)
            elif s=="state":
                self.contact.sort(key=lambda x:x.state)
            elif s=="zip":
                self.contact.sort(key=lambda x:x.zip)
            else:
                print("invalid value")
            print("contact sorted successfully based on",{s})

