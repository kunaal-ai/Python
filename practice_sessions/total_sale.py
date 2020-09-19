# calculate total sales from string 
mon_sale = "1200"
tue_sale = "1300"
wed_sale = "1400"
thu_sale = "1500"

total_sales = int(mon_sale) + int(tue_sale) + int(wed_sale) + int(thu_sale) 
# this is string value so need to convert in string which can not be done in print statement. 
# concatination can be done only string to string. Str to int not allowed

print('Total sale of week\'s:' + str(total_sales))


