cars = ["BMW","AUDI","Toyata"]

print("\n*********************    ADD             ************************\n")

# ADD
cars.insert(0,"Insert_method") # Add at index location

cars.append('Appended_method') # Add at end of list

cars_2 = ["Kia","Honda"]
cars.extend(cars_2) # will add another list in another one. Returns nothing - change the value of initial list

print(cars)

print("\n*********************    REMOVE        ************************\n")
# Remove
cars.remove('BMW')
print('Removed - BMW:',cars)

new_car_list = cars.pop()
print('POP:',new_car_list) # returns last item in list

print("\n*********************    SORT         ************************\n")


cars.reverse()  # revers the original list
print('REVERSE: ',cars)

cars.sort()  # sort original list
print('SORT-Def-ASC:',cars)

cars.sort(reverse=True)  # sort original list in reverse 
print('Sort DESC:',cars)

sorted_cars_list = sorted(cars) # returns new sorted list, without changing original list
print('SORTED:',sorted_cars_list)

print("\n*********************    Others         ************************\n")

print('Index Kia: ',cars.index('Kia')) # returns index number of value

print('string in List:','AUDI' in cars)  # Returns True or false if exists in String


print("\n*********************    NUMERIC         ************************\n")

amount = [123250,546698,456987,8,1]
print(min(amount))
print(max(amount))
print(sum(amount))
print(amount.index(546698))
