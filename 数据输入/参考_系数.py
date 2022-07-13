from doctest import REPORT_CDIFF
from pathlib import Path
import json


class 系数():
    def __init__(self) -> None:
        cwd = Path.cwd()
        with open(Path.joinpath(Path.joinpath(cwd, '数据输入'), '参考_系数.json'), 'rt', encoding='utf_8') as fp:
            self.原始数据 = json.load(fp)

    def 获取转换系数(self, 等级=110) -> dict:
        ret_dict = {}
        转换系数 = self.原始数据['转换系数']
        for key in 转换系数['全局系数']:
            ret_dict[key] = 转换系数['全局系数'][key] * (等级 * 转换系数['等级系数'] + 转换系数['等级常数'])
        # 对破招进行特殊处理
        ret_dict['破招'] = 转换系数['全局系数']['破招']
        return ret_dict

    def 获取心法转化系数(self) -> dict:
        ret_dict = {}
        心法转化系数 = self.原始数据['心法转化系数']
        for key in 心法转化系数:
            ret_dict[key] = 心法转化系数[key]
        return ret_dict