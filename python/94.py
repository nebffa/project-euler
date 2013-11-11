import time
import math

t = time.time()

b = [1, 0, 3]
c = [1, 1, 5]
while True:
    b_new = 3 * b[-1] + 3 * b[-2] - b[-3]
    c_new = 3 * c[-1] + 3 * c[-2] - c[-3]
    
    if (2 * b_new + 2 * c_new) > 10 ** 9:
        break
        
    b.append(b_new)
    c.append(c_new)
    
perimeter_sum = 0
for i in range(2, len(b)):
    perimeter_sum += 2 * b[i] + 2 * c[i]
    
print perimeter_sum
print time.time() - t