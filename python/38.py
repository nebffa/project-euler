def getPandi(n):
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test1Pandi = ''

    for i in digits:
        test1Pandi += str(n * digits[i - 1])
        
        if len(test1Pandi) > 9:
            break
        else:
            test2Pandi = test1Pandi
        
    return int(test2Pandi)
        
def checkPandi(n):
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    array = []
    
    for i in str(n):
        array.append(int(i)) 
    array.sort()
    
    # algorithm assumes n is pandidigital and sets out to prove it is not
    isPandi = True
    for i in range(0, len(array) - 1):
        if array[i] != array[i + 1] - 1:
            isPandi = False
            
    return isPandi

        
largestPandi = 0
# by trial and error an upper bound of 10000 was found to get the answer
for i in range(1, 10000):
    testPandi = getPandi(i)
    
    isPandi = checkPandi(testPandi)
    
    if isPandi == True and testPandi > largestPandi:
        largestPandi = testPandi
        
print largestPandi