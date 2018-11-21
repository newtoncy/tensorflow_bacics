class KdBox:
    kd_range = []  # 第k个数组元素是表示第k个轴上最大和最小取值的元组
    _k = 0

    def split(self, axis, value):
        a = b = self.kd_range
        a[axis] = a[axis][0], value
        b[axis] = value, b[axis][1]
        return KdBox(a), KdBox(b)

    # 点在超立方体区域内,讲道理这个函数不会被用到
    def is_inner(self, point):
        for i in range(self._k):
            value = point[i]
            min, max = self.kd_range[i]
            if not min <= value < max:
                return False
        return True

    # 讲道理,这个函数应该用来判断超立方体和超球体有没有交集,但是我写不来..
    # 所以把球体用外接立方体代替,或许这样反而快,毕竟计算量小
    def is_cross(self, point, r):
        for i in range(self._k):
            # 判断在第i个轴向上是不是有交集
            axis_min = max(point[i] - r, self.kd_range[i][0])
            axis_max = min(point[i] + r, self.kd_range[i][1])
            if axis_min > axis_max:
                return False
        return True

    def __init__(self, kd_range=None):
        self.kd_range = kd_range
        if kd_range is not None:
            self._k = len(kd_range)


class KdNode:
    point = None
    left = None
    right = None
    parent = None



class KdTree:
    _root = None

    def __init__(self, point_list=None):
        if point_list is not None:
            self.create(point_list)

    def create(self, point_list, i=0, parent=None):
        if len(point_list) == 0:
            return None
        i %= len(point_list[0])
        point_list = point_list.sort(key=lambda l: l[i])
        mid = int(len(point_list)/2)
        it = KdNode()
        it.point = point_list[mid]
        it.parent = parent
        if parent is None:
            self._root = it
        it.left = self.create(point_list[0:mid], i=i + 1, parent=it)
        it.right = self.create(point_list[mid:], i=i + 1, parent=it)
        return it

    def find_k(self, point, k):
        pass
