import sys
# sample data
# 
config = {
    "manualInput": 0,
    "disableDecoder": 0,
    "disableOCR": 0,
    "repeater": 0
}
def start():
    file = open("grid.txt", "w")
    unsolved = [[],[],[],[],[],[],[],[],[]]
    # Check for flags
    for i in sys.argv:
        if (i.strip("-") == "m") or (i.strip("-") == "manualMode"):
            config["manualInput"] = 1
        if (i.strip("-") == "dD") or (i.strip("-") == "disableDecoder"):
            config["disableDecoder"] = 1
        if (i.strip("-") == "dO") or (i.strip("-") == "disableOCR"):
            config["disableOCR"] = 1
        if (i.strip("-") == "r") or (i.strip("-") == "repeater"):
            config["repeater"] = 1
    if config["manualInput"] == 1 and config["disableOCR"] == 1:
        Uinput = input(">")
        if "," in Uinput:    
            for x in range(0,9):
                for y in range(0,9):
                    unsolved[x].append(int(Uinput.split(" ")[y+9*x].strip(",")))
        else:
            for x in range(0,9):
                for y in range(0,9):
                    unsolved[x].append(int([*Uinput][y+9*x]))
        file.write(convert.toString("", unsolved))
        file.close()
        startSolve(unsolved)
    #startgrab()
    #startmovement()
    # if config["repeater"] == 1:
    #     start()
    # else: 
    #     return
# def startSolve(inputGrid):
#     grid = convert.toList("". open("grid.txt", "r"))
#     if (solver.Suduko(inputGrid, 0, 0)):
#         print("Solving...")
#         solver.puzzle(grid, grid)
#     else:
#         print("Solution does not exist:(")

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