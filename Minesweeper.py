import random

validLetters = ["A", "B", "C", "D", "E", "F", "G"]
validNumbers = [1, 2, 3, 4, 5]

minefield = [
    [".", "1", "2", "3", "4", "5"],
    ["A", False, False, False, False, False],
    ["B", False, False, False, False, False],
    ["C", False, False, False, False, False],
    ["D", False, False, False, False, False],
    ["E", False, False, False, False, False],
    ["F", False, False, False, False, False],
    ["G", False, False, False, False, False]
]

field = [
    ["-", "1", "2", "3", "4", "5"],
    ["A", ".", ".", ".", ".", "."],
    ["B", ".", ".", ".", ".", "."],
    ["C", ".", ".", ".", ".", "."],
    ["D", ".", ".", ".", ".", "."],
    ["E", ".", ".", ".", ".", "."],
    ["F", ".", ".", ".", ".", "."],
    ["G", ".", ".", ".", ".", "."]
]

def checkMines(index, col):
    counter = 0
    startIndex = index - 1
    startCol = col - 1

    for i in range(3):
        for j in range(3):
            r = startIndex + i
            c = startCol + j

            #check boundaries
            if 1 <= r < len(minefield) and 1 <= c < len(minefield[0]):
                if minefield[r][c]:
                    counter += 1

    return counter

def checkField(row, col):

    row = row.upper()
    col = int(col)
    index = (validLetters.index(row) + 1)

    chosenField = field[index][col]
    chosenMinefield = minefield[index][col]

    if chosenField != ".":
        print("Field already checked.")
        return

    if chosenMinefield:
        #Minehit
        print("Too bad you hit a mine.")
        return True

    else:

        amountOfMines = checkMines(index, col)

        field[index][col] = str(amountOfMines)

def showField():

    for row in field:
        print(row)

def layMines(amount):
    counter = 0

    while counter < amount:
        column = random.randint(1, 5)
        row = random.randint(1,7)

        if not minefield[row][column]:
            minefield[row][column] = True
            counter+=1

def countFields():
    counter = 0

    for i in range(len(field)):
        for j in range(len(field[i])):

            counter += 1

    return counter

def checkWin():
    global mineAmount
    counter = 0

    for i in range(len(field)):
        for j in range(len(field[i])):

            if field[i][j] == ".":
                counter+=1

    if counter == mineAmount:
        win = True
        print("You got all mines.")
        print("You win, congratulations!")

        return win

start = True
mineAmount = 0

while True:
    showField()
    won = checkWin()

    if won:
        break

    if start:

        fields = countFields()
        mineAmount = input("How many mines do you want to search: ")

        if not mineAmount.isdigit():
            print("Choose a number.")
            continue

        mineAmount = int(mineAmount)

        if mineAmount < (fields//3):
            layMines(mineAmount)
            start = False
            print("Game start")
        else:
            print("Too many mines for the field. Take fewer.")

    else:
        #Game start after laying mines


        chosenRow = input("What row do you want to check (A, B, C, D, E, F, G): ")

        if chosenRow.isalpha() and chosenRow.upper() in validLetters:
            #Row check

            chosenCol = input("What column do you want to check (1, 2, 3, 4, 5): ")

            if not chosenCol.isdigit() or int(chosenCol) not in validNumbers:
                print("Choose a valid number.")
                continue

            else:
                #Column check

                endGame = checkField(chosenRow, chosenCol)

                if endGame:
                    print("Game over.")
                    break

        else:
            print("Choose a valid letter.")
            continue