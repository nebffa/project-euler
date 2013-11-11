import time
import itertools
import pprint

t = time.time()

def valid(die_pair, six_or_nine_squares, squares):
    for square in six_or_nine_squares:
        if square in die_pair[0] and (6 in die_pair[1] or 9 in die_pair[1]):
            pass
        elif square in die_pair[1] and (6 in die_pair[0] or 9 in die_pair[0]):
            pass
        else:
            return False
            
    for square in squares:
        if square[0] in die_pair[0] and square[1] in die_pair[1]:
            pass
        elif square[0] in die_pair[1] and square[1] in die_pair[0]:
            pass
        else:
            return False
    
    return True
    

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

six_or_nine_squares = [0, 1, 3, 4] # the digit of the square that is not 6 or 9 - 09, 16, 36, 49, 64
squares = [[0, 1], [0, 4], [2, 5], [8, 1]]
# all digits are necessary except 7

die_pairs = set()
for first_die in itertools.combinations(digits, 6):
    for second_die in itertools.combinations(digits, 6):
        die_pairs.add((first_die, second_die))

valid_pairs = []
for die_pair in die_pairs:
    if valid(die_pair, six_or_nine_squares, squares):
        valid_pairs.append(sorted(die_pair))
            
valid_pairs = [tuple(i) for i in valid_pairs]
print len(set(valid_pairs))

print time.time() - t