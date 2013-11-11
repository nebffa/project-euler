import time

t = time.time()    

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


n = 1
numb_primes = 3
while 1.00 * numb_primes / (4 * n + 1) > 0.1:
    n += 1
    if check_prime(4 * n ** 2 + 4 * n + 1):
        numb_primes += 1
        #primes.remove(4 * n ** 2 + 4 * n + 1)
    if check_prime(4 * n ** 2 - 2 * n + 1):
        numb_primes += 1
        #primes.remove(4 * n ** 2 - 2 * n + 1)
    if check_prime(4 * n ** 2 + 1):
        numb_primes += 1
        #primes.remove(4 * n ** 2 + 1)
    if check_prime(4 * n ** 2 + 2 * n + 1):
        numb_primes += 1
        #primes.remove(4 * n ** 2 + 2 * n + 1)
        
print 2 * n + 1
print time.time() - t
