if __name__ == '__main__':
    from .. import 数据输入

from 数据输入 import 玩家属性


class 状态效果():
    def __init__(self, 作用属性, 作用数值: 0, 作用1024分值: 0, 作用对象: None, 作用于心法主属性=False) -> None:
        '''
        如果该状态效果作用于心法主属性, 那么需要使用 '定义作用对象' 方法传入一个个体对象, 以便调用 '个体对象' 类中的心法主属性变动方法.
        '''
        self.作用属性 = []
        if isinstance(作用属性, 玩家属性.简单属性):
            self.作用属性.append(作用属性)
        elif isinstance(作用属性, 玩家属性.复杂属性_外阳阴混毒):
            for key in 作用属性.attr:
                self.作用属性.append(getattr(作用属性, key))
        self.作用数值 = 作用数值
        self.作用1024分值 = 作用1024分值
        self.作用对象 = 作用对象
        self.作用于心法主属性 = 作用于心法主属性

    def 定义作用对象(self, obj):
        '''
        obj 应为 '个体对象' 类.
        '''
        self.作用对象 = obj

    def 获得效果(self):
        for elem in self.作用属性:
            if not self.作用于心法主属性:
                self.作用属性[elem].额外 = self.作用数值
                self.作用属性[elem].额外1024分比 = self.作用1024分值
            else:
                try:
                    if self.作用对象.体质 == self.作用属性[elem]:
                        self.作用对象.体质变动(self.作用数值, self.作用1024分值)
                    if self.作用对象.元气 == self.作用属性[elem]:
                        self.作用对象.元气变动(self.作用数值, self.作用1024分值)
                    if self.作用对象.根骨 == self.作用属性[elem]:
                        self.作用对象.根骨变动(self.作用数值, self.作用1024分值)
                    if self.作用对象.力道 == self.作用属性[elem]:
                        self.作用对象.力道变动(self.作用数值, self.作用1024分值)
                    if self.作用对象.身法 == self.作用属性[elem]:
                        self.作用对象.身法变动(self.作用数值, self.作用1024分值)
                except:
                    print('未能成功获得效果.')

    def 失去效果(self):
        self.作用数值 = -self.作用数值
        self.作用1024分值 = -self.作用1024分值
        self.获得效果()
        self.作用数值 = -self.作用数值
        self.作用1024分值 = -self.作用1024分值
