#from ocr import *
from main import unsolved, colors
M = 9
savedUnsolved = unsolved
grid = unsolved
def puzzle(unsolvedGrid, solvedGrid):
    for i in range(M):
        for j in range(M):
            if unsolvedGrid[i][j] == 0:
                print(colors.fg.generated + solvedGrid, end=" ")
            else:
                print(colors.fg.prefilled + solvedGrid, end=" ")
        print()
    print(colors.reset)


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


def startSolve():
    if (Suduko(grid, 0, 0)):
        print("Solving...")
        puzzle(savedUnsolved, grid)

    else:
        print("Solution does not exist:(")
