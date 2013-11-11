from time import time
from prime import prime
t = time()


# for finding ways to sum to 100
def count_rec(cursum, level):
    global count_rec_dict
    global ceiling
    global primes
    

    if level == ceiling - 1:
        if cursum == ceiling:
            return 1
        else:
            return 0

    res = 0
    
    if level in primes:
        for i in xrange(0, (ceiling + 1) - cursum, level):
            #print 'prime', level, cursum

            # fetch branch value from the dictionary
            if (cursum + i, level + 1) in count_rec_dict:
                res += count_rec_dict[(cursum + i, level + 1)]
            
            # add branch value to the dictionary
            else:
                count_rec_dict[(cursum + i, level + 1)] = count_rec(cursum + i, level + 1)
                res += count_rec_dict[(cursum + i, level + 1)]
                
                
    else:
        # fetch branch value from the dictionary
        #print 'non-prime', level, cursum
        if (cursum, level + 1) in count_rec_dict:
            res += count_rec_dict[(cursum, level + 1)]
        
        # add branch value to the dictionary
        else:
            count_rec_dict[(cursum, level + 1)] = count_rec(cursum, level + 1)
            res += count_rec_dict[(cursum, level + 1)]
        
    return res


    
# global variable
primes = []
for i in range(1, 1000):
    if prime(i):
        primes.append(i)
        primes.append
primes = set(primes)
       
ceiling = 1   
while True:

    #global variables
    count_rec_dict = {}
    ceiling += 1
    
    print ceiling
    if count_rec(0, 0) > 5000:
        break
        
print ceiling
print time() - t