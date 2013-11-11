import copy
import math
import operator
import time

t = time.time()

def number_of_ones(factors):
    n = 1
    for i in factors:
        n *= i
    
    return n - sum(factors)
    
def recursive_incrementer(factors, upper_bound, increment_location = 0):
    global factors_all
    
    while reduce(operator.mul, factors) <= upper_bound:
        factors_all.append(copy.copy(factors))
    
        if not (increment_location == len(factors) - 1):
            recursive_incrementer(factors, upper_bound, increment_location + 1)
            
        if increment_location < len(factors) - 1:
            factors[increment_location] += 1
            for i in range(increment_location + 1, len(factors)):
                factors[i] = factors[increment_location]
        else:
            factors[-1] += 1
         
            
factors_all = []
for i in range(2, int(math.log(24001, 2))):
    recursive_incrementer([2] * i, upper_bound = 24000)
    
mpsns = {}

for factors in factors_all:
    k = len(factors) + number_of_ones(factors)
    
    if k > 12000:
        continue
    
    N = reduce(operator.mul, factors)

    if mpsns.has_key(k):
        if mpsns[k] > N:
            mpsns[k] = N
    else:
        mpsns[k] = N
 

print sum(set(mpsns.values()))
print time.time() - t