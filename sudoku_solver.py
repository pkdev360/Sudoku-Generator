
board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def display_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')


def display_board_list(bo):
    print('board = [')
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if j == 0:
                print('\t[' + str(bo[i][j]) + ', ', end='')
            elif j == 8 and i != 8:
                print(str(bo[i][j]) + '],')
            elif i == 8 and j == 8:
                print(str(bo[i][j]) + ']')
            else:
                print(str(bo[i][j]) + ', ', end='')
    print(']')


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return False


def valid(bo, num, pos):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[pos[0]][j] == num and pos[1] != j:
                return False

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num

            if solve(bo):
                return True
            else:
                bo[row][col] = 0
    return False


def main():
    display_board(board)
    print('\n*********************\n')

    solve(board)

    display_board(board)


if __name__ == "__main__":
    main()
