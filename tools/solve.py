M = 9
grid = None
unsolvedGrid = None
class colors:
    reset = "\033[0m"
    class fg: 
        prefilled = "\033[31m"
        generated = "\033[32m"
    class bg:
        black = "\033[40m"
def start():
    grid = [[],[],[],[],[],[],[],[],[]]
    unsolvedGrid = [[],[],[],[],[],[],[],[],[]]
    bemenet = input(">")
    if "," in bemenet:    
        for x in range(0,9):
            for y in range(0,9):
                grid[x].append(int(bemenet.split(" ")[y+9*x].strip(",")))
                unsolvedGrid[x].append(int(bemenet.split(" ")[y+9*x].strip(",")))
    else:
        for x in range(0,9):
            for y in range(0,9):
                grid[x].append(int([*bemenet][y+9*x]))
                unsolvedGrid[x].append(int([*bemenet][y+9*x]))
    
    if (Suduko(grid, 0, 0)):
        print("Solving...")
        puzzle(grid, unsolvedGrid)

    else:
        print("Solution does not exist:(")
def puzzle(solvedGrid, unsolvedGrid):
    for i in range(M):
        for j in range(M):
            if j == 2 or j == 5:
                if unsolvedGrid[i][j] == 0:
                    print(colors.fg.generated + str(solvedGrid[i][j]) + colors.reset,end = "   ")
                else:
                    print(colors.fg.prefilled + str(solvedGrid[i][j]) + colors.reset,end = "   ")
            else:
                if unsolvedGrid[i][j] == 0:
                    print(colors.fg.generated + str(solvedGrid[i][j]),end = " " + colors.reset)
                else:
                    print(colors.fg.prefilled + str(solvedGrid[i][j]),end = " " + colors.reset)
        if i == 2 or i == 5:
            print()
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
if __name__ == "__main__":
    try:
        while True:
            start()
    except KeyboardInterrupt:
        pass