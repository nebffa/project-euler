# performs Miller-Rabin deterministic test. Essential conditions are: testPrime > 1 and testPrime is odd
def check_prime(testPrime):
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
    
def append_prime(new_prime, list_of_primes):
    for i in list_of_primes:
        if not (check_prime(int(str(new_prime) + str(i))) and check_prime(int(str(i) + str(new_prime)))):
            # if new_prime does not form primes with any i in list_of_primes, return the old list_of_primes
            return False
            
    # else append new_prime and return the updated list_of_primes
    return True
                
    
    

import time

t = time.time()
primes = []
for i in range(3, 10000, 2):
    if check_prime(i): 
        primes.append(i)

sets = []
for i in primes:
    print i
    for j in sets:
        if append_prime(i, j):
            sets.append(j + [i])
        if len(sets[-1]) == 5:
            print sets[-1]
            print time.time() - t
            raw_input()
            break
           

    for j in primes:
        if i >= j:
            continue
            
        if check_prime(int(str(i) + str(j))) and check_prime(int(str(j) + str(i))):
            sets.append([i, j])


     