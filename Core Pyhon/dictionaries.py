# Dict are mutable but KEYS MUST be immutable data type. such as int, float, str but not list as can be changed index values
# VALUES can be list as well
# un-ordered
population2 = {1:17.8,2:13.3,3.5:13.0,'Mumbai':12.5}

employees = {'name':'kunaal','department':'Software QA','min_hours':40}
print(employees)

# Add
employees['is_current_staff'] = False
print(employees)

# UPDATE - if multiple values 
employees.update({'name':'Thanik','department':'Unknown'})
print(employees)

# without update function for single item only
employees['department'] = 'SDET'
print(employees)

print(employees['name'])
# print(employees['address'])   # will throw error
print(employees.get('address')) # will return None as not found in dictionary
print(employees.get('address','Not Found here ! ')) # will return passed value as not found in dictionary else actual value
employees['address']='115 Planet Mars'
print(employees.get('address','Not Found here !'))

# DELETE
del(employees['min_hours'])
print('Deleted min_hours:',employees)

# OTHER
print(employees.keys())
print(employees.values())
print(employees.items())

for key,value in employees.items():
    print(key,value)
for i,j in employees.items():
    print(j)
    
# Nested Dictionary
nested_dict = {
    'dictA':{'key_1':'value_1'},
    'dictB':{'key_2':'value_2'}
}
nested_dict['dictA']['access_code'] = 4565
print(nested_dict)



verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
verse_set = set(verse_list)
print(verse_set, '\n')
print(len(verse_set))