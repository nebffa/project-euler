from prime import prime
from math import sqrt
from time import time

t = time()

square_max = 7072
cube_max = 369
quart_max = 85

primes = [i for i in range(2, square_max + 1) if prime(i)]
squares = [i for i in primes if i <= square_max]
cubes = [i for i in primes if i <= cube_max]
quarts = [i for i in primes if i <= quart_max]

numbers = []
for square in squares:
    sum = square ** 2
    
    for cube in cubes:
        sum += cube ** 3
        
        if sum >= 50000000:
            sum -= cube ** 3
            break
        
        for quart in quarts:
            sum += quart ** 4
            
            if sum < 50000000:

                numbers.append(sum)
            else:
                sum -= quart ** 4
                break
                
            sum -= quart ** 4
            
            
        sum -= cube ** 3
        
print len(set(numbers))
print time() - t