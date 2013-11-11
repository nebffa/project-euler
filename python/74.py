from math import factorial
from time import time
import pickle

t = time()
def write_factorials():
    digit_factorials = [factorial(i) for i in range(0, 10)]
    factorials = []
    for seed in range(1, 10000000):
        factorials.append(sum([digit_factorials[int(i)] for i in str(seed)]))
            
    factorials_file = open('74.txt', 'wb')
    pickle.dump(factorials, factorials_file)

def read_factorials():
    factorials_file = open('74.txt', 'r')
    return pickle.load(factorials_file)
    
#write_factorials()
factorials = read_factorials()

loop_items = [2, 145, 169, 871, 872, 1454, 40585, 45361, 45362, 363601]
loop1, loop2, loop3 = [2, 145, 40585], [871, 45361, 872, 45362], [169, 363601, 1454]
loop_lengths = [1, 1]
    
numb_sixty_loops = 0
for seed in range(2, 1000000):
#for seed in range(69, 70):
    descendent = seed
    numb_non_repeats = 0
    while descendent not in loop_items:
        #if seed > 974300:
        #    print seed, descendent
        descendent = factorials[descendent - 1]
        numb_non_repeats += 1
    
    if descendent in loop_lengths:
        pass
    elif descendent in loop1:
        numb_non_repeats += 1
    elif descendent in loop2:
        numb_non_repeats += 2
    else:
        numb_non_repeats += 3
    
    if numb_non_repeats == 60:
        numb_sixty_loops += 1
        
    #if numb_non_repeats > 60:
    #    print "ALERT ALERT ALERT"
    #    raw_input()

print numb_sixty_loops
print time() - t
