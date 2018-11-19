import numpy as np
import random

a = [[3, 4], [4, 3], [5, 6], [2, 8], [1, 1], [0.1, 0.1]]
b = [[-1, -1], [-2, -2], [-0.1, -0.1]]
a = [(np.array(item), 1) for item in a]
b = [(np.array(item), -1) for item in b]
c = a + b  # c为一个行向量x和正负y的元组的列表
w = np.zeros(2)
b = 0.


# 分类函数
def classify(w, x, b):
    return np.sign(w @ x.T + b)


# 用于随机选择一个没有被正确分类的点
def choose():
    global w, b, c
    random.shuffle(c)
    for item in c:
        x, y = item
        if classify(w, x, b) != y:
            return item
    return None


eta = 1
while True:
    item = choose()
    if item is None:
        break
    x, y = item
    w += eta * y * x
    b += eta * y

print(w)
print(b)
