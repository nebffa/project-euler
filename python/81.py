import csv
from time import time

t = time()

matrix = list(csv.reader(open('TextFiles\matrix.txt', 'r'), quoting = 2))

initial_cell_row = len(matrix) - 1
initial_cell_column = len(matrix) - 1
for diagonal_number in range(2 * (len(matrix) - 1) - 1, -1, -1):

    # the diagonal_number does not easily specify the bottom-left (initial) cell of its row
    # initial_cell_column and initial_cell_row keep track of that bottom-left cell
    if initial_cell_column != 0:
        initial_cell_column -= 1
    else:
        initial_cell_row -= 1
        
    diagonal_cell_coordinates = [initial_cell_row, initial_cell_column]
    for diagonal_element in range(0, len(matrix) - abs(len(matrix) - 1 - diagonal_number)):
        diagonal_cell_coordinates = [initial_cell_row - diagonal_element, initial_cell_column + diagonal_element]
        
        if diagonal_cell_coordinates[0] == len(matrix) - 1:
            matrix[diagonal_cell_coordinates[0]][diagonal_cell_coordinates[1]] += \
                    matrix[diagonal_cell_coordinates[0]][diagonal_cell_coordinates[1] + 1]
        elif diagonal_cell_coordinates[1] == len(matrix) - 1:
            matrix[diagonal_cell_coordinates[0]][diagonal_cell_coordinates[1]] += \
                    matrix[diagonal_cell_coordinates[0] + 1][diagonal_cell_coordinates[1]]
        else:
            matrix[diagonal_cell_coordinates[0]][diagonal_cell_coordinates[1]] += \
                    min(matrix[diagonal_cell_coordinates[0] + 1][diagonal_cell_coordinates[1]], \
                            matrix[diagonal_cell_coordinates[0]][diagonal_cell_coordinates[1] + 1])
                            
print matrix[0][0]
print time() - t
                    
        
                
