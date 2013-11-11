import random
from fractions import gcd

# performs Miller-Rabin deterministic test. Essential conditions are: testPrime > 1 and testPrime is odd
def prime(testPrime):
    if testPrime == 2:
        return True
    elif testPrime == 1:
        return False
    elif testPrime % 2 == 0:
        return False

    # fetches the parameters required for test
    s = 0
    d = testPrime - 1
    while d % 2 == 0:
        s += 1
        d = d/2

    # the algorithm assumes testPrime is prime and sets out to prove it is non-prime
    isPrime = True
    # see http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants_of_the_test for more information on the values 'a' takes
    if 4759123141 <= testPrime < 2152302898747:
        aList = [2, 3, 5, 7, 11]
    if 9080191 <= testPrime < 4759123141:
        aList = [2, 7, 61]
    if 1373653 <= testPrime < 9080191:
        aList = [31, 73]           
    if testPrime < 1373653:
        aList = [2, 3]
    if testPrime == 3:
        aList = [2]
    
    for a in aList:
        if pow(a, d, testPrime) != 1:
            compositeTestA = True
        else:
            compositeTestA = False
        
        for r in range(0, s):
            # wikipedia calls for '!= -1' but due to python's pow(a,b,c) function we must use '!= -1 + testPrime'
            if pow(a, (2 ** r) * d, testPrime) != -1 + testPrime:
                compositeTestB = True
            else:
                compositeTestB = False
                break
               
        if compositeTestA & compositeTestB :
            isPrime = False
            break
            
    return isPrime
    
# returns random factor of N
def brent(N):
    if N%2==0:
            return 2
    y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
    g,r,q = 1,1,1
    while g==1:             
            x = y
            for i in range(r):
                    y = ((y*y)%N+c)%N
            k = 0
            while (k<r and g==1):
                    ys = y
                    for i in range(min(m,r-k)):
                            y = ((y*y)%N+c)%N
                            q = q*(abs(x-y))%N
                    g = gcd(q,N)
                    k = k + m
            r = r*2
    if g==N:
            while True:
                    ys = ((ys*ys)%N+c)%N
                    g = gcd(abs(x-ys),N)
                    if g>1:
                            break
    
    return g    

# returns unique prime factors of n
def prime_factors_unique(n, primes_set):
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
    
# returns all prime factors of n
def prime_factors(n, primes_set):
    factors = []

    if type(primes_set) == list:
        primes_set = set(primes_set)
    
    while n != 1:
        if n in primes_set:
            break
        
        factor = brent(n)

        if factor not in primes_set:
            factors += prime_factors(factor, primes_set)
        else:
            factors.append(factor)
        
        n /= factor
    
    if n != 1:
        factors.append(n)
        
    return factors
    
