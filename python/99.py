'''
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048  37 = 2187.

However, confirming that 632382518061  519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a 
base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.'''


import time
import csv
import math

t = time.time()

simplified_powers = []
f = open('base_exp.txt', 'r')
for base_exp_pair in csv.reader(f):
    log10 = math.log(int(base_exp_pair[0]), 10)
    simplified_powers.append(log10 * int(base_exp_pair[1]))


max_power = max(simplified_powers)
print simplified_powers.index(max_power) + 1

print time.time() - t