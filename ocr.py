import os
import time
from paddleocr import PaddleOCR
import pyautogui
os.environ['DISPLAY'] = ':0'
ocr = PaddleOCR(use_angle_cls=False, lang='en', show_log=False, max_text_length=1, use_gpu=False)
unsolved = [[],[],[],[],[],[],[],[],[]]
ssPos = [
    [[342, 187],[417, 187],[495,187],[575,187],[650,187],[729,187],[808,187],[885,187],[963,187]],
    [[342, 260],[417, 260],[495,260],[575,260],[650,260],[729,260],[808,260],[885,260],[963,260]],
    [[342, 339],[417, 339],[495,339],[575,339],[650,339],[729,339],[808,339],[885,339],[963,339]],
    [[342, 421],[417, 421],[495,421],[575,421],[650,421],[729,421],[808,421],[885,421],[963,421]],
    [[342, 495],[417, 495],[495,495],[575,495],[650,495],[729,495],[808,495],[885,495],[963,495]],
    [[342, 573],[417, 573],[495,573],[575,573],[650,573],[729,573],[808,573],[885,573],[963,573]],
    [[342, 654],[417, 654],[495,654],[575,654],[650,654],[729,654],[808,654],[885,654],[963,654]],
    [[342, 730],[417, 730],[495,730],[575,730],[650,730],[729,730],[808,730],[885,730],[963,730]],
    [[342, 808],[417, 808],[495,808],[575,808],[650,808],[729,808],[808,808],[885,808],[963,808]],
    ]
def startgrab():
    answer = input("Is the Bluestacks window in fullscreen? (Y/n)\n ==>")
    if answer.lower() == "n":
        return print("Please maximize the Bluestacks window!")    
    print("Starting ScreenGrab™")
    time.sleep(3)
    for x in range(9):
        for y in range(9):
            pyautogui.screenshot(f"./screenshots/sec{x}{y}.png",region=(ssPos[x][y][0],ssPos[x][y][1],73,71))
    print("S-Grab finished, initalizing OCR")
    for x in range(9):
        for y in range(9):
            readdata = ocr.ocr(f"./screenshots/sec{x}{y}.png", cls=False)
            #sample data from the OCR = [[[[[11.0, 6.0], [58.0, 6.0], [58.0, 68.0], [11.0, 68.0]], ('7', 0.9997418522834778)]]]
            if readdata == [[]]:
                unsolved[x].append(0)
            else:
                unsolved[x].append(int(readdata[0][0][1][0]))
def startmovement():
    for x in range(0,9):
        pyautogui.click(ssPos[x][0][0]+20, ssPos[x][0][1]+20)
        for y in range(0,9):
            pyautogui.press(str(unsolved[x][y]))
            pyautogui.press('right')    
            time.sleep(0.4)
    return