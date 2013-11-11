# null for 0, followed by number of letters in 11-19
teens = [0, 6, 6, 8, 8, 7, 7, 9, 8, 8]
# null for 0, followed by number of letters in 1-9
ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
# null for 00, number of letters in 10, 20, ..., 90
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
# number of letters in 100
hundred = [7]
# numbers of letters in 'and'
andString = [3]

lettersInSequence = 0
for i in range(1, 1001):
    lettersInString = 0
    if 1 <= i < 10:
        strInteger = "00" + str(i)
    elif 10 <= i < 100:
        strInteger = "0" + str(i)
    elif 100 <= i < 1000:
        strInteger = str(i)
    

    # number of letters for the hundreds column
    if int(strInteger[0]) == 0:
        lettersInString += 0
    else:
        lettersInString += ones[int(strInteger[0])] + hundred[0]
        
    if i > 100 and i % 100 != 0:
        # if i > 100 and is not 100, 200, ..., 900 we need 'and'
        lettersInString += andString[0]

    if i % 100 == 0:
        # special case - if i % 100 == 0. No 'and' needed
        lettersInString += 0
    else:
        
        # number of letters for the tens and ones column
        if i % 100 < 10:
            lettersInString += ones[int(strInteger[2])]
        elif i % 100 == 10:
            # ten is a special case
            lettersInString += tens[1]
        elif 11 <= i % 100 < 20:
            lettersInString += teens[int(strInteger[2])]
        else:
            lettersInString += tens[int(strInteger[1])] + ones[int(strInteger[2])]
    
    if i == 1000:
        # i = 1000 is a special case
        lettersInString = 11
        
    lettersInSequence += lettersInString
        
print "the number of letters in the sequence is %d" % lettersInSequence