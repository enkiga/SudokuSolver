# Solve the board
def solve(bo):
    # find an empty square
    find = find_empty(bo)
    # if no empty squares are found, the board is solved
    if not find:
        return True
    else:
        # row, col
        row, col = find

    # iterate through the numbers 1-9
    for i in range(1, 10):
        # if the number is valid, add it to the board
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # recursively call solve() to solve the board
            if solve(bo):
                return True

            # if the board cannot be solved, backtrack and try again
            bo[row][col] = 0

    return False


# Validate the board
def valid(bo, num, pos):
    # Check Row
    for i in range(len(bo[0])):
        # if the number is already in the row, return False
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check Column
    for i in range(len(bo)):
        # if the number is already in the column, return False
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check Box
    # find the box that the number is in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # iterate through the box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            # if the number is already in the box, return False
            if bo[i][j] == num and (i, j) != pos:
                return False
    # if the number is not in the row, column, or box,
    return True


# find an empty square in the board
def find_empty(bo):
    # iterate through the board
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            # if the element is 0, return the position
            if bo[i][j] == 0:
                # row, col
                return i, j

                # if no empty squares are found, return None
    return None
