def is_X_winner(matrix_):
    for i in range(3):
        if matrix_[i] == ["X", "X", "X"] or [row[i] for row in matrix_] == ["X", "X", "X"]:
            return True
    if [matrix_[i][i] for i in range(3)] == ["X", "X", "X"]:
        return True
    if [matrix_[2 - i][i] for i in range(3)] == ["X", "X", "X"]:
        return True
    return False


def is_O_winner(matrix_):
    for i in range(3):
        if matrix_[i] == ["O", "O", "O"] or [row[i] for row in matrix_] == ["O", "O", "O"]:
            return True
    if [matrix_[i][i] for i in range(3)] == ["O", "O", "O"]:
        return True
    if [matrix_[2 - i][i] for i in range(3)] == ["O", "O", "O"]:
        return True
    return False


def display(matrix_):
    print("-" * 9)
    print("|", *matrix_[0], "|")
    print("|", *matrix_[1], "|")
    print("|", *matrix_[2], "|")
    print("-" * 9)



matrix = list([" ", " ", " "] for i in range(3))
players = [" ", "X", "O"]
shift = 1
display(matrix)
while True:
    try:
        x, y = map(int, input("Enter the coordinates: ").split())
    except:
        print("You should enter numbers!")
        continue
    if x > 3 or y > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    elif matrix[3 - y][x - 1] != " ":
        print("This cell is occupied! Choose another one!")
        continue
    else:
        matrix[3 - y][x - 1] = players[shift]
        shift *= -1
    if is_X_winner(matrix):
        display(matrix)
        print("X wins")
        break
    if is_O_winner(matrix):
        display(matrix)
        print("O wins")
        break
    if all(" " not in rows for rows in matrix):
        display(matrix)
        print("Draw")
        break
    display(matrix)