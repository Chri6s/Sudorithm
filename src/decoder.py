import time
from paddleocr import PaddleOCR
import pyautogui
from main import savedUnsolved
from ocr import unsolved, ssPos
def startmovement():
    for x in range(0,9):
        pyautogui.click(ssPos[x][0][0]+20, ssPos[x][0][1]+20)
        for y in range(0,9):
            pyautogui.press(str(unsolved[x][y]))
            pyautogui.press('right')    
            time.sleep(0.4)
    return