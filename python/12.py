triangleNumber = 0
numbFactors = 0
s = 0
while numbFactors <= 500:
    s += 1
    triangleNumber += s
    numbFactors = 0
    import math
    for i in range(1, int(math.sqrt(triangleNumber)) - 1):
        if triangleNumber % i == 0:
            numbFactors += 2
        
    if int(triangleNumber) ** 2 == triangleNumber:
        numbFactors += 1
        
print triangleNumber