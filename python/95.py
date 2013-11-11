import operator
import math
import copy
import pprint
import time

t = time.time()

def recursive_incrementer(factors, upper_bound, increment_location = 0):
    global factors_all
    global factors_of_a_number
    
    
    while True:
        number = reduce(operator.mul, factors)
        if number > 10 ** 6:
            break
        factors_all.append(copy.copy(factors))
        factors_of_a_number[number] += [i for i in factors if i not in factors_of_a_number[number]]
    
        if not (increment_location == len(factors) - 1):
            recursive_incrementer(factors, upper_bound, increment_location + 1)
            
        if increment_location < len(factors) - 1:
            factors[increment_location] += 1
            for i in range(increment_location + 1, len(factors)):
                factors[i] = factors[increment_location]
        else:
            factors[-1] += 1

            
upper_bound = 10 ** 6
factors_of_a_number = dict((i, []) for i in range(2, upper_bound + 1))
factors_all = []
for i in range(2, int(math.log(upper_bound + 1, 2))):
    print i
    recursive_incrementer([2] * i, upper_bound)

sum_of_factors = {}    
for key in factors_of_a_number.keys():
    sum_of_factors[key] = 1 + sum(factors_of_a_number[key])
    

    
    
checked = set([1])
chains = []
for key in sum_of_factors.keys():
    if key in checked:
        continue
    
    chain = [key]
    while True:
        if sum_of_factors[key] in chain:
            chains.append(chain[chain.index(sum_of_factors[key]):])
            break
        elif sum_of_factors[key] > 10 ** 6 or sum_of_factors[key] in checked:
            for j in chain:
                checked.add(j)
            break
        else:
            checked.add(key)
            chain.append(sum_of_factors[key])
            key = sum_of_factors[key] 
        
        
    
    
pprint.pprint(chains)
chains.sort()
longest_chain = chains.pop()
print longest_chain
print min(longest_chain)

print time.time() - t
    
    
    
    
    