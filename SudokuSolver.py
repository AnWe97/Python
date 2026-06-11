sudoku_field = []

with open("Sudoku.txt", "r") as file:
    values = file.readlines()

index = -1

for row in values:

    sudoku_field.append([])
    row = row.strip()
    index += 1

    for number in row:

        sudoku_field[index].append(int(number))

def is_valid(row, col, number):
    temp_array = []

    row_bool = True
    col_bool = True
    block_bool = True

    if number != 0:
        return []

    # choose block
    if col <= 2:
        # first block
        col_start_original = 0
    elif 2 < col < 6:
        # second block
        col_start_original = 3
    else:
        # third block
        col_start_original = 6

    if row <= 2:
        # first block
        row_start_original = 0
    elif 2 < row < 6:
        # second block
        row_start_original = 3
    else:
        # third block
        row_start_original = 6

    #check start

    for i in range(1,10):

        #rowcheck
        if i in sudoku_field[row]:
            row_bool = False

        #colcheck
        for j in range(9):

            if i == sudoku_field[j][col]:
                col_bool = False
                break

        #blockcheck

        row_start = row_start_original

        for j in range(3):

            col_start = col_start_original

            for n in range(3):

                if sudoku_field[row_start][col_start] == i:
                    block_bool = False

                col_start += 1

            row_start += 1

        if row_bool and col_bool and block_bool:
            temp_array.append(i)

        row_bool = True
        col_bool = True
        block_bool = True

    return temp_array


def check_win():

    for i in range(9):

        for j in range(9):

            if sudoku_field[i][j] == 0:
                return False

    return True

#Genutztes Feld (Anpassbar)
#[5, 3, 0, 0, 7, 0, 0, 0, 0]
#[6, 0, 0, 1, 9, 5, 0, 0, 0]
#[0, 9, 8, 0, 0, 0, 0, 6, 0]
#[8, 0, 0, 0, 6, 0, 0, 0, 3]
#[4, 0, 0, 8, 0, 3, 0, 0, 1]
#[7, 0, 0, 0, 2, 0, 0, 0, 6]
#[0, 6, 0, 0, 0, 0, 2, 8, 0]
#[0, 0, 0, 4, 1, 9, 0, 0, 5]
#[0, 0, 0, 0, 8, 0, 0, 7, 9]

while True:

    for row_index in range(9):

        for col_index in range(9):
            temp_array = is_valid(row_index, col_index, sudoku_field[row_index][col_index])

            if len(temp_array) == 1:
                sudoku_field[row_index][col_index] = temp_array[0]

    solved = check_win()

    if solved:
        for row in sudoku_field:
            print(row)
        break