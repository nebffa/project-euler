import time
from itertools import izip
from itertools import permutations
import collections


# performs Miller-Rabin deterministic test. Essential conditions are: testPrime > 1 and testPrime is odd
def checkPrime(testPrime):
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
    

primesCountLimit = 8
primes = []
for i in range(100001, 1000000, 2):
    if checkPrime(i):
        primes.append(i)
        
t = time.time()
        
masksTemp = list(permutations('00111'))
masks = [k + tuple('0') for k in masksTemp]

for i in primes:
    # apply each mask to each prime
    iNew = [j for j in str(i)]
    for mask in masks:
        primesCount = 0
        problems = 0
        for j in range(0, 10):
            for k in range(0, 6):
                if mask[k] == '1':
                    iNew[k] = str(j)
            if int(''.join(iNew)) in primes:
                primesCount += 1
            else:
                problems += 1
            
            if primesCount == 8:
                break
            
            if problems == 3:
                break
    
        if primesCount == 8:
            break
            
    if primesCount == 8:
        break
        
for k in range(0, 6):
    if mask[k] == '1':
        iNew[k] = str(1)
            
print int(''.join(iNew))
print time.time() - t
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        