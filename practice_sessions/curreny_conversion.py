list_one = [6200,2100,2100,2100,3100,8500,15000]
total = 0
usd = 0
for i in list_one:
    total += i
print(total)
usd = int(total/72) 
print("$"+ str(usd))
print("Total USD to send: " + str(int(usd) + 100) )


