from decimal import *
from time import time

t = time()

getcontext().prec = 110

sum_digits_total = 0
for i in range(1, 101):
    square_root_number = Decimal(i).sqrt()
    if not square_root_number == int(square_root_number):
    
        square_root_string = str(square_root_number).replace(".", "")[0:100]
        sum_digits_total += sum([int(j) for j in square_root_string])

print sum_digits_total
print time() - t