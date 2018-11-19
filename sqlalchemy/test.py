import time

calNum = 100000000
listSize = 100000
d = [0.0 for _ in range(listSize)]


def test():
    global d
    for x in range(calNum):
        d[x % listSize] = x+0.1
    return d


start = time.time()

test()

end = time.time()

print(end - start)
