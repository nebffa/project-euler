from collections import Counter
import time

t = time.time()

i = 1
isFound = False
while not isFound:
    if Counter(str(i)) == Counter(str(2 * i)) == Counter(str(3 * i)) == Counter(str(4 * i)) == Counter(str(5 * i)) == Counter(str(6 * i)):
        isFound = True
    else:
        i += 1
        
print i
print time.time() - t