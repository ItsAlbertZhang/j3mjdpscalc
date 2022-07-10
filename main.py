from 数据输入 import 玩家属性
from 数据输入 import 输入_JX3BOX格式处理


def main():
    玩家 = 玩家属性.玩家属性(输入_JX3BOX格式处理.JX3BOX数据().导出数据())
    # print(玩家)
    arg = 1024 + 玩家.破防.阳性内功.最终 - int((1024 + 玩家.破防.阳性内功.最终) * 358 / 1024)
    ret = int(int(玩家.破招.最终 * arg / 1024 * (1024 + 玩家.无双.最终) / 1024) * (1 + 246 / 1024))
    print(ret)


if __name__ == '__main__':
    main()
