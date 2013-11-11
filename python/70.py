from prime import prime, brent
from time import time
from math import sqrt
import pickle

t = time()
    
def prime_factors(n, primes_set):
    factors = []

    while n != 1:
        if n in primes_set:
            break
        
        factor = brent(n)

        if factor not in primes_set:
            factors += prime_factors(factor, primes_set)
        else:
            factors.append(factor)
            
        while n % factor == 0:
            n /= factor
    
    if n != 1:
        factors.append(n)
        
    return factors
    
def write_primes():
    primes = []
    for i in range(2001, int(sqrt(10000000)) + 1000, 2):
        if prime(i):
            primes.append(i)
            
    primes_file = open('70.txt', 'wb')
    pickle.dump(primes, primes_file)

def read_primes():
    primes_file = open('70.txt', 'r')
    return pickle.load(primes_file)
    
write_primes()
primes = read_primes()
primes_set = set(primes)

min_ratio = 100
for i in primes:
    for j in primes:
        number = i * j
        if number > 10000000:
            continue

        phi = number * (i - 1) * (j - 1) / i / j
        
        ratio = 1.0 * number / phi
        if sorted(str(number)) == sorted(str(phi)) and ratio < min_ratio:
            min_ratio, min_number, min_phi = ratio, number, phi
            print min_ratio, min_number, min_phi
            
print min_number, min_phi
print time() - t