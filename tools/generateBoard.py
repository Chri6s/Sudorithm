import random
M = 9 

Board = [[], [], [], [], [], [], [], [], []]
def genBoard():
    for x in range(0, 9):
        for y in range(0, 9):
            if random.randint(0, 100) <= 30:
                Board[x].append(0)
            else: 
                Board[x].append(random.randint(0,9))
    out = ""
    for x in range(0,9):
        for y in range(0,9):
            out += str(Board[x][y])
    return out