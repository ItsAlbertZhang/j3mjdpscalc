from pathlib import Path
import json


class 通用数据():
    def __init__(self) -> None:
        self.数据 = {}
        cwd = Path.cwd()
        print(cwd)
        with open(Path.joinpath(Path.joinpath(cwd, '数据输入'), '输入_通用格式.json'), 'rt', encoding='utf_8') as fp:
            self.数据 = json.load(fp)

    def __str__(self) -> str:
        return str(self.数据)

    def 导出数据(self) -> dict:
        return self.数据


def test_func():
    待处理数据 = 通用数据()
    print(待处理数据)


if __name__ == '__main__':
    test_func()
