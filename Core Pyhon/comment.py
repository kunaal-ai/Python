# This is single line coment

''' This is doc comment - explaining what class or function does '''

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []
# for i in names:
#     usernames.append(i.lower().replace(' ','_'))
# print(usernames)    

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(' ','_')
print(usernames)
