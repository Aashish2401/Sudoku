import numpy as np

board = [[5,3,0,0,7,0,0,0,0],                                           #Declaration of the incomplete sudoku grid. May be edited for other 
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,0,8,0],
         [0,0,0,4,1,9,0,0,0],
         [0,0,0,0,8,0,0,0,0]]

count = 1                                                               #This variable is used to keep track of the number of solution, in case of multiple solutions

print("Original Grid:")
print()
print(np.matrix(board))

def possible(n,x,y) :                                                   #Method used to check whether a particular number 'n' between 1 to 9 can be inserted into the index (y,x) of the board
    global board
    
    for i in range(9) :        
        if board[y][i] == n : #Check the row
            return False
        if board[i][x] == n : #Check the column
            return False

    x = x // 3
    y = y // 3

    for i in range(y * 3,y * 3 + 3) : #Check the 3x3 grid
        for j in range(x * 3,x * 3 + 3) :
            if board[i][j] == n :
                return False

    return True

def solve() :                                                           #Method to perform the backtracking search to find the solution
    global board
    global count
    
    for i in range(9) :
        for j in range(9) :
            if board[i][j] == 0 :
                for num in range(1,10) :
                    if possible(num,j,i) :
                        board[i][j] = num
                        solve() #Recursive call
                        board[i][j] = 0

                return
            
    print()
    print("Solution {0}:".format(count))
    print()
    count += 1
    print(np.matrix(board))

solve() #Initial call
input()
