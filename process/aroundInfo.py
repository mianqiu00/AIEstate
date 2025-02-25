import re


def aroundInfo_split(input_str):
    pattern = r"小区名称 (.*?) 地图 所在区域 (.*?) 看房时间"
    match = re.search(pattern, input_str)
    estate_name = match[1]
    location = match[2].replace('   ', ' ')

    return estate_name, location