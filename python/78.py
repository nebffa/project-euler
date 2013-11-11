from time import time

t = time()

def pentagonal_number(n):
    n = ((n + 1) / 2) * ((n % 2) * 2 - 1)
    return n * (3 * n - 1) / 2

pentagonal_numbers = [1]
partition_level = 0
while True:
    partition_level += 1
    partition = 0
    i = 1
    flip_bit = -1
    while True:
        g = pentagonal_number(i)
        if g > partition_level:
            break
        if i % 2 == 1:
            flip_bit *= -1
        partition += flip_bit * pentagonal_numbers[partition_level - g]
        i += 1
    pentagonal_numbers.append(partition)
    if partition % 1000000 == 0:
        break
        
print partition_level
print time() - t