import time

t = time.time()
max = 0
for a in range(1, 100):
    for b in range(1, 100):
        sum_digits = sum([int(i) for i in str(a ** b)])
        
        if sum_digits > max:
            max = sum_digits
            
print max

print time.time() - t