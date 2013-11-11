from math import sqrt
from time import time

t = time()
        
    
integer_solutions = 0
max_length = 0
squares = set([i ** 2 for i in range(10000)])

while True:
    
    max_length += 1
    i = max_length
    
    for j in xrange(1, i + 1):
        for k in xrange(1, j + 1):        
            
            if i ** 2 + (k + j) ** 2 in squares:
                integer_solutions += 1
                
    if integer_solutions > 1000000:
            break
    
    if max_length % 100 == 0:
        print "the longest side is %d, and the number of integer solutions is %d" % (max_length, integer_solutions)
        print "time taken: %d" % (time() - t)
    
print max_length
print integer_solutions
print time() - t