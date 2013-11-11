import time

t = time.time()

arrive = {}
for i in range(1, 568):
    
    j = sum([int(digit) ** 2 for digit in str(i)])
    if j == 1:
        arrive[i] = 0
        continue
    elif j == 89:
        arrive[i] = 1
        continue
        
    while j not in [1, 89]:
        j = sum([int(digit) ** 2 for digit in str(j)])
        
        if j == 1:
            arrive[i] = 0
            continue
        elif j == 89:
            arrive[i] = 1
            continue
        

count = 0
squares = {'0': 0, '1': 1, '2': 4,'3': 9,'4': 16,'5': 25,'6': 36,'7': 49,'8': 64,'9': 81}
for i in xrange(1, 10 ** 7):
    count += arrive[sum([squares[digit] for digit in str(i)])]
            
print count
print time.time() - t