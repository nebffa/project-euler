import time
import collections

t = time.time()
n = 1
length = 1
found = False


while not found:
    cubes = []

    while len(str(n ** 3)) == length:
        cubes.append(n ** 3)
        n += 1
    length += 1
        
    dictionaries = []
    for i in cubes:
        dictionaries.append(collections.Counter(str(i)))
        
        
    for i in range(0, len(dictionaries)):
        permutations = 0
        for j in dictionaries:
            if dictionaries[i] == j:
                permutations += 1
            
            if permutations == 5:
                break        
        if permutations == 5:
            break
    if permutations == 5:
        break
                    
print cubes[i]
print time.time() - t