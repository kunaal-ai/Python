#
# Program to calculate number of weeks and days from given integer value
#
def time_days(days):
    week = days // 7
    days = days % 7
    return f'{week} Week(s) and {days} day(s)'
print(time_days(100))    