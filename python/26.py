# calculates the next decimal value
def remaindersExtend(remainder, divisor):
    remainder *= 10
    newRemainder= remainder % divisor
    
    return newRemainder
    
# checks if a boundary is found for the cycle, 
def checkCycle(remainders):
    countRemainders = collections.Counter(remainders)
    repeatedValue = [i for i in countRemainders if countRemainders[i]>1]
    
    if len(repeatedValue) == 1:
        # cycle is complete
        stopCycle = True
        boundValue = repeatedValue[0]
    else:
        # cycle is not complete - keep going
        stopCycle = False
        boundValue = -1

    return stopCycle, boundValue
        
        
import collections
stopCycle = False
maxLength = 0
maxNumber = 0
remainders = [1]

for i in range(1, 13):

    remainders = [10 % i]
    stopCycle = False
    
    while stopCycle == False:

        newRemainder = remaindersExtend(remainders[len(remainders) - 1], i)
        remainders.append(newRemainder)
        stopCycle, boundValue = checkCycle(remainders)

    # .index(a, b) searches for the fisrt instance of a starting from index b
    firstIndex = remainders.index(boundValue, 0)
    secondIndex = remainders.index(boundValue, firstIndex + 1)
        
    if secondIndex - firstIndex > maxLength:
        maxLength = secondIndex - firstIndex
        maxNumber = i
        
print maxNumber




