class Customer:
    raise_amount = 4  # class variables
    def __init__(self,fname,lname,address,phone,pay): # instance variables
        self.fname      =   fname
        self.lname      =   lname
        self.address    =   address
        self.phone      =   phone
        self.pay        =   pay
        self.full_name  =   fname + lname 
        
    def full_names_only(self):
        return f'{self.lname},{self.fname}'
    
    def calculate_cashback(self):
        self.pay = int(self.pay * self.raise_amount)
        print(self.pay)
                
customer_01 = Customer('kunaal','thanik','205 www',84923849534,5000)        
customer_02 = Customer('James','Brown','888 XYZ',999111222,10000)        

# print(customer_01.full_names_only())   OR 
print(Customer.full_names_only(customer_01))
print(Customer.full_names_only(customer_02))
Customer.calculate_cashback(customer_01)
         
         