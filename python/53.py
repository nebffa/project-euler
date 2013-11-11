import time
from math import factorial as fact

t = time.time()

ways = 0
for n in range(23, 101):
    for r in range(0, n + 1):
        if fact(n) / (fact(r) * fact(n - r)) > 1000000:
            ways += 1
            
            
print ways
print time.time() - t