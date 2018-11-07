# 打印棋盘的函数
def chess_board_print(chess_board):
    i = 0
    print("-" * (6 * 3))
    for line in chess_board:
        str_line = "|"
        for item in line:
            if item == 0:
                p = " "
            elif item == 1:
                p = "X"
            elif item == -1:
                p = "●"
            str_line += "%d: %c |" % (i, p)
            i += 1
        print(str_line)
        print("-" * (6 * 3))


# chess_board_print([
#     [1, 0, -1],
#     [0, 0, 1],
#     [1, -1, 1]
# ])
