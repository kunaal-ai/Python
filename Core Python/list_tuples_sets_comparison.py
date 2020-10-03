
# Mutable : Can change object value after initialization - LIST  
# In-mutable : cam NOT changed - Tuples
# if requirement is not to change the values then use Tuples

# **************      LIST          **********************
# LIST - Mutable - we can change the values 
# ordered
states = ['Ohio','New York','DC','IL']
states[0] = 'California'
print('LIST:',states)

# **************      Tuples          **********************
# Immutable - Can not change values
# Ordered
tuples_states = ('Ohio','New York','DC','IL')
# or () are optional
tuples_states = 'Ohio','New York','DC','IL'

# Uncoment next line and This will fail to print and throw an error, because we can not change the values.
# tuples_states[0] = 'California'
# print(tuples_states)


# **************      SETS          **********************

# Unordered, mutable and unique values
# Removes any duplicate values in sets and print in random order
# More fast in terms of processing

# Let run without duplicate

sets_states = {'Ohio','New York','DC','IL'}
print(sets_states)

# Let run with duplicate
sets_states = {'Ohio','New York','DC','DC','IL','IL'}
print('SET with duplicates:',sets_states)
sets_states.add('Atlanta')
print(sets_states)
# pop - to extract any random value 

# can be useful in case where we need to find what values are shared /not with other sets.
sets_states     =   {'Ohio','New York','Albama','Colorado'}
new_sets_states =   {'Ohio','New York','DC','IL'}
print('Print shared in sets:',sets_states.intersection(new_sets_states)) # print shared values
print('Print NOT shared :',sets_states.difference(new_sets_states))

# combine boh sets values 
print(sets_states.union(new_sets_states))



# ----------------------------------------------------------------------------------
# Ways to initialize empty
# Empty List Syntax
empty_list = [] 
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Set
empty_set = {} # invalid for sets, this is reserved for Dictionaries.
empty_set = set()
