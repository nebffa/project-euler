numb = 2 ** 1000

strNumb = str(numb)
strLen = len(strNumb)
digitsSum = 0
for i in range(0, strLen):
    digitsSum += int(strNumb[i])
    
print "sum of digits = %d" % digitsSum