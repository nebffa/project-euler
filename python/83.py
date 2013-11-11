import csv
from time import time

t = time()
matrix = list(csv.reader(open('TextFiles\matrix.txt', 'r'), quoting = 2))

def shortest_distance(matrix, row, column):
    right = 0
    down = 0
    up_right_L = 0
    left_down_L = 0
    
    options = []
    if row == len(matrix) - 1:
        right = matrix[row][column + 1]
        options.append(right)
    elif column == len(matrix) - 1:
        down = matrix[row + 1][column]
        options.append(down)
    else:
        right = matrix[row][column + 1]
        down = matrix[row + 1][column]
        options.append(right)
        options.append(down)
        
    if row > 0 and column < len(matrix) - 2:
        up_right_L = matrix[row - 1][column] + matrix[row - 1][column + 1] + \
                matrix[row - 1][column + 2]
        options.append(up_right_L)
    
    if row < len(matrix) - 2 and column > 0:
            
        left_down_L = matrix[row][column - 1] + matrix[row + 1][column - 1] + \
                matrix[row + 2][column - 1]
        options.append(left_down_L)

    
    return min(options)
    
    
initial_cell_row = len(matrix) - 1
initial_cell_column = len(matrix) - 1
for diagonal_number in range(2 * (len(matrix) - 1) - 1, -1, -1):

    # the diagonal_number does not easily specify the bottom-left (initial) cell of its row
    # initial_cell_column and initial_cell_row keep track of that bottom-left cell
    if initial_cell_column != 0:
        initial_cell_column -= 1
    else:
        initial_cell_row -= 1
        
    add_to_diag = []
    diagonal_cell_coordinates = [initial_cell_row, initial_cell_column]
    for diagonal_element in range(0, len(matrix) - abs(len(matrix) - 1 - diagonal_number)):
        diagonal_cell_coordinates = [initial_cell_row - diagonal_element, initial_cell_column + diagonal_element]
        
        add_to_diag.append(shortest_distance(matrix, diagonal_cell_coordinates[0], diagonal_cell_coordinates[1]))
        
    for diagonal_element in range(0, len(matrix) - abs(len(matrix) - 1 - diagonal_number)):
        diagonal_cell_coordinates = [initial_cell_row - diagonal_element, initial_cell_column + diagonal_element]
        matrix[diagonal_cell_coordinates[0]][diagonal_cell_coordinates[1]] += \
                add_to_diag[diagonal_element]

        
print matrix[0][0]
print time() - t