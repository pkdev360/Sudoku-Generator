import copy
import random as r
import sudoku_solver as solver


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


def rand_box():
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    rand_row = r.choice(seq)
    rand_col = r.choice(seq)
    return rand_row, rand_col


def filled_boxes(bo):
    count = []
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] != 0:
                count.append(1)
    total = len(count)
    return total


def generate_board(bo, max_num):
    if filled_boxes(bo) == max_num:
        return True
    while True:
        rand_pos = rand_box()
        row, col = rand_pos
        if bo[row][col] == 0:
            break
        else:
            continue

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rand_num = r.sample(numbers, 9)
    for num in range(len(rand_num)):
        if solver.valid(bo, rand_num[num], (row, col)):
            bo[row][col] = rand_num[num]

            if generate_board(bo, max_num):
                return True

            bo[row][col] = 0
    return False


while True:
    generate_board(board, 15)

    if solver.solve(board):
        break

solved_board = copy.deepcopy(board)


def generate_board_2(solved_bo, empty_boxes):
    length = 0
    while length < empty_boxes:
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        rand_num_1 = r.choice(numbers)
        rand_num_2 = r.choice(numbers)

        box_value = solved_bo[rand_num_1][rand_num_2]
        if box_value != 0:
            solved_bo[rand_num_1][rand_num_2] = 0
            length += 1
        else:
            continue


def main():
    generate_board_2(board, 30)

    solver.display_board(solved_board)

    print('\n*********************\n')

    solver.display_board(board)

    print('\n*********************\n')

    solver.display_board_list(board)


if __name__ == "__main__":
    main()
