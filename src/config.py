import main
import pyautogui
import time
import ocr
class configFuncs:
    def manual() -> None:
        unsolvedInput = [[],[],[],[],[],[],[],[],[]]    
        Uinput = input(">")
        if "," in Uinput:    
            for x in range(0,9):
                for y in range(0,9):
                    unsolvedInput[x].append(int(Uinput.split(" ")[y+9*x].strip(",")))
        else:
            for x in range(0,9):
                for y in range(0,9):
                    unsolvedInput[x].append(int([*Uinput][y+9*x]))
        return unsolvedInput
    def startmovement(unsolvedInput) -> None:
        for x in range(0,9):
            pyautogui.click(ocr.ssPos[x][0][0]+20, ocr.ssPos[x][0][1]+20)
            for y in range(0,9):
                pyautogui.press(str(main.unsolvedInput[x][y]))
                pyautogui.press('right')    
                time.sleep(0.4)
        return None