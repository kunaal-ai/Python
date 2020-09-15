
# Comparison 
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

weather = 'Good'

if weather == 'Good':
    print('Weather is Good')
elif weather == 'Bad':
    print('Weather is Bad')
        
else:
    print('Report Missing')    
    
    
# and 
# or
# not
# 0/False/() - empty will be == False
air_quality = False
if weather == 'Good' and air_quality:
    print('Weather is Good and air quality is GOOD')
elif weather == 'Good':
    print('Weather is Good and air quality is Bad')
else:
    print('Report Missing')  
    
logged_in = False
if not logged_in:
    print('Please log in ')
else:
    print('Welcome')

    
        