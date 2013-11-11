import math
maxTriplets = 0
number = 0
for p in range(1, 1001):
    
    triplets = 0
    solutions = []
    for a in range(1, p):    
        for n in range(1, p):
            if p * 1.0 == 1.0 * n + (a ** 2) / (4 * n) + a + math.fabs(n - (a ** 2) / (4 * n)) and math.floor(1.0 * (a ** 2) / (4 * n)) == 1.0 * (a ** 2) / (4 * n):
                if math.fabs(n - (a ** 2) / (4 * n)) > 0:
                    if min(a, math.fabs(n - (a ** 2) / (4 * n))) not in solutions:
                        #if a 
                        triplets +=  1
                        

                        
                        #print "(p, n, a) = %d" % p, ", ", n, ", ", a
                        #print "(", a, math.fabs(n - (a ** 2) / (4 * n)), n + (a ** 2) / (4 * n), ")"
                        solutions.append(min(a, math.fabs(n - (a ** 2) / (4 * n))))
                        break
                
        
                
    if triplets > maxTriplets:
        maxTriplets = triplets
        number = p
        
print maxTriplets
print number
#print solutions