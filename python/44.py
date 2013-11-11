from math import sqrt
isFound = False
k = 1
min = 100000000

while k < 3000:
    k += 1
    print k
    for j in range(1, k):
        
        # test difference for pentagonality
        difference = sum(3 * j + 3 * n - 2 for n in range(1, k - j + 1))
        if (1 + sqrt(1 + 24 * difference)) % 6 != 0:
            continue
         
        # test addition for pentagonality
        addition = j * (3 * j - 1) + difference
        if (1 + sqrt(1 + 24 * addition)) % 6 != 0:
            continue  

        if min > difference:
            min = difference

print min