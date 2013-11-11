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
    
primes = [2]
for i in range(3, 1000000, 2):
    if checkPrime(i):
        primes.append(i)
        
chain = []        
i = 99000
while i < 1000000:
    i += 1
    
        
    numbDivisors = 0
    for j in primes:
        # i does not have 4 prime factors
        
        
        if i <= j :
            chain = []
            break
            
        # is j a prime factor of i?
        if not i % j:
            numbDivisors += 1
            
        if numbDivisors == 4:
            chain.append(i)
            break
            
    else:
        chain = []
    
    if len(chain) == 4:
        break
    elif len(chain) == 3:
        print chain
        
print chain
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    