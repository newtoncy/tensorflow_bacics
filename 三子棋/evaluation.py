def connect_len(chess_board, i, j):
    """
    相连的长度
    :param chess_board:
    :param i:
    :param j:
    :return: 连成一条线的棋子长度
    """
    forward = [[1, 0], [0, 1], [1, 1], [1, -1]]
    result = []
    for f in range(4):
        l = 0
        r = 0
        a, b = i, j
        while i + forward[f][1] < 3 and j + forward[f][2] < 3 \
                and chess_board[i][j] == chess_board[i + forward[f][1]][j + forward[f][2]]:
            l += 1
            a += forward[f][1]
            b += forward[f][2]

        a, b = i, j
        while i - forward[f][1] > 0 and j - forward[f][2] > 0 \
                and chess_board[i][j] == chess_board[i - forward[f][1]][j - forward[f][2]]:
            r += 1
            a -= forward[f][1]
            b -= forward[f][2]
        result.append(l + r + 1)
    return max(result)


def evaluation(chess_board):
    """

    :param chess_board: 一个表示棋盘的列表
    :return: 一个元组(评价值,是否有进一步拓展的必要)
    """
    # 如果相连有三个,那返回正负无穷,不需要再继续了
    for i in range(3):
        for j in range(3):
            if connect_len(chess_board, i, j) == 3:
                return chess_board[i][j] * float('inf'), False
    # 如果棋盘还有空位,返回0,继续
    for i in range(3):
        for j in range(3):
            if chess_board[i][j] == 0:
                return 0, True
    # 否则返回0,退出
    return 0, False
