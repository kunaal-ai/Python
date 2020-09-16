employees = {'name':'kunaal','department':'Software QA','min_hours':40}
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
    
