def property(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    
    for i in range(0, 7):
        if int(n[1 + i : 4 + i]) % primes[i]:
            return False
            
    return True
    
    
import itertools
perms = list(itertools.permutations('0123456789'))
pandiList = ["".join(map(str, b)) for b in perms]
pandiList.sort()
sumTotal = 0

for i in pandiList:
    if property(i):
        sumTotal += int(i)
        
print sumTotal
