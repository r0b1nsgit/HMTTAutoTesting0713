import os

import yaml

from config import BASE_PATH


def read_yaml(filename):
    # 测试数据
    arr = []
    # 读取文件 构造测试数据
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(file_path, 'r', encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f).values()
        for data in yaml_data:
            arr.append(tuple(data.values()))
    # 返回测试数据
    return arr
