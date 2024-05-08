import json


# 封装获取测试数据的方法
def get_case_data(filename):
    with open(filename, encoding='utf-8') as f:
        case = json.load(f)
        print(case)
    list_case_data = []
    for case_data in case:
        list_case_data.append(tuple(case_data.values()))
    return list_case_data