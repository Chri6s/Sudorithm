from solver import *
#import mouse
import argparse
#import pyautogui
#from paddleocr import PaddleOCR
# sample data
# 0, 6, 0, 8, 5, 0, 0, 0, 7, 7, 0, 5, 2, 0, 3, 8, 0, 0, 0, 0, 2, 0, 9, 0, 5, 0, 0, 0, 4, 0, 9, 0, 8, 2, 7, 3, 0, 0, 7, 5, 0, 6, 4, 0, 8, 0, 9, 0, 0, 4, 0, 1, 0, 6, 0, 7, 3, 0, 8, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 8, 0, 1, 0, 0, 0, 0, 3, 4, 0

unsolved = [[],[],[],[],[],[],[],[],[]]



parser = argparse.ArgumentParser()
config = {
    "useDecoder": True,
    "verbose": False
}
def start():
    print("----MANUAL INPUT MODE----")
    #startgrab()
    bemenet = input(">")
    for x in range(0,9):
        for y in range(0,9):
            unsolved[x].append(int(bemenet.split(" ")[y+9*x].strip(",")))
    startSolve()
    #startmovement()
class colors:
    reset = "\033[0m"
    class fg: 
        prefilled = "\033[31m"
        generated = "\033[32m"




parser.add_argument("-dd", "--disable-decoder", action="store")
if __name__ == "__main__":
    try:
        start()
    finally:
        print("Exception thrown.")
