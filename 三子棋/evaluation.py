# (i,j)棋子和同色棋子相连的最大长度
def connect_len(chess_board, i, j):
    """
    相连的长度
    :param chess_board:
    :param i:
    :param j:
    :return: 连成一条线的棋子长度
    """
    if chess_board[i][j] == 0:
        return 0
    forward = [[1, 0], [0, 1], [1, 1], [1, -1]]
    result = []
    for f in range(4):
        l = 0
        r = 0
        a, b = i, j
        while 0 <= a + forward[f][0] < 3 and 0 <= b + forward[f][1] < 3 \
                and chess_board[a][b] == chess_board[a + forward[f][0]][b + forward[f][1]]:
            l += 1
            a += forward[f][0]
            b += forward[f][1]

        a, b = i, j
        while 3 > a - forward[f][0] >= 0 and 3 > b - forward[f][1] >= 0 \
                and chess_board[a][b] == chess_board[a - forward[f][0]][b - forward[f][1]]:
            r += 1
            a -= forward[f][0]
            b -= forward[f][1]

        result.append(l + r + 1)
    return max(result)


# 残局评价函数,因为只有九个格子,所以评估函数只在胜利的情况返回正无穷,输掉的时候返回负无穷
# 其他时候返回0
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

# a = [
#     [1, 0, 1],
#     [1, 1, 0],
#     [0, 0, 1]
# ]
# connect_len(a, 1, 1)
# pass
