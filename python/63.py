import time

t = time.time()
n = 0

for i in range(1, 10):
    j = 1
    stop = False
    
    while not stop:
        if len(str(i ** j)) == j:
            n += 1
            j += 1
        else:
            stop = True

print n
print time.time() - t