# 完全失败的想法，被百度百科坑了
import numpy as np

a = np.array([[2., 2.], [1., 0.], [3., 0.]])
b = np.array([2., 1.])


def stack_one(a):
    a = a.T
    ones = np.ones([1, a.shape[1]])
    a = np.vstack((a, ones))
    return a


def point_in_conv(conv, point):
    A = stack_one(conv)
    B = stack_one(point.reshape(1, point.shape[0]))
    C = np.hstack((A, B))
    rankA = np.linalg.matrix_rank(A)
    rankC = np.linalg.matrix_rank(C)
    if rankC == rankA:
        return True
    return False


point_in_conv(a, b)
print(point_in_conv(a, np.array([2.5, 1])))
print(point_in_conv(a, np.array([3, 1])))
