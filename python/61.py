import math
import itertools
import time

t = time.time()

def num_type(i):
    type = []
    if (-1 + math.sqrt(1 + 8 * i)) % 2 == 0:
        type.append(1)
    if math.sqrt(4 * i) % 2 == 0:
        type.append(2)
    if (1 + math.sqrt(1 + 24 * i)) % 6 == 0:
        type.append(3)
    if (1 + math.sqrt(1 + 8 * i)) % 4 == 0:
        type.append(4)
    if (3 + math.sqrt(9 + 40 * i)) % 10 == 0:
        type.append(5)
    if (1 + math.sqrt(1 + 3 * i)) % 3 == 0:
        type.append(6)
        
    return type
    
def break_chain(k1, k2):
    if str(k1)[-2:] == str(k2)[:2]:
        return False
    else:
        return True
        
def check_chain(list):
    nums = [False, False, False, False, False, False]
    for i in list:
        if 1 in i:
            nums[0] = True
        if 2 in i:
            nums[1] = True
        if 3 in i:
            nums[2] = True
        if 4 in i:
            nums[3] = True
        if 5 in i:
            nums[4] = True
        if 6 in i:
            nums[5] = True
            
    if nums[0] and nums[1] and nums[2] and nums[3] and nums[4] and nums[5]:
        return True
    else:
        return False
    

nums = [[], [], [], [], [], []]
for i in range(1000, 10000):
    if (-1 + math.sqrt(1 + 8 * i)) % 2 == 0:
        nums[0].append(i)
    if math.sqrt(4 * i) % 2 == 0:
        nums[1].append(i)
    if (1 + math.sqrt(1 + 24 * i)) % 6 == 0:
        nums[2].append(i)
    if (1 + math.sqrt(1 + 8 * i)) % 4 == 0:
        nums[3].append(i)
    if (3 + math.sqrt(9 + 40 * i)) % 10 == 0:
        nums[4].append(i)
    if (1 + math.sqrt(1 + 3 * i)) % 3 == 0:
        nums[5].append(i)
        
sequences = list(itertools.permutations([0, 1, 2, 3, 4, 5]))
ways = 0
set_type_1, set_type_2, set_type_3, set_type_4, set_type_5, set_type_6 = ([], [], [], [], [], [])
for i in sequences:
    for n1 in nums[i[0]]:
        set_type_1 = []
        set_type_1.append(num_type(n1))


        for n2 in nums[i[1]]:
            set_type_2 = list(set_type_1)
            set_type_2.append(num_type(n2))
            # a true value here means the two numbers are not cyclic
            if break_chain(n1, n2):
                continue

            for n3 in nums[i[2]]:
                set_type_3 = list(set_type_2)
                set_type_3.append(num_type(n3))
                # a true value here means the two numbers are not cyclic
                if break_chain(n2, n3):
                    continue    
                    
                for n4 in nums[i[3]]:
                    set_type_4 = list(set_type_3)
                    set_type_4.append(num_type(n4))
                    # a true value here means the two numbers are not cyclic
                    if break_chain(n3, n4):
                        continue      
                        
                    for n5 in nums[i[4]]:
                        set_type_5 = list(set_type_4)
                        set_type_5.append(num_type(n5))
                        # a true value here means the two numbers are not cyclic
                        if break_chain(n4, n5):
                            continue      
                            
                        for n6 in nums[i[5]]:
                            set_type_6 = list(set_type_5)
                            set_type_6.append(num_type(n6))
                            # a true value here means the two numbers are not cyclic
                            if break_chain(n5, n6):
                                continue    
                            if break_chain(n6, n1):
                                continue
                
                            if check_chain(set_type_6):
                                print n1, n2, n3, n4, n5, n6
                                print n1 + n2 + n3 + n4 + n5 + n6


							
                            #for j in range(0, 6):
                            #    if len(set_type_6[j]) != 1:
                            #        break
                            #else:
                            #    print n1, n2, n3, n4, n5, n6
                            #    print set_type_6
									
print time.time() - t
                
                
                
                
                
                
                
                