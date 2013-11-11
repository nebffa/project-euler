from time import time

t = time()
e = [2]
while len(e) != 100:
    if (len(e) + 1) % 3:
        e.append(1)
    else:
        e.append(2 * (len(e) + 1) / 3)
        
numerator = 1
denominator = e.pop()

while e:
    numerator += e.pop() * denominator
    tmp = [numerator, denominator]
    denominator, numerator = (tmp[0], tmp[1])

    
print sum([int(i) for i in str(denominator)])
print time() - t
        

        