class Searching:
    def Search_city(self,city,state):
        '''
        Search a person by city name and display result
        '''
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
        '''
        Display person in city or state using dictionary
        '''
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
            return result
        
    
    def count_by_city(self,city,state):
        '''
        Count number of person in city and state and display the  result
        '''
        city_count=0
        state_count=0
        for k,v in self.Address_Book_dict.items():
            for i in v.contact:
                if i.city==city:
                    city_count+=1
                if i.state==state:
                    state_count+=1
        
        print("Number of person in city {} is\t".format(city),city_count)
        print("Number of person in state{} is:".format(state),state_count)
       

