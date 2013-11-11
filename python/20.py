import math
digitsCount = 0

numb = math.factorial(100)
numbString = str(numb)

for i in range(0, len(numbString) - 1):
    digitsCount += int(numbString[i])
    
print digitsCount