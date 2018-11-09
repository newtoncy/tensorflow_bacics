from print_chess import *
import game_tree
import copy
import evaluation

while True:  # 最外层循环是为了实现'重玩'这个指令
    chess_board = [[0] * 3 for _ in range(3)]  # 用来表示棋盘
    chess_board_print(chess_board)
    turn = -1  # 用来标记是哪方执棋
    path = []  # 用来存放预估路径
    while True:  # 循环执棋,下棋
        if turn == -1:
            command = input(">")
            command = command.split()
            place = 0
            # 若不输入任何指令,什么也不干

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

            if command[0] == 'show':
                if command[1] == 'branch' and len(command) == 2:
                    if len(path) < 2:
                        continue
                    tem_chess = copy.deepcopy(chess_board)
                    t = turn
                    chess_board_print(tem_chess)
                    for i, j in path[1:]:
                        tem_chess[i][j] = t
                        chess_board_print(tem_chess)
                        t = -t
                    continue
                if command[1] == 'board' and len(command) == 2:
                    chess_board_print(chess_board)
                    continue

            if command[0] == 'replay' and len(command) == 1:
                break

        elif turn == 1:
            _, _, path = game_tree.game_tree(chess_board, 1, 0)
            if len(path) > 0:
                i, j = path[0]
                chess_board[i][j] = turn
            chess_board_print(chess_board)
            if not evaluation.evaluation(chess_board)[1]:  # 当 go_on == false 时游戏结束
                print("游戏结束")
            turn = -1
