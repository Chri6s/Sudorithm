from solver import *
import mouse
def start():
    startgrab()
    startSolve()
if __name__ == "__main__":
    try:
        start()
    expect:
        print("Exception thrown.")