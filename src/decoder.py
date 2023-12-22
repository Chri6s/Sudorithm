import time
from paddleocr import PaddleOCR
import pyautogui
import main
import ocr
def startmovement():
    for x in range(0,9):
        pyautogui.click(ocr.ssPos[x][0][0]+20, ocr.ssPos[x][0][1]+20)
        for y in range(0,9):
            pyautogui.press(str(main.unsolved[x][y]))
            pyautogui.press('right')    
            time.sleep(0.4)
    return