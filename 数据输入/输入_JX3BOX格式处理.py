# 本文件为导入 JX3BOX 配装数据 (https://www.jx3box.com/pz/) 的处理模块

from pathlib import Path
import json


class JX3BOX数据():
    def __init__(self) -> None:
        self.数据 = {}
        cwd = Path.cwd()
        with open(Path.joinpath(Path.joinpath(cwd, '数据输入'), '输入_JX3BOX格式.json'), 'rt', encoding='utf_8') as fp:
            self.数据 = json.load(fp)

            with open(Path.joinpath(Path.joinpath(cwd, '数据输入'), '参考_JX3BOX转通用.json'), 'rt', encoding='utf_8') as fp:
                参考_JX3BOX转通用 = json.load(fp)
                for key1 in list(self.数据.keys()):
                    if key1 in 参考_JX3BOX转通用['属性']:
                        data = self.数据.pop(key1)
                        self.数据[参考_JX3BOX转通用['属性'][key1]] = data
                    else:
                        for key2 in 参考_JX3BOX转通用['外阳阴混毒']:
                            if key2 in key1:
                                data = self.数据.pop(key1)
                                try:
                                    if 参考_JX3BOX转通用['属性'][key1.replace(key2, '')] not in self.数据:
                                        self.数据[参考_JX3BOX转通用['属性'][key1.replace(key2, '')]] = {}
                                    self.数据[参考_JX3BOX转通用['属性'][key1.replace(key2, '')]][参考_JX3BOX转通用['外阳阴混毒'][key2]] = data
                                except:
                                    pass
                # 明教特殊处理
                for key in list(self.数据.keys()):
                    if type(self.数据[key]) == dict:
                        if '阳性内功' not in self.数据[key]:
                            try:
                                self.数据[key]['阳性内功'] = self.数据[key]['阴性内功']
                            except:
                                self.数据[key]['阳性内功'] = 0
                        if '阴性内功' not in self.数据[key]:
                            try:
                                self.数据[key]['阴性内功'] = self.数据[key]['阳性内功']
                            except:
                                self.数据[key]['阴性内功'] = 0

    def __str__(self) -> str:
        return str(self.数据)

    def 导出数据(self) -> dict:
        return self.数据


def test_func():
    待处理数据 = JX3BOX数据()
    print(待处理数据)


if __name__ == '__main__':
    test_func()
