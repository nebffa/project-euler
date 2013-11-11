from math import sqrt as squareroot

i = 143
isFound = False

while not isFound:
    i += 1
    h = i * (2 * i - 1)
    
    if (1 + squareroot(1 + 24 * h)) % 6 == 0:
        isFound = True
        
print h