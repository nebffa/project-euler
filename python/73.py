from fractions import gcd
from time import time
t = time()

def numerator_range(denominator):
    lower_bound = denominator / 3
    upper_bound = denominator / 2
	
    while 1.00 * lower_bound <= 1.00 * denominator * 1 / 3:
        lower_bound += 1
		
    while 1.00 * upper_bound >= 1.00 * denominator * 1 / 2:
        upper_bound -= 1
		
    upper_bound += 1
    return lower_bound, upper_bound

	
number_of_fractions = 0
for denominator in range(2, 12001):
    lower_bound, upper_bound = numerator_range(denominator)
	
    for numerator in range(lower_bound, upper_bound):
        if gcd(numerator, denominator) == 1:
            number_of_fractions += 1
    print denominator

print number_of_fractions
print time() - t