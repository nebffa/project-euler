from itertools import groupby
from time import time
from math import sqrt
from fractions import gcd

t = time()
triplets = []
upper_bound = int(sqrt(1500000 / 2))

for n in range(1, upper_bound):
    if n % 100 == 0:
        print n
    for m in range(n + 1, upper_bound):
        if not (m + n) % 2 or gcd(m, n) != 1:
            continue
        
        k_exhausted = False
        k = 0
        while k_exhausted == False:
            k += 1
            triplet = [k * (m ** 2 - n ** 2), k * (2 * m * n), k * (m ** 2 + n ** 2)]
        
            if sum(triplet) > 1500000:
                break
                
            triplets.append(tuple(sorted(triplet)))
        
        
triplets_set = set(triplets)

perimeters = sorted([sum(i) for i in triplets_set])

counter = [len(list(group)) for key, group in groupby(perimeters)]

tally = 0
for i in counter:
    if i == 1:
        tally += 1
print tally
print time() - t