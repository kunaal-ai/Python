states = ['Ohio','New York','DC','IL']

for i in states:
    if i == 'DC':
        print('Found\n')
        break
    print(i)
    
for j in states:
    if j == 'DC':
        print('Found')
        continue
    print(j)
    
# Range 
# range(start,stop,step)
# default start to 0 if not initialized 
print(list(range(4)))
print(list(range(1,5)))
print(list(range(1,10,3))) # this will print 3 element from 1
# OR
for r in range(5): # will start at 0
    print(r)    
print('\n')  
for ra in range(1,5): # will start at 0
    print(ra)  
print('\n')  
  
# While
order_id = 50
while order_id < 55:
    print(order_id) 
    order_id += 1   
else:
    print("Else is executed")    
    
    
dic_one = {"Position":"SDET","Address":"123 XYZ","Phone":"999-555-777"}
for i in dic_one:
    print("Keys "+ i + " Values", dic_one[i])    
    
    
t_one = ('asd','asdf')
for i in t_one:
    print(i)
    
   