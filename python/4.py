def checkPalindrome(testPalindrome):
    # the algorithm assumes the number is a palindrome, then sets out to disprove it
    isPalindrome = True
    strPalindrome = str(testPalindrome)
    testLength = len(strPalindrome)
   
    for i in range(0, testLength / 2):
        if strPalindrome[i] != strPalindrome[testLength - 1 - i]:
            isPalindrome = False
            # exit if non-palindromicity is found
            break
           
    return isPalindrome
    

largestPalindrome = 0
lowerBound = 900


for i in range(lowerBound, 1000):
    for j in range(i, 1000):
        testPalindrome = i * j
        isPalindrome = checkPalindrome(testPalindrome)
        
        if (isPalindrome == True and testPalindrome > largestPalindrome):
            largestPalindrome = testPalindrome

print "largestPalindrome = %d" % largestPalindrome
        
