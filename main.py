from solver import *
import mouse
def start():
    startgrab()
    startSolve()
    startmovement()
class colors:
    reset = "\033[0m"
    class fg: 
        prefilled = "\033[31m"
        generated = "\033[32m"




if __name__ == "__main__":
    try:
        start()
    finally:
        print("Exception thrown.")
