import evaluation


# 博弈树,核心代码
def game_tree(chess_board, turn, layer):
    """

    :param chess_board: 表示一个棋盘的列表
    :param turn: 谁的回合,对手的填-1,我们的填1
    :param layer: 层数,初始填0
    :return: 返回一个元组,(博弈树末梢的评估值,此评估值是在那一层产生的,此评估值产生的路径)
    """
    # 局部变量的解释
    # root_eva 当前层的评估值
    # go_on 是否继续
    # branch_back 每个分支的返回值列表
    # branch_eva 每个分支的评估值
    # branch_eva_layer 这个评估值在哪一层产生

    # 获得此时的评估值
    (root_eva, go_on) = evaluation.evaluation(chess_board)
    # 这个数组用来放返回值
    branch_back = []
    if go_on is False:
        return root_eva, layer, [None for _ in range(layer)]
    for i in range(3):
        for j in range(3):
            if chess_board[i][j] == 0:
                chess_board[i][j] = turn
                branch_eva, branch_eva_layer, branch_path = game_tree(chess_board, -turn, layer + 1)
                chess_board[i][j] = 0
                branch_back.append({
                    'branch': (i, j),
                    'value': branch_eva,
                    'path': branch_path,
                    'layer': branch_eva_layer})
    # 如果是自己的回合,选取最大值返回,如果是对方的回合选取最小值返回
    value_list = [item['value'] for item in branch_back]
    if turn == 1:
        index = value_list.index(max(value_list))
    elif turn == -1:
        index = value_list.index(min(value_list))
    branch_back = branch_back[index]
    path = branch_back['path']
    path[layer] = branch_back['branch']
    return branch_back['value'], branch_back['layer'], path
