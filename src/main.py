import sys
import config
import ocr
import solver
M = 9
options = {
    "manualInput": False,
    "disableDecoder": False,
    "repeater": True
}
unsolved = [[],[],[],[],[],[],[],[],[]]
def start() -> None:
    # Check for flags
    for i in sys.argv:
        if (i.strip("-") == "m") or (i.strip("-") == "manualMode"):
            options["manualInput"] = 1
        if (i.strip("-") == "dD") or (i.strip("-") == "disableDecoder"):
            options["disableDecoder"] = 1
        if (i.strip("-") == "r") or (i.strip("-") == "repeater"):
            config["repeater"] = 1
    answer = input("Is the Bluestacks window in fullscreen? (Y/n)\n ==>")
    if answer.lower() == "n":
        return print("Please maximize the Bluestacks window!")
    
    if options["manualInput"] == 1:
        config.configFuncs.manual("")
    else:
        ocr.startOCR()
    if options["disableDecoder"] == 1:
        config.configFuncs.startMovement("")
    if options["repeater"] != False:
        start() 
    return None
        
        
def startSolve(inputGrid) -> None:
    grid = convert.toList("". open("grid.txt", "r"))
    if (solver.Suduko(inputGrid, 0, 0)):
        print("Solving...")
        solver.puzzle(grid, grid)
    else:
        print("Solution does not exist:(")
    return None
        
#
#       Classes
#
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