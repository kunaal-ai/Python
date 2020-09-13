class Customer:
    def __init__(self,fname,lname,address,phone):
        self.fname      =   fname
        self.lname      =   lname
        self.address    =   address
        self.phone      =   phone
        self.full_name  =   fname + lname 
    def full_name(self):
# added new test            
    
customer_01 = Customer('kunaal','thanik','205 www',84923849534)        
print(customer_01.full_name)
        
         