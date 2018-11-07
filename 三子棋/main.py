from print_chess import *
import game_tree

chess_board = [[0] * 3] * 3

while True:
    turn = -1
    if turn == -1:
        command = input(">")
        command = command.split()
        place = 0
        if len(command) == 0:
            continue
        if command[0] == 'p' and len(command) == 2:
            try:
                place = int(command[1])
            except:
                print("Error")
                continue
            if 9 >= place >= 1:
                place -= 1
                chess_board[place / 3][place % 3] = turn
                chess_board_print(chess_board)
            else:
                print("Error")
                continue
        if command[0] == 'c':
            turn = 1
            continue
    elif turn == 1:
        game_tree.game_tree(chess_board, 1, 0)
        i, j = game_tree.path[0]
        chess_board[i][j] = turn
        chess_board_print(chess_board)
