from solver import *
import sys
# sample data
# 0, 6, 0, 8, 5, 0, 0, 0, 7, 7, 0, 5, 2, 0, 3, 8, 0, 0, 0, 0, 2, 0, 9, 0, 5, 0, 0, 0, 4, 0, 9, 0, 8, 2, 7, 3, 0, 0, 7, 5, 0, 6, 4, 0, 8, 0, 9, 0, 0, 4, 0, 1, 0, 6, 0, 7, 3, 0, 8, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 8, 0, 1, 0, 0, 0, 0, 3, 4, 0
unsolved = [[],[],[],[],[],[],[],[],[]]
savedUnsolved = [[],[],[],[],[],[],[],[],[]]
config = {
    "manualInput": 0,
    "disableDecoder": 0,
    "useOCR": 1,
    "repeater": 0
}
def start():
    # Check for flags
    for i in sys.argv:
        if (i.strip("-") == "m") or (i.strip("-") == "manualMode"):
            config["manualInput"] = 1
        if (i.strip("-") == "dD") or (i.strip("-") == "disableDecoder"):
            config["disableDecoder"] = 0
        if (i.strip("-") == "dO") or (i.strip("-") == "disableOCR"):
            config["useOCR"] = 0
    if config["manual"] == 1 and config["disableOCR"] == 1:
        Uinput = input(">")
        if "," in Uinput:    
            for x in range(0,9):
                for y in range(0,9):
                    unsolved[x].append(int(Uinput.split(" ")[y+9*x].strip(",")))
                    savedUnsolved[x].append(int(Uinput.split(" ")[y+9*x].strip(",")))
        else:
            for x in range(0,9):
                for y in range(0,9):
                    unsolved[x].append(int([*Uinput][y+9*x]))
                    savedUnsolved[x].append(int([*Uinput][y+9*x]))
        startSolve()
    #startgrab()
    #startmovement()
    if config["repeater"] == 1:
        start()
class colors:
    reset = "\033[0m"
    class fg: 
        prefilled = "\033[31m"
        generated = "\033[32m"
    class bg:
        black = "\033[40m"
if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        pass
    finally:
        print("Exception thrown.")
