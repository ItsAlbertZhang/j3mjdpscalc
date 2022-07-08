# coding:utf-8

if __name__ != '__main__':
    from . import 输入_通用格式处理
    from . import 输入_JX3BOX格式处理
else:
    import 输入_通用格式处理
    import 输入_JX3BOX格式处理


class 属性():
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


class 外阳阴混毒():
    def __init__(self, arg={}) -> None:
        attr = ['外功', '阳性内功', '阴性内功', '混元内功', '毒性内功']
        for elem in attr:
            setattr(self, elem, 属性())
        # 如果传入了参数, 那么按照参数进行属性设置
        for key in arg:
            if key in attr:
                setattr(self, key, 属性(arg[key]))

    def 输出dict结果(self):
        attr = ['外功', '阳性内功', '阴性内功', '混元内功', '毒性内功']
        ret = {}
        for elem in attr:
            ret[elem] = getattr(self, elem).输出dict结果()
        return ret

    def __str__(self) -> str:
        return str(self.输出dict结果())


class 玩家属性():
    def __init__(self, arg={}) -> None:
        # 这部分不使用装饰器定义的抽象属性, 因为没有为该属性定义 setter 方法
        基础属性 = ['体质', '元气', '根骨', '力道', '身法']
        for elem in 基础属性:
            setattr(self, '_'+elem, 属性())
        # 如果传入了参数, 那么按照参数进行属性设置
        for key in arg:
            if key in 基础属性:
                setattr(self, '_'+key, 属性(arg[key]))

        进阶属性 = {'攻击': '外阳阴混毒', '会心': '外阳阴混毒', '会心效果': '外阳阴混毒', '破防': '外阳阴混毒', '无双': '单属性', '加速': '单属性', '破招': '单属性', '气血': '单属性', '防御': '外阳阴混毒', '御劲': '单属性', '化劲': '单属性', '闪避': '单属性', '招架': '单属性', '招架效果': '单属性', '威胁': '单属性', '武器攻击速度': '单属性', '武器伤害基础': '单属性', '武器伤害浮动': '单属性'}
        for key in 进阶属性:
            if(进阶属性[key] == '外阳阴混毒'):
                setattr(self, key, 外阳阴混毒())
            if(进阶属性[key] == '单属性'):
                setattr(self, key, 属性())
        # 如果传入了参数, 那么按照参数进行属性设置
        for key in arg:
            if key in 进阶属性:
                if(进阶属性[key] == '外阳阴混毒'):
                    setattr(self, key, 外阳阴混毒(arg[key]))
                if(进阶属性[key] == '单属性'):
                    setattr(self, key, 属性(arg[key]))
                # setattr(self, key, 属性(arg[key]))

    def 输出dict结果(self):
        基础属性 = ['体质', '元气', '根骨', '力道', '身法']
        进阶属性 = {'攻击': '外阳阴混毒', '会心': '外阳阴混毒', '会心效果': '外阳阴混毒', '破防': '外阳阴混毒', '无双': '单属性', '加速': '单属性', '破招': '单属性', '气血': '单属性', '防御': '外阳阴混毒', '御劲': '单属性', '化劲': '单属性', '闪避': '单属性', '招架': '单属性', '招架效果': '单属性', '威胁': '单属性', '武器攻击速度': '单属性', '武器伤害基础': '单属性', '武器伤害浮动': '单属性'}
        ret = {}
        for elem in 基础属性:
            ret[elem] = getattr(self, elem).输出dict结果()
        for elem in 进阶属性:
            ret[elem] = getattr(self, elem).输出dict结果()
        return ret

    def __str__(self) -> str:
        return str(self.输出dict结果())

    # 抽象出基础属性, 以便于在属性变动时执行操作

    @property
    def 体质(self):
        return self._体质

    def 体质变动(self, arg={}):
        for key in arg:
            if key == '额外':
                pass
            if key == '额外1024分比':
                pass

    @property
    def 元气(self):
        return self._元气

    def 元气变动(self, arg={}):
        for key in arg:
            if key == '额外':
                pass
            if key == '额外1024分比':
                pass

    @property
    def 根骨(self):
        return self._根骨

    def 根骨变动(self, arg={}):
        for key in arg:
            if key == '额外':
                pass
            if key == '额外1024分比':
                pass

    @property
    def 力道(self):
        return self._力道

    def 力道变动(self, arg={}):
        for key in arg:
            if key == '额外':
                pass
            if key == '额外1024分比':
                pass

    @property
    def 身法(self):
        return self._身法

    def 身法变动(self, arg={}):
        for key in arg:
            if key == '额外':
                pass
            if key == '额外1024分比':
                pass


def test_func() -> dict:
    # 会心 = 属性(50)
    # print(会心)

    # arg = {'外功': 20, '阳性内功': 100, '阴性内功': 200, '混元内功': 80, '毒性内功': 50}
    # 会心 = 外阳阴混毒(arg)
    # print(会心)

    玩家 = 玩家属性(输入_JX3BOX格式处理.JX3BOX数据().导出数据())
    print(玩家)


if __name__ == '__main__':
    test_func()
