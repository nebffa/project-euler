from fractions import gcd
import time
t = time.time()

############ could just use euler's totient function. woohoo thanks guy in thread #73

def reduce_n(n, d): 
    n -= 1
    while gcd(n, d) != 1:
        n -= 1
        
    return n

three_seven_fraction = 1.000000000 * 3 / 7
max_fraction, max_n, max_d = 0  , 0, 0
for i in range(2, 1000000):
    n = i * 3 / 7 + 7
        
    while 1.000000000 * n / i > 1.000000000 * three_seven_fraction:
        n = reduce_n(n, i)
            
        if max_fraction < 1.000000000 * n / i and 1.000000000 * n / i < 1.000000000 * three_seven_fraction:
            max_fraction, max_n, max_i = 1.000000000 * n / i, n, i
            
print max_fraction, max_n, max_i
print time.time() - t