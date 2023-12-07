from solver import *
import mouse
def start():
    startgrab()
    startSolve()
    startmovement()
if __name__ == "__main__":
    try:
        start()
    finally:
        print("Exception thrown.")
