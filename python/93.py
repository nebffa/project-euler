import itertools
import decimal
import pprint
import operator
import copy
import time

t = time.time()

def reduce_partition(partition, operator_chain):
    operator_chain = copy.copy(operator_chain)
    for i in range(len(partition)):
        if type(partition[i]) == list:
            partition[i] = reduce(operator_chain.pop(i), partition[i])
            
    while len(partition) > 1:
        partition[0] = operator_chain.pop()(partition[0], partition[1])
        partition.pop(1)
        
    return partition[0]
    
def select_operator_sets(partition):
    types = {
                'Decimal': 0,
                'list': 0
            }
    for i in partition:
        if type(i) == decimal.Decimal:
            types['Decimal'] += 1
        elif type(i) == list:
            types['list'] += 1
            
    if types['Decimal'] == 2: #  and types['list'] == 1
        return 3 # 1, 1, 2
    elif types['Decimal'] == 0 and types['list'] == 2:
        return 3 # 2, 2
    elif types['Decimal'] == 1: # and types['list'] == 1 
        return 2 # 1, 3
    elif types['Decimal'] == 4:
        return 3 # 1, 1, 1, 1
    else: #elif types['Decimal'] == 0 and types['list'] == 1:
        return 1 # 4


digits = [decimal.Decimal(i) for i in range(1, 10)]
digit_sets = [list(i) for i in itertools.combinations(digits, 4)]
operators = [operator.add, operator.sub, operator.mul, operator.div]
all_operator_sets = {
                    1: [list(i) for i in itertools.product(operators, repeat = 1)], 
                    2: [list(i) for i in itertools.product(operators, repeat = 2)], 
                    3: [list(i) for i in itertools.product(operators, repeat = 3)]
                }
        
digit_set_partitions = []
for digit_set in digit_sets:
    digit_set_partitions.append([])

    for i in itertools.permutations(digit_set, 4):
        digit_set_partitions[-1].append(list(i)) # 1, 1, 1, 1
    
    digit_set_partitions[-1].append([list(digit_set)]) # 4
    
    for i in itertools.combinations(digit_set, 2):
        segment = list(i)
        leftover = [j for j in digit_set if j not in segment]
        for j in itertools.permutations([segment] + leftover, 3):
            digit_set_partitions[-1].append(list(j)) # 1, 1, 2
        for j in itertools.permutations([segment, leftover], 2):
            digit_set_partitions[-1].append(list(j)) # 2, 2
        
    for i in digit_set:
        segment = [i]
        leftover = [j for j in digit_set if j not in segment]
        for j in itertools.permutations(segment + [leftover], 2):
            digit_set_partitions[-1].append(list(j)) # 1, 3

max_integer_chain = 0
for digit_set in digit_set_partitions:
    integers_formed = []
    for source_partition in digit_set:
        

        operator_sets = all_operator_sets[select_operator_sets(source_partition)]
        for operator_set in operator_sets:
            # we break down a partition in 4^1 or 4^2 or 4^3 = 4, 16 or 64 ways
            # hence we need to use copies of the original partition, so as to not modify it
        
            partition = copy.copy(source_partition)
        
            
            result = reduce_partition(partition, operator_set)
            if int(result) == result and result > 0 and result not in integers_formed:
                integers_formed.append(int(result))
                
    integers_formed.sort()
    i = 0

    while True:
        if i + 1 == len(integers_formed):
            break
        elif integers_formed[i] + 1 != integers_formed[i + 1]:
            break
        else:
            i += 1
    
    if max_integer_chain < i + 1:
        max_integer_chain = i + 1
        max_digit_set = digit_set[0]
        
print max_digit_set, max_integer_chain
print time.time() - t
        
        