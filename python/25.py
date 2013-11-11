termNminusOne = 1
termN = 1
termNumber = 2

while len(str(termN)) < 1000:
    temp = termN
    termN += termNminusOne
    termNminusOne = temp
    termNumber += 1
    
print termNumber