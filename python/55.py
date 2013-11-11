import time

t = time.time()

def check_palindrome(testPalindrome):
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

lychrels = 0
for i in range(1, 10000):
    for j in range(1, 50):
        i += int(str(i)[::-1])
        if check_palindrome(i):
            break
    else:
        lychrels += 1
            
print lychrels

print time.time() - t