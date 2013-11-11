def checkAbundant(n):
    sumFactors = 0
    for i in range(1, 1 + n / 2):
        if n % i == 0:
            sumFactors += i
            
    if sumFactors > n:
        isAbundant = True
    else:
        isAbundant = False
        
    return isAbundant
    
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]
    
    
listAbundants = []
for i in range(1, 20162):
    if checkAbundant(i):
        listAbundants.append(i)

sumAbundants = []
for i in range(0, len(listAbundants)):
    for j in range(i, len(listAbundants)):
        if listAbundants[i] + listAbundants[j] < 20162:            
            sumAbundants.append(listAbundants[i] + listAbundants[j])
        else:
            break


sumAbundants = f7(sumAbundants)
        
sumAbundants.sort()
        

sumTotal = 0
for i in range(1, 20162):
    sumTotal += i
    
sumTotal -= sum(sumAbundants)

print sumTotal