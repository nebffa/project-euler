# fetches the parameters required for Miller-Rabin deterministic test
def getParameters(testPrime):
    s = 0
    d = testPrime - 1
    while d % 2 == 0:
        s += 1
        d = d/2
    return s, d
    
# performs Miller-Rabin deterministic test. Essential conditions are: testPrime > 3 and testPrime is odd
# (wikipedia article says > 1, but by using the approximation and not the 'proper' algorithm for a, the case of testPrime = 3 uses a = [2, 3] though it should only use a = [2])
def checkPrime(testPrime, s, d):
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
    
def testChain(a, b):
    isPrime = True
    chainLength = 0
    while isPrime == True:
        chainLength += 1
        n = chainLength ** 2 + chainLength * a + b
        if n < 3:
            break
        
        s, d = getParameters(n)
        isPrime = checkPrime(n, s, d)
        
        if n == 3:
            isPrime = True
        
    return chainLength


longestChain = 0
product = 0
for a in range(-999, 1000, 2):
    for b in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, \
    89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, \
    173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, \
    263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, \
    359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, \
    457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, \
    569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, \
    659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, \
    769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, \
    881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, \
    997]:

        chainLength = testChain(a, b)
        
        if chainLength > longestChain:
            longestChain = chainLength
            product = a * b
            
print product
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

