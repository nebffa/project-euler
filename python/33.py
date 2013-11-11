import fractions
import collections

def getFraction(i, j):
    numerator = i / fractions.gcd(i, j)
    denominator = j / fractions.gcd(i, j)
    
    return numerator, denominator
    
def commonDigit(i, j, k):
    iNew, jNew = (i, j)

    useArray = collections.Counter(str(i) + str(j) + str(k)) 
    checkDigits = [int(k) for k in useArray if useArray[k] >= 3]
    
    # i
    if len(checkDigits) > 0:
        for digit in range(0, len(str(i))):
            if int(str(i)[digit]) == checkDigits[0]:
                iNew = str(i)[1 - digit]

                
        for digit in range(0, len(str(j))):
            if int(str(j)[digit]) == checkDigits[0]:
                jNew = str(j)[1 - digit]

    return iNew, jNew
    
def compareFractions(i, j, iNew, jNew):
    sameFractions = False
    
    if i != iNew and j != jNew:
        gcd1 = fractions.gcd(i, j)
        gcd2 = fractions.gcd(iNew, jNew)
        #print i, j, iNew, jNew
        
        i /= gcd1
        j /= gcd1
        iNew /= gcd2
        jNew /= gcd2
        
        
        
        if i == iNew and j == jNew:
            sameFractions = True
            print i, j, iNew, jNew
        else:
            sameFractions = False
    
    return sameFractions
    
overallNumerator, overallDenominator = (1, 1)
for i in range(10, 100):
    for j in range(i, 100):
        
        # test 1-9 as common digits
        for k in range(1, 10):
            iNew, jNew = commonDigit(i, j, k)
            

            # fractions do not reduce
            if len(str(iNew)) == 2 or len(str(jNew)) == 2 or i == j:
                continue
                
            # fractions do reduce, test to see if they are equal
            if int(jNew) != 0:
                if compareFractions(i, j, int(iNew), int(jNew)) == True:
                    print i, j, iNew, jNew
                    numerator, denominator = getFraction(i, j)
                    overallNumerator *= numerator
                    overallDenominator *= denominator
                
overallDenominator /= fractions.gcd(overallNumerator, overallDenominator)

print overallDenominator