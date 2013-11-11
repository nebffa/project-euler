numTotal = 0

for i in range(100, 500000):
    indivTotal = 0
    strNumber = str(i)
    
    for j in range(0, len(str(i))):
        indivTotal += int(str(i)[j]) ** 5
        
    if indivTotal == i:
        numTotal += i
        
print numTotal