import csv
import copy
import random
import time

t = time.time()

def blocks(sudoku): # returns small_grid, a list
    small_grid = [[[], [], []], [[], [], []], [[], [], []]]
    
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] != 0:
                small_grid[row / 3][column / 3].append(sudoku[row][column])
                
    return small_grid

def certain_check_1(sudoku, small_grid, row, column):
    if sudoku[row][column] != 0:
        return
    
    possibilities = range(1, 10)
    
    for rw_check in range(9):
        if rw_check == row:
            continue
        if sudoku[rw_check][column] in possibilities:
            possibilities.remove(sudoku[rw_check][column])
    for cl_check in range(9):
        if cl_check == column:
            continue
        if sudoku[row][cl_check] in possibilities:
            possibilities.remove(sudoku[row][cl_check])
    
    for i in small_grid[row / 3][column / 3]:
        if i in possibilities:
            possibilities.remove(i)
            
    if len(possibilities) == 1:
        small_grid[row / 3][column / 3].append(possibilities[0])
        sudoku[row][column] = possibilities[0]
        changed = True
    else:
        changed = False

    return changed
    
def certain_check_2(sudoku, small_grid):
    possibilities = dict(((i, j), range(1, 10)) for i in range(9) for j in range(9))
            
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] != 0:
                possibilities[(row, column)] = []
            else:
                for value in small_grid[row / 3][column / 3]:
                    possibilities[(row, column)].remove(value)
            
            for row_check in range(9):
                if sudoku[row_check][column] in possibilities[(row, column)]:
                    possibilities[(row, column)].remove(sudoku[row_check][column])
            for column_check in range(9):
                if sudoku[row][column_check] in possibilities[(row, column)]:
                    possibilities[(row, column)].remove(sudoku[row][column_check])
            
    # now to reverse things
    values_to_coordinates = [[dict((i, []) for i in range(1, 10)) for i in range(3)] for i in range(3)]
    for row in range(9):
        for column in range(9):
            for value in possibilities[row, column]:
                values_to_coordinates[row / 3][column / 3][value].append((row, column))

    changed = False
    for small_grid_column in values_to_coordinates:
        for dictionary in small_grid_column:
            for key in dictionary:
                if len(dictionary[key]) == 1:
                    changed = True
                    sudoku[dictionary[key][0][0]][dictionary[key][0][1]] = key
                    small_grid[dictionary[key][0][0] / 3][dictionary[key][0][1] / 3].append(key)                        
    return changed
        
def uncertain_check(sudoku):
    possibilities = dict(((i, j), range(1, 10)) for i in range(9) for j in range(9))
            
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] != 0:
                possibilities[(row, column)] = []
            else:
                for value in small_grid[row / 3][column / 3]:
                    possibilities[(row, column)].remove(value)
            
            for row_check in range(9):
                if sudoku[row_check][column] in possibilities[(row, column)]:
                    possibilities[(row, column)].remove(sudoku[row_check][column])
            for column_check in range(9):
                if sudoku[row][column_check] in possibilities[(row, column)]:
                    possibilities[(row, column)].remove(sudoku[row][column_check])
            
    # now to reverse things
    values_to_coordinates = [[dict((i, []) for i in range(1, 10)) for i in range(3)] for i in range(3)]
    for row in range(9):
        for column in range(9):
            for value in possibilities[row, column]:
                values_to_coordinates[row / 3][column / 3][value].append((row, column))

    for small_grid_column in values_to_coordinates:
        for dictionary in small_grid_column:
            for place in sorted(dictionary, key = lambda x: len(dictionary[x])):
                if len(dictionary[place]) > 1:
                    choice = random.randint(0, len(dictionary[place]) - 1)
                    sudoku[dictionary[place][choice][0]][dictionary[place][choice][1]] = place
                    small_grid[dictionary[place][0][0] / 3][dictionary[place][0][1] / 3].append(place)                        
                    return True
    return False
       
def is_solution(sudoku):
    small_grid = blocks(sudoku)
    for smaller_grid in small_grid:
        for grid in smaller_grid:
            if not sorted(grid) == range(1, 10):
                return False
    for row in sudoku:
        if not sorted(row) == range(1, 10):
            return False
    for column_number in range(9):
        column = [sudoku[i][column_number] for i in range(9)]
        if not sorted(column) == range(1, 10):
            return False
    
    return True     
    
    
sudokus = []
for line in  csv.reader(open('TextFiles\sudoku.txt', 'r')):
    if "Grid" in line[0]:
        sudokus.append([])
    else:
        sudokus[-1].append([int(i) for i in line[0]])

i = -1
sum = 0
for sudoku in sudokus:
    sudoku = copy.deepcopy(sudoku)
    small_grid = blocks(sudoku)

    cached = False
    while True:
        while True: # this part is certain!
            is_complete = True

            while True:
                is_complete = True
                
                for row in range(9):
                    for column in range(9):
                        if sudoku[row][column] == 0:
                            if certain_check_1(sudoku, small_grid, row, column): # the sudoku was changed
                                is_complete = False
                        
                if is_complete:
                    break
            
            if certain_check_2(sudoku, small_grid): # the sudoku was changed
                is_complete = False
                
            if is_complete:
                break

        if is_solution(sudoku):
            sum += int(str(sudoku[0][0]) + str(sudoku[0][1]) + str(sudoku[0][2]))
            break

        if not cached:
            sudoku_cache = copy.deepcopy(sudoku) # store in case the guess is wrong
            cached = True
            guesses = 0
        if not uncertain_check(sudoku): # we had to guess but there were no valid guesses, let's return to square one
            sudoku = copy.deepcopy(sudoku_cache)
            small_grid = blocks(sudoku)
            cached = False
        
print sum
print time.time() - t
