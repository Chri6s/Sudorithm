import sys
import config
import ocr
import solver
M = 9
options = {
    "manualInput": 0,
    "disableDecoder": 0,
    "repeater": 0
}
def start():
    # Check for flags
    for i in sys.argv:
        if (i.strip("-") == "m") or (i.strip("-") == "manualMode"):
            options["manualInput"] = 1
        if (i.strip("-") == "dD") or (i.strip("-") == "disableDecoder"):
            options["disableDecoder"] = 1
        if (i.strip("-") == "r") or (i.strip("-") == "repeater"):
            config["repeater"] = 1
    if options["manualInput"] == 1:
        config.configFuncs.manual("")
    else:
        ocr.startgrab()
    startSolve
    if options["disableDecoder"] == 1:
        config.configFuncs.startMovement("")
        
        
def startSolve(inputGrid):
    grid = convert.toList("". open("grid.txt", "r"))
    if (solver.Suduko(inputGrid, 0, 0)):
        print("Solving...")
        solver.puzzle(grid, grid)
    else:
        print("Solution does not exist:(")
        
        
def puzzle(unsolvedGrid, solvedGrid):
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
        if (i == 2) or (i == 5):
            print()
        print()
    print(colors.reset)
        
class colors:
    reset = "\033[0m"
    class fg: 
        prefilled = "\033[31m"
        generated = "\033[32m"
    class bg:
        black = "\033[40m"

class convert:
    def toList(self, string) -> list:
        listified = [[],[],[],[],[],[],[],[],[]]
        if "," in string:    
            for x in range(0,9):
                for y in range(0,9):
                    listified[x].append(int(string.split(" ")[y+9*x].strip(",")))
        else:
            for x in range(0,9):
                for y in range(0,9):
                    listified[x].append(int([*string][y+9*x]))
        return listified

    def toString(self, list) -> str:
        stringified = ""
        for x in range(0,9):
            for y in range(0,9):
                stringified += str(list[x][y])
        return stringified
    
    
if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        pass
    finally:
        print("Exception thrown.")