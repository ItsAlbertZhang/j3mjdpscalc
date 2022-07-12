# coding:utf-8


class 简单属性():
    '''
    简单属性, 包括 '基础', '额外', '额外1024分比' 三个字段.
    '''

    def __init__(self, 基础=0) -> None:
        self.基础 = 基础
        self.额外 = 0
        self.额外1024分比 = 0

    # 抽象出一个属性, 以便于在属性变动时执行操作
    @property
    def 基础(self):
        return self._基础

    @基础.setter
    def 基础(self, value):
        self._基础 = value
        self.计算最终属性()

    # 重复两次上述操作, 再次抽象出两个属性
    @property
    def 额外(self):
        return self._额外

    @额外.setter
    def 额外(self, value):
        self._额外 = value
        self.计算最终属性()

    @property
    def 额外1024分比(self):
        return self._额外1024分比

    @额外1024分比.setter
    def 额外1024分比(self, value):
        self._额外1024分比 = value
        self.计算最终属性()

    # 定义方法
    def 计算最终属性(self):
        try:
            self.最终 = int((self.基础 + self.额外) * (1 + self.额外1024分比 / 1024))
        except:
            self.最终 = self.基础

    def 输出dict结果(self):
        attr = ['基础', '额外', '额外1024分比', '最终']
        ret = {}
        for elem in attr:
            ret[elem] = getattr(self, elem)
        return ret

    def __str__(self) -> str:
        return str(self.输出dict结果())


class 复杂属性_外阳阴混毒():
    '''
    有外功, 阳性内功, 阴性内功, 混元内功和毒性内功之区分的属性.

    其包括上述五个字段, 每个字段均为一个简单属性.
    '''

    def __init__(self, arg={}) -> None:
        self.attr = ['外功', '阳性内功', '阴性内功', '混元内功', '毒性内功']
        for elem in self.attr:
            setattr(self, elem, 简单属性())
        # 如果传入了参数, 那么按照参数进行属性设置
        for key in arg:
            if key in self.attr:
                setattr(self, key, 简单属性(arg[key]))

    def 输出dict结果(self):
        ret = {}
        for elem in self.attr:
            ret[elem] = getattr(self, elem).输出dict结果()
        return ret

    def __str__(self) -> str:
        return str(self.输出dict结果())


def test_func() -> dict:
    # 会心 = 属性(50)
    # print(会心)

    arg = {'外功': 20, '阳性内功': 100, '阴性内功': 200, '混元内功': 80, '毒性内功': 50}
    会心 = 复杂属性_外阳阴混毒(arg)
    print(会心)


if __name__ == '__main__':
    test_func()
