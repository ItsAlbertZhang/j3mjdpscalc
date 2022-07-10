from pathlib import Path
import json


class 转换系数():
    def __init__(self, 等级=110) -> None:
        self.数据 = {}
        cwd = Path.cwd()
        with open(Path.joinpath(Path.joinpath(cwd, '数据输入'), '参考_系数.json'), 'rt', encoding='utf_8') as fp:
            全局 = json.load(fp)
        全局 = 全局['全局']
        for key in 全局['全局系数']:
            self.数据[key] = 全局['全局系数'][key] * (等级 * 全局['等级系数'] + 全局['等级常数'])
        self.数据['破招'] = 全局['全局系数']['破招']

    def __str__(self) -> str:
        return str(self.数据)

    def 导出数据(self) -> dict:
        return self.数据


def test_func():
    待处理数据 = 转换系数()
    print(待处理数据)


if __name__ == '__main__':
    test_func()
