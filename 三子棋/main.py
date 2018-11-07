from print_chess import *
import game_tree
import copy

chess_board = [[0] * 3 for _ in range(3)]
chess_board_print(chess_board)
turn = -1
while True:
    if turn == -1:
        command = input(">")
        command = command.split()
        place = 0
        if len(command) == 0:
            continue
        # 使用p命令来放置棋子
        if command[0] == 'p' and len(command) == 2:
            try:
                place = int(command[1])
            except:
                print("Error")
                continue
            if 8 >= place >= 0:
                chess_board[int(place / 3)][place % 3] = turn
                chess_board_print(chess_board)
                turn = 1
                continue
            else:
                print("Error")
                continue
    elif turn == 1:
        game_tree.game_tree(chess_board, 1, 0)
        i, j = game_tree.path[0]
        chess_board[i][j] = turn
        chess_board_print(chess_board)
        turn = -1
