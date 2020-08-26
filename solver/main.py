"""
#A simple Sudoku solver.
#By Parth Pruthi.
"""

def print_puzzle(puzzle):
    print('__________________')
    for i in puzzle:
        for j in i:
            print('%d' %(j), end=" ")
        print('')
    print('__________________')

def find_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return (i, j)
    return (-1,-1)


def is_empty(puzzle: list) -> bool:
    count = 0
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                return False
    return True

#the function checks wether puzzle[i][j] is unique in the row.
#returns true if it is unique else false.
def is_unique_row(puzzle: list, i: int, j: int, val: int) -> bool:
    for index in range(9):
        if puzzle[i][index] == val and index != j:
            return False
    return True

#checks wether puzzle[i][j] is unique in its respective box[3X3].
def is_unique_box(puzzle: list, i: int, j: int, val:int) -> bool:
    secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
    for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if puzzle[x][y] == val:
                    return False
    return True

#checks wether puzzle[i][j] is unique in it's respective column.
def is_unique_col(puzzle: list, i: int, j: int, val: int) -> bool:
    for index in range(9):
        if puzzle[index][j] == val and index != i:
            return False
    return True



#checks wether given puzzle is valid by checking uniqueness of puzzle[i][j]
def is_valid(puzzle: list, i: int, j: int, val: int) -> bool:
    if val == 0:
        return False
    r = is_unique_row(puzzle, i, j, val)
    if r is False:
        return False
    c = is_unique_col(puzzle, i, j, val)
    if c is False:
        return False
    b = is_unique_box(puzzle, i, j, val)
    if b is False:
        return False
    return True


def solver(puzzle):
    (c1, c2) = find_empty(puzzle)
    if c1 == -1:
        return True
    for val in range(1,10):
        valid = is_valid(puzzle, c1, c2, val)
        if valid:
            puzzle[c1][c2] = val
            if solver(puzzle):
                return True
        puzzle[c1][c2] = 0
    return False







