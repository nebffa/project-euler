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
    if testPrime == 3:
        return True
    if testPrime == 1:
        return False
    
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


sumTotal = 0
numbTruncatables = 0
i = 9

while numbTruncatables != 11:
    i += 2
    s, d = getParameters(i)
    isPrime = checkPrime(i, s, d)
    
    # i is prime, now check its truncations
    if isPrime == True:
        truncatable = True
        for j in range(1, len(str(i))):
            isRight = int(str(i)[:-j])
            if isRight == 2:
                isRightPrime = True
            elif isRight == 1 or isRight % 2 == 0:
                isRightPrime = False
            else:
                s, d = getParameters(isRight)
                isRightPrime = checkPrime(isRight, s, d)
                
            
            isLeft = int(str(i)[j:])
            if isLeft == 2:
                isLeftPrime = True
            elif isLeft == 1 or isLeft % 2 == 0:
                isLeftPrime = False
            else:
                s, d = getParameters(isLeft)
                isLeftPrime = checkPrime(isLeft, s, d)
                
            
            if isRightPrime & isLeftPrime:
                # both truncations from left and right are prime
                pass
            else:
                truncatable = False
                break
                
        if truncatable == True:
            print i
            numbTruncatables += 1
            sumTotal += i

print sumTotal




















    