from math import sqrt
from fractions import gcd
from copy import copy
import time

t = time.time()

def period_length(n):

    # [0] is coefficient of sqrt, [1] is the n, [2] is the addition to the numerator, [3] is the denominator
    
    fraction = [1, n, -int(sqrt(n)), 1]
    fractions = []
    fractions.append(fraction)
    temp = [0, n, 0, 0]
    found = False
    
    while not found:
    
        simplify = gcd(fraction[3], (fraction[1] - fraction[2] ** 2))
        temp[0] = fraction[0] * fraction[3] / simplify
        temp[3] = (fraction[1] - fraction[2] ** 2) / simplify
        temp[2] = -fraction[2] * fraction[3] / simplify
        a = int(temp[0] * (sqrt(temp[1]) + temp[2]) / temp[3])
        temp[2] += -a * temp[3]
        
        fraction = copy(temp)
        
        if fraction in fractions:
            found = True
    
        fractions.append(fraction)

    return len(fractions) - fractions.index(fraction) - 1
    
odd_periods = 0
for i in range(2, 10001):

    if int(sqrt(i)) ** 2 == i:
        continue
    
    if not (period_length(i) % 2 == 0):
        odd_periods += 1
    
print odd_periods
print time.time() - t
