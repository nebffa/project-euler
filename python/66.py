from math import sqrt
from time import time
from copy import copy
from fractions import gcd

t = time()
def next_level_fraction(fraction):
    temp = [0, 0, 0, 0]
    simplify = gcd(fraction[3], (fraction[1] - fraction[2] ** 2))
    temp[1] = fraction[1]
    temp[0] = fraction[0] * fraction[3] / simplify
    temp[3] = (fraction[1] - fraction[2] ** 2) / simplify
    temp[2] = -fraction[2] * fraction[3] / simplify
    final_level = int(temp[0] * (sqrt(temp[1]) + temp[2]) / temp[3])
    temp[2] += -final_level * temp[3]
    
    return final_level, copy(temp)
    
def simplify_continued_fraction(D, continued_fraction):
    numerator = 1
    denominator = continued_fraction.pop()

    while continued_fraction:
        numerator += continued_fraction.pop() * denominator
        numerator, denominator = denominator, numerator
        
    numerator += int(sqrt(D)) * denominator
        
    return numerator, denominator
    
def diophantine_solution(numerator, denominator, D):
    if numerator ** 2 - D * denominator ** 2 == 1:
        return True
    else:
        return False
    
max_x = 0
max_D = 0
for D in range(2, 1001):
    if int(sqrt(D)) ** 2 == D:
        continue
		
    found = False
    continued_fraction, fractions, fraction = ([], [], [1, D, -int(sqrt(D)), 1])

    while not found:
        final_level, fraction = next_level_fraction(fraction)
        continued_fraction.append(final_level)
        
        if len(continued_fraction) > 1:
            numerator, denominator = simplify_continued_fraction(D, copy(continued_fraction))
        elif len(continued_fraction) == 1:
            denominator = continued_fraction[0]
            numerator = 1 + int(sqrt(D)) * denominator
            
        found = diophantine_solution(numerator, denominator, D)
           
    if numerator > max_x:
        max_x = numerator
        max_D = D
    
print max_D
print time() - t
