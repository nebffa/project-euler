def amicableSum(numb):
	factorSum = 0
	for i in range(1, 1 + numb / 2):
		if numb % i == 0:
			factorSum += i
			
	return factorSum


totalSum = 0

for i in range(1, 10000):
	pair = amicableSum(i)
	
	if amicableSum(pair) == i and pair != i:
		# i and pair are amicable numbers
		totalSum += i
			
	
print totalSum
		