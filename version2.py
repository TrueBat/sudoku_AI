#  In this method for solving the sudoku puzzle, first, we assign the size of the 2D matrix to a 
# variable M (MM).
import numpy as py;
rows=9
cols=9

matrix = [
    [2,9,0,0,7,1,0,0,0],
    [0,8,0,3,0,9,0,0,6],
    [0,4,0,0,0,0,0,0,0],
    [9,0,7,0,8,0,2,0,4],
    [0,0,0,9,0,0,6,0,0],
    [0,0,8,0,2,0,9,1,3],
    [0,2,9,7,0,4,0,3,8],
    [8,0,5,1,0,0,0,7,9],
    [0,7,4,0,9,0,1,6,2]
]

# • If we find the same num in the same row or same column or in the specific 33 matrix, ‘false’ 
# will be returned.
def check_box(state, row, col, num):
    loc_box_row = (row // 3) * 3
    loc_box_col = (col // 3) * 3
    for i in range(loc_box_row, loc_box_row + 3):
        for j in range(loc_box_col, loc_box_col + 3):
            if state[i][j] == num and not(i == row and j == col ):
                return False

    for u in range(9):
        if state[u][col] == num and u != row:
            return False

        if state[row][u] == num and u != col:
            return False
    print_matrix(state)
    print("----")
    return True

# • Then we assign the utility function (puzzle) to print the grid.
def print_matrix(matrix):
    for i in range(0,9):
        print(matrix[i])

def solve_puzzle(state):
    f = True
    for r in range(9):
        for c in range(9):
            if state[r][c] == 0:
                row = r
                col = c
                f = False
                break
    if not f:
        print_matrix(state)
    for n in range(1,10):
        new_state=py.copy(state)
        new_state[row][col]=n
        if check_box(new_state,row,col,n):
            solve_puzzle(new_state)

    return 

solve_puzzle(matrix)