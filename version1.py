import numpy

initState =   [
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

def printPuzzle(state):
    for row in state:
        print(row)

def checkBox(state, i , j):
    x = (i//3)*3
    y = (j//3)*3
    for u in range(x,x+3):
        for v in range(y,y+3):
            if state[u][v] == state[i][j] and not (u == i and v == j):
                return False
            
    for u in range(9):
        if state[u][j] == state[i][j] and u != i:
            return False
        
        if state[i][u] == state[i][j] and u != j:
            return False
    #printPuzzle(state)
    #print('-------------------')
    return solve(state)

def solve(state):
    x = -1
    y = -1
    f = True
    for r in range(0,9):
        if f:
            for c in range(0,9):
                if state[r][c] == 0:
                    x = r
                    y = c
                    f = False 
                    break
    if f:
        printPuzzle(state)
        return True
    for num in range(1,10):
        newState = numpy.copy(state)
        newState[x][y] = num
        if checkBox(newState, x, y):
            return True      
     
solve(initState)