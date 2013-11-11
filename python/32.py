import collections
import itertools

pandidigitals = []
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pandidigitals = []

for i in range(1, 100):
    duplicate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if i % 10 == 0:
        continue

    for digit in range(0, len(str(i))):
        duplicate.append(int(str(i)[digit]))

    digitsCount = collections.Counter(duplicate)
    remainingDigits = [q for q in digitsCount if digitsCount[q] == 1]

    
    temp = list(itertools.permutations(remainingDigits, 5 - len(str(i))))
    factorTwo = [int("".join(map(str, b))) for b in temp]

    
    product = [number * i for number in factorTwo]
    
    for j in range(0, len(product)):
        checkPandidigital = collections.Counter(str(i) + str(factorTwo[j]) + str(product [j]))
        
        checkDigits = [int(k) for k in checkPandidigital if checkPandidigital[k] == 1]
        checkDigits.sort()
       
        if checkDigits == digits:
            pandidigitals.append(product[j])
            

print set(pandidigitals)
print sum(set(pandidigitals))