from prime import prime, brent
from time import time

t = time()
def prime_factors(n, primes_set):
    a = n
    factors = []

    while n != 1:
        if n in primes_set:
            break
        
        factor = brent(n)

        if not factor in primes_set:
            factors += prime_factors(factor, primes_set)
        else:
            factors.append(factor)

        n /= factor
    
    if n != 1:
        factors.append(n)
        
    return set(factors)
    
primes = []
for i in range(2, 1000000):
    if prime(i):
        primes.append(i)
primes_set = set(primes)

totient_values_tally = 0
for number in range(2, 1000001):
    if number in primes_set:
        totient_values_tally += number - 1
    else:
        j = number
        prime_factors_list_denominator = prime_factors(number, primes_set)
        for i in prime_factors_list_denominator:
            j = j * (i - 1) / i
        totient_values_tally += j
    
print totient_values_tally
print time() - t    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



