# ------------------------------------------------------
# Rules
# no spaces
# Use only ordinary leeters, numbers and uncerscores.
# Need to start with letter or underscore.
# -------------------------------------------------------

# int
# float
# boolean 
# string

print(type(300))
print(type(300.00))
print(type('300'))


# variable declaration 
var_a = 5
var_b = 10
# or 
var_a, var_b = 5,10

# int and Float conversion
temp_float_value = 500.888
temp_int_calue = 333
print(int(temp_float_value))
print(float(temp_int_calue))

# in python 0.1 != 0.1 , It is actually more than that. Not big concern but important to know. 
# E.g:
print(0.1+0.1+0.1) # Expected result would be 0.3 but actual is 0.30000000000000004 
# this will make an issue if we try confirm if above statement is == 0.3
print(0.1+0.1+0.1 == 0.3) # response will be False

# Boolean (True / False)
print(42>50)  # output: False


# String
fname = 'kunaal'
lname = 'thanik'
print(fname + ''+ lname)
print(fname*5)