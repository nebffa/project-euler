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
    
    
sumTotal = 0
for i in range(1, 1000000):
    # remove first two characters of bin(i) string as python uses 0b at front to identify as binary
    if checkPalindrome(i) and checkPalindrome(bin(i)[2:]):
        sumTotal += i
        
print sumTotal