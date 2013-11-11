months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthsLeap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 1/1/1901 is Tuesday which is 1 in 0, 1, 2, ..., 6
currentDay = 1
# 1/1/1901 is in January which is 0 in 0, 1, 2, ..., 11
currentMonth = 0
currentYear = 1901

def runMonth(months, currentDay, currentMonth):
    dayCounter = 1
    
    while dayCounter <= months[currentMonth]:
        dayCounter += 1
        currentDay += 1
        
    currentDay = currentDay % 7
    currentMonth += 1
    return currentDay, currentMonth
    
counterSunday = 0
while currentYear < 2001:
    while currentMonth != 12:
        if currentDay == 6:
            # if first day of month is Sunday increment the counter
            counterSunday += 1
        
        # find first day of next month
        if currentYear % 4 != 0:
            # non leap-year
            currentDay, currentMonth = runMonth(months, currentDay, currentMonth)
        else:
            # leap-year
            currentDay, currentMonth = runMonth(monthsLeap, currentDay, currentMonth)

        
    # new year - reset months and increment years
    currentMonth = 0
    currentYear += 1
    
print counterSunday