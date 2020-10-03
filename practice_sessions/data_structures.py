# List
list_one = ['W','Z','A','B','C','D','E','F','G','H','I']
    # Add
list_one.append('Appended')    
print(list_one)

list_one.insert(0,'Insert at 0')
print(list_one)

list_one.insert(len(list_one),'Insert at len(a)')
print(list_one)

    # Remove
list_one.remove('Appended')
print(list_one)

pop_out_last_element_from_list = list_one.pop()
print(pop_out_last_element_from_list)

    # Other
print(list_one.count('A'))

a=sorted(list_one, reverse= True)
print(a)
print(list_one)


''' Integers or other data types can NOT be compared with string so SORT function can be used there
    e.g: names_and_age = ['James','Kristine',10,22] will throw an error'''

    # Looping 
for i in list_one:
    print(i)
    
for i in range(len(list_one)):
    list_one[i] = list_one[i].lower()
print(list_one)        

# Sets

# Tuples

# Dictionaries
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

    # Keys - only
for keys in cast:
    print(keys)
    
    # Keys and values - Use items() functions     
for key,value in cast.items():
    print(key,value)
    
    # ADD    
cast['C']='value_4'    
print(cast.get('C'))
print(len(cast))
