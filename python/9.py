# http://en.wikipedia.org/wiki/Pythagorean_triple#Distribution_of_triples

a, b, c = (0, 0, 0)
aX, bX, cX = (a, b, c)
for a in range(1, 500):
    for n in range(1, 1 + (a ** 2) / 4):
        # criteria for being a pythagorean triplet        
        if (a ** 2) % (4 * n) == 0:
            b = abs(n - (a ** 2) / (4 * n))
            c = n + (a ** 2) / (4 * n)
            
        # exit upon finding pythagorean triplet that sums to 1000
        if a + b + c == 1000:
            break
            
    if a + b + c == 1000:
        print a * b * c
        break
        

            
#print a
#print b
#print c
#print a * b * c