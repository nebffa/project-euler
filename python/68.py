from itertools import permutations
from time import time

t = time()

digits = range(1, 10)
n_gon_ring = list(permutations("".join([str(i) for i in digits])))
n_gon_ring = [('10',) + i for i in n_gon_ring]

# outer items are:
# n_gon_ring[0], n_gon_ring[3], n_gon_ring[5], n_gon_ring[7], n_gon_ring[9]

def is_magic(n_gon_ring):
    n_gon_ring = [int(i) for i in n_gon_ring]
    top = n_gon_ring[0] + n_gon_ring[1] + n_gon_ring[2]
    right = n_gon_ring[3] + n_gon_ring[2] + n_gon_ring[4]
    bottom = n_gon_ring[5] + n_gon_ring[4] + n_gon_ring[6]
    left = n_gon_ring[7] + n_gon_ring[6] + n_gon_ring[8]
    final = n_gon_ring[9] + n_gon_ring[8] + n_gon_ring[1]

    if top == right:
        if right == bottom:
            if bottom == left:
                if left == final:
                    return True
                    
    return False

def string_value(n_gon_ring):
    top = str(n_gon_ring[0]) + str(n_gon_ring[1]) + str(n_gon_ring[2])
    right = str(n_gon_ring[3]) + str(n_gon_ring[2]) + str(n_gon_ring[4])
    bottom = str(n_gon_ring[5]) + str(n_gon_ring[4]) + str(n_gon_ring[6])
    left = str(n_gon_ring[7]) + str(n_gon_ring[6]) + str(n_gon_ring[8])
    final = str(n_gon_ring[9]) + str(n_gon_ring[8]) + str(n_gon_ring[1])
    lines = [top, right, bottom, left, final]
    
    n_gon_ring = [int(i) for i in n_gon_ring] # convert to list of ints
    min_outer_item = [n_gon_ring[0], n_gon_ring[3], n_gon_ring[5], n_gon_ring[7], n_gon_ring[9]].index(min([n_gon_ring[0], n_gon_ring[3], n_gon_ring[5], n_gon_ring[7], n_gon_ring[9]]))
    
    output_string = ""
    for i in range(0, 5):
        output_string += lines[(i + min_outer_item) % 5]

    return int(output_string)
    
max_value = 0
for i in n_gon_ring:
    if not is_magic(i):
        continue
    
    n_gon_value = string_value(i)
    if max_value < n_gon_value:
        max_value = n_gon_value
        last = i
        
print max_value
print time() - t
    
    