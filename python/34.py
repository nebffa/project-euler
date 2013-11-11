import math
print sum([x for x in range(3, 1000000) if sum([math.factorial(int(j)) for j in str(x)]) == x])