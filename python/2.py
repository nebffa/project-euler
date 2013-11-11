nMinusTwoValue = 1
nMinusOneValue = 2
# nValue is the '3rd' number - i.e. 3 + 5 = 8, 8 will be nValue
nValue = 0
# start the total Fibonacci stack at 2 as nValue will start above 2
stackFibonacci = 2


while nMinusTwoValue + nMinusOneValue < 4000000:
    nValue = nMinusTwoValue + nMinusOneValue
	
    if 2 * (nValue / 2) == nValue:
        stackFibonacci = stackFibonacci + nValue
    
    nMinusTwoValue = nMinusOneValue
    nMinusOneValue = nValue

print stackFibonacci
