message = "This is a string functions demo"
print(message.lower())
print(message.upper())
print(message.count('l')) # This will count how many number of times 'l' exists
print(message.find('demo')) # find exaxt match and return index number - case sensetive
print(message.find('Not in text')) # If not found then returns -1 value
new_message = message.replace('World','universe')


print(new_message)
first_name = 'kunaal'
last_name = 'Thanik'

# Formating method 01
full_name = first_name +' '+last_name
print(full_name)

# Formating method 02
full_name =  '{} {}'.format(first_name,last_name)
print(full_name)

# Formating method 03 - More advanced and helpful
full_name = f'{first_name.upper()} {last_name.upper()}'
print(full_name)

print(full_name.__contains__('KUN')) # Returns True / false 

print(dir(full_name)) # Prints all possible functions that can be used

print(help(str.lower)) # Help on specefic method