# Import random Module
## Option - 1 , import complete module and use any method
import  random
# Use function randint(range_from,to)
print(random.randint(1,9))


## option - 2, import only specefic methods we need 
from random import randint
print(randint(10,19))

# we can import multiple functions from same module 
from random import randint, choice
print(randint(20,30))
print(choice([33,44,55,66,77,88,99]))