def first_function():
    print("In method first function")

first_function()

# parameter
def pass_values(name,message):
    print('{},{}'.format(name,message))
    
pass_values('Kunaal','is teaching Python')    

# Optional Parameter, should be in same order
def pass_optional_values(name,message='is SDET'):
    print('{},{}'.format(name,message))
    
pass_optional_values('Kunaal') 
pass_optional_values('Kunaal','Optional value is passing') 

# pass argument as Tuples and Dictionary. But can not pass existing tuple or dictionary 
def employee(*args, **kwargs):
    print(args)
    print(kwargs)
employee('Kunaal','Sam',department='SDET',year=2)    

# pass list and this will change to tuples and second as dictionary 
def customer(*args,**kwargs):
    print(args)
    print(kwargs)

order_items_list     =  ['Books','Grocery']
customer_info        =  {'name':'Simon','Location':'DC','Phone':'5555-555-55'}
customer(*order_items_list,**customer_info)    # * will unpack values       