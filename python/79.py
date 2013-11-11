import csv

def generate_compare_digits(key):
    return ((key[0], key[1]), (key[0], key[2]), (key[1], key[2]))
    
    
file = open('keylog.txt', 'r')
keys = [i[0] for i in csv.reader(file)]
    
# we use a dictionary to list how all digits 0-9 are ordered relative to eachother
# in order to see what the code will be like
relative_positions = dict(((str(i), str(j)), 0) for i in range(0, 10) for j in range(0, 10))
for i in keys:
    compare_digits = generate_compare_digits(i)
    for j in compare_digits:
        relative_positions[j] += 1
        
# print the order of digits 
for key in sorted(relative_positions.iterkeys()):
    if relative_positions[key] > 0:
        print (key, relative_positions[key])

    
# from the printed output
# no 4s, no 5s        
# 7 is to the left of everything
# 7 is to the left of 3
# 3 is to the left of 2
# 1 is to the left of 6
# 6 is to the left of 2
# 2 is to the left of 8
# 8 is to the left of 9
# 9 is to the left of 0
# 0 is to the right of everything
    
# 73162890    