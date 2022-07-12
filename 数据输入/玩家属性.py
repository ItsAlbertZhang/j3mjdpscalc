# coding:utf-8

if __name__ != '__main__':
    from . import 输入_通用格式处理
    from . import 输入_JX3BOX格式处理
    from . import 参考_系数
else:
    import 输入_通用格式处理
    import 输入_JX3BOX格式处理
    import 参考_系数


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


class 个体对象():
    '''
    每个个体对象是一个可操作的独立个体. 例如, 每个符合该属性模板的玩家, NPC 都是一个独立的个体对象.
    '''

    def __init__(self, 传入参数={}) -> None:
        # 这部分不使用装饰器定义的抽象属性, 因为没有为该属性定义 setter 方法.
        # 目的是在变更这些属性时必须调用对应的变动方法, 而不能直接使用 setter.
        心法主属性 = ['体质', '元气', '根骨', '力道', '身法']
        for elem in 心法主属性:
            setattr(self, '_'+elem, 简单属性())
        # 如果传入了参数, 那么按照参数进行属性设置
        for key in 传入参数:
            if key in 心法主属性:
                setattr(self, '_'+key, 简单属性(传入参数[key]))

        进阶属性 = {'攻击': '复杂属性_外阳阴混毒', '会心': '复杂属性_外阳阴混毒', '会心效果': '复杂属性_外阳阴混毒', '破防': '复杂属性_外阳阴混毒', '无双': '单属性', '加速': '单属性', '破招': '单属性', '气血': '单属性', '防御': '复杂属性_外阳阴混毒', '御劲': '单属性', '化劲': '单属性', '闪避': '单属性', '招架': '单属性', '招架效果': '单属性', '威胁': '单属性', '武器攻击速度': '单属性', '武器伤害基础': '单属性', '武器伤害浮动': '单属性'}
        for key in 进阶属性:
            if(进阶属性[key] == '复杂属性_外阳阴混毒'):
                setattr(self, key, 复杂属性_外阳阴混毒())
            if(进阶属性[key] == '单属性'):
                setattr(self, key, 简单属性())

        # 如果传入了参数, 那么按照参数进行属性设置
        for key in 传入参数:
            if key in 进阶属性:
                if(进阶属性[key] == '复杂属性_外阳阴混毒'):
                    setattr(self, key, 复杂属性_外阳阴混毒(传入参数[key]))
                if(进阶属性[key] == '单属性'):
                    setattr(self, key, 简单属性(传入参数[key]))

        # 进行传入数据的修正
        self.修正传入数据(传入参数)

    def 修正传入数据(self, 初始化参数={}) -> None:
        # 修正传入数据, 将百分比统一转换为数值
        转换系数 = (参考_系数.系数().获取转换系数())
        def 修正属性(属性, 是否为反比属性, 阈值, 转换系数):
            待处理简单属性列表 = []
            if isinstance(属性, 简单属性):
                待处理简单属性列表.append(属性)
            elif isinstance(属性, 复杂属性_外阳阴混毒):
                for key in 属性.attr:
                    待处理简单属性列表.append(getattr(属性, key))
            for elem in 待处理简单属性列表:
                if elem.基础 < 阈值:
                    if 是否为反比属性 == True:
                        elem.基础 = 转换系数 * elem.基础 / (1 - elem.基础)
                    else:
                        elem.基础 *= 转换系数
        # 心法主属性无需修正.
        正比属性阈值 = {'会心': 1, '会心效果': 3, '破防': 1, '无双': 1, '加速': 0.25, '御劲': 1, }
        反比属性阈值 = { '防御': 0.75, '闪避': 1, '破招': 1, }
        for key in 正比属性阈值:
            修正属性(getattr(self, key), False, 正比属性阈值[key], 转换系数[key])
        for key in 反比属性阈值:
            修正属性(getattr(self, key), False, 反比属性阈值[key], 转换系数[key])

    def 主属性转进阶属性基础(self):
        '''
        再次计算一次主属性转换进阶属性'基础值', 如 1 元气转 0.18 基础攻击与 0.3 基础破防.

        注意, 由门派心法转化的 心法主属性转换进阶属性的'额外值' 不在此处. 如焚影圣诀心法下 1 元气转 1.9 额外攻击与 0.29 会心.

        此方法只会在配装结束时使用一次. 由于计算器尚未内置配装模块, 因此此方法实际上并不会被调用, 所以先咕咕咕.
        '''
        pass

    def 输出dict结果(self):
        心法主属性 = ['体质', '元气', '根骨', '力道', '身法']
        进阶属性 = {'攻击': '复杂属性_外阳阴混毒', '会心': '复杂属性_外阳阴混毒', '会心效果': '复杂属性_外阳阴混毒', '破防': '复杂属性_外阳阴混毒', '无双': '单属性', '加速': '单属性', '破招': '单属性', '气血': '单属性', '防御': '复杂属性_外阳阴混毒', '御劲': '单属性', '化劲': '单属性', '闪避': '单属性', '招架': '单属性', '招架效果': '单属性', '威胁': '单属性', '武器攻击速度': '单属性', '武器伤害基础': '单属性', '武器伤害浮动': '单属性'}
        ret = {}
        for elem in 心法主属性:
            ret[elem] = getattr(self, elem).输出dict结果()
        for elem in 进阶属性:
            ret[elem] = getattr(self, elem).输出dict结果()
        return ret

    def __str__(self) -> str:
        return str(self.输出dict结果())

    # 抽象出心法主属性, 以便于在属性变动时执行操作

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
    # 会心 = 复杂属性_外阳阴混毒(arg)
    # print(会心)

    玩家 = 个体对象(输入_JX3BOX格式处理.JX3BOX数据().导出数据())
    print(玩家)


if __name__ == '__main__':
    test_func()
