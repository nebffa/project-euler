import csv
from time import time

t = time()
        
# generates two-column slice of the matrix
def generate_matrix_slice(matrix, column):
    matrix_slice = [[i[column]] for i in matrix]
    for i in range(len(matrix_slice)):
        matrix_slice[i].append(matrix[i][column + 1])
        
    return matrix_slice

def shortest_distance(matrix_slice, row):
    upper_bound = matrix_slice[row][1]
    
    up_offset = 0
    up_total = 0
    
    while True:
        up_offset += 1
        if row - up_offset < 0:
            break
        
        up_total += matrix_slice[row - up_offset][0]
        
        if up_total > upper_bound:
            break
        
        test_distance = up_total + matrix_slice[row - up_offset][1]
        if upper_bound > test_distance:
            upper_bound = test_distance
            
    down_offset = 0
    down_total = 0
    while True:
        down_offset += 1
        if row + down_offset > len(matrix_slice) - 1:
            break
        
        down_total += matrix_slice[row + down_offset][0]
        
        if down_total > upper_bound:
            break
            
        test_distance = down_total + matrix_slice[row + down_offset][1]
        if upper_bound > test_distance:
            upper_bound = test_distance
            
    return upper_bound

    
matrix = list(csv.reader(open('TextFiles\matrix.txt', 'r'), quoting = 2)) 
    
for column in range(len(matrix) - 2, -1, -1):
    matrix_slice = generate_matrix_slice(matrix, column)
        
    for row in range(len(matrix)):
        matrix[row][column] += shortest_distance(matrix_slice, row)
        
print min([i[0] for i in matrix])
print time() - t