import random

def getRand(): 
    return random.randrange(1,5)


def printTable(name: str, a,b,c,d):
    print("_________")
    for row in range(1,5):
        line = "|"

        if a == row:
            line+="#|"
        else:
            line+=" |"
        if b == row:
            line+="#|"
        else:
            line+=" |"
        if c == row:
            line+="#|"
        else:
            line+=" |"
        if d == row:
            line+="#|"
        else:
            line+=" |"
        if (row == 1):
            line += " " + name
        print(line)
    print(chr(8254) + chr(8254) + chr(8254) + chr(8254) + chr(8254) + chr(8254) + chr(8254) + chr(8254) + chr(8254))

printTable("Table 1", 1,3,2,4)
printTable("Table 2", 1,1,1,1)
printTable("Table 3", 1,2,3,4)
printTable("Table 4", 1,1,2,4)

for round in range(1,5):
    for i in range(1,5):
        print(f"Round {round}: Table {i} Queen {getRand()} is selected to move")
    print()

