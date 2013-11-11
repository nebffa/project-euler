from time import time
t = time()
count_rec_dict = {}

# for finding ways to sum to 100
def count_rec(cursum, level):
    global count_rec_dict
    
    # 99 is the last integer that we could be using,
    # so prevent the algorithm from going further. 
    if level == 99:
        if cursum == 100:
            return 1
        else:
            return 0

    res = 0
    
    for i in xrange(0, 101-cursum, level+1):
        
        # fetch branch value from the dictionary
        if (cursum+i, level+1) in count_rec_dict:
            res += count_rec_dict[(cursum+i, level+1)]
        
        # add branch value to the dictionary
        else:
            count_rec_dict[(cursum+i, level+1)] = count_rec(cursum+i, level+1)
            res += count_rec_dict[(cursum+i, level+1)]        
        
    return res

print count_rec(0, 0)
print time() - t