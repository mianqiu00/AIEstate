import re
from utils import chinese_to_number
from utils import FLOOR_TYPE_MAPPING, CONSTRUCT_TYPE_MAPPING, FLOOR_MAPPING, CONSTRUCT_INSTRUCT_MAPPING, DECORATION_TYPE_MAPPING, VILLA_TYPE_MAPPING, HEATING_TYPE


def insert_space(pattern, input_str):
    if pattern in input_str:
        return input_str.replace(' ' + pattern, '\n' + pattern)
    else:
        return input_str

def sub_introContent_split_1(input_str):
    if not input_str:
        return -1, -1, -1
    shi_match = re.search(r"(\d+)室", input_str)
    ting_match = re.search(r"(\d+)厅", input_str)
    wei_match = re.search(r"(\d+)卫", input_str)

    shi = int(shi_match.group(1)) if shi_match else -1
    ting = int(ting_match.group(1)) if ting_match else -1
    wei = int(wei_match.group(1)) if wei_match else -1

    return shi, ting, wei

def sub_introContent_split_2(input_str):
    if not input_str:
        return -1
    if '暂无' in input_str:
        area = -1
    area = float(input_str[:-1])

    return area

def sub_introContent_split_3(input_str):
    if not input_str:
        return -1
    else:
        return FLOOR_TYPE_MAPPING.get(input_str)

def sub_introContent_split_4(input_str):
    if not input_str:
        return -1
    else:
        return CONSTRUCT_TYPE_MAPPING.get(input_str)

def sub_introContent_split_5(input_str):
    if not input_str:
        return -1
    else:
        return FLOOR_MAPPING.get(input_str)

def sub_introContent_split_8(input_str):
    if not input_str:
        return -1
    elif '暂无' in input_str:
        return -1
    else:
        return float(input_str[:-1])

def sub_introContent_split_9(input_str):
    east, west, south, north = 0, 0, 0, 0
    if '东' in input_str: east = 1
    if '西' in input_str: west = 1
    if '南' in input_str: south = 1
    if '北' in input_str: north = 1
    if '暂无' in input_str: east, west, south, north = -1, -1, -1, -1
    return east, west, south, north

def sub_introContent_split_10(input_str):
    if not input_str:
        return -1
    elif '暂无' in input_str:
        return -1
    else:
        return CONSTRUCT_INSTRUCT_MAPPING.get(input_str)
    
def sub_introContent_split_11(input_str):
    if not input_str:
        return -1
    elif '暂无' in input_str:
        return -1
    else:
        return DECORATION_TYPE_MAPPING.get(input_str)
    
def sub_introContent_split_12(input_str):
    if not input_str:
        return -1
    elif '暂无' in input_str:
        return -1
    else:
        return VILLA_TYPE_MAPPING.get(input_str)
    
def sub_introContent_split_13(input_str):
    if not input_str:
        return -1, -1
    elif '暂无' in input_str:
        return -1, -1
    else:
        pattern = r"([一二两三四五六七八九十百]+)梯([一二两三四五六七八九十百]+)户"
        match = re.search(pattern, input_str)
        ti = chinese_to_number(match.group(1))
        hu = chinese_to_number(match.group(2))
        return ti, hu
    
def sub_introContent_split_14(input_str):
    if not input_str:
        return -1
    elif '暂无' in input_str:
        return -1
    else:
        return HEATING_TYPE.get(input_str)
    
def sub_introContent_split_15(input_str):
    if not input_str:
        return 0
    elif '暂无' in input_str:
        return 0
    else:
        return 1

def introContent_split(input_str):
    input_str = ' ' + input_str 
    pattern = r"(?:\s*房屋户型\s*([\w\d]+))?" \
              r"(?:\s*建筑面积\s*([\d.]+㎡))?" \
              r"(?:\s*户型结构\s*([\w]+))?" \
              r"(?:\s*建筑类型\s*([\w]+))?" \
              r"(?:\s*所在楼层\s*([\w]+))?" \
              r"(?:\s*\(共(\d+)层\))?" \
              r"(?:\s*咨询楼层)?" \
              r"(?:\s*楼层高度\s*([\w]+))?" \
              r"(?:\s*套内面积\s*([\w\d.㎡]+))?" \
              r"(?:\s*咨询套内面积)?" \
              r"(?:\s*房屋朝向(?:\s(东南|西南|东北|西北|东|南|西|北))+\s)?" \
              r"(?:\s*建筑结构\s*([\w]+))?" \
              r"(?:\s*装修情况\s*([\w]+))?" \
              r"(?:\s*别墅类型\s*([\w]+))?" \
              r"(?:\s*梯户比例\s*([\w\d]+))?" \
              r"(?:\s*供暖方式\s*([\w]+))?" \
              r"(?:\s*配备电梯\s*([\w]+))?"

    match = re.search(pattern, input_str)

    keys = [
        "房屋户型", "建筑面积", "户型结构", "建筑类型", "所在楼层", 
        "总楼层", "楼层高度", "套内面积", "房屋朝向", "建筑结构", 
        "装修情况", "别墅类型", "梯户比例", "供暖方式", "配备电梯"
    ]

    values = match.groups()
    result = {key: (value.strip() if value else None) for key, value in zip(keys, values)}
    
    shi, ting, wei = sub_introContent_split_1(result.get("房屋户型"))
    area = sub_introContent_split_2(result.get("建筑面积"))
    floor_type = sub_introContent_split_3(result.get("户型结构"))
    construct_type = sub_introContent_split_4(result.get("建筑类型"))
    floor_loc = sub_introContent_split_5(result.get("所在楼层"))
    total_floors_1 = int(result.get("总楼层")) if result.get("总楼层") else -1
    total_floors_2 = int(result.get("楼层高度")) if result.get("楼层高度") and not result.get("楼层高度") == "暂无数据" else -1
    total_floors = max(total_floors_1, total_floors_2)
    area_in = sub_introContent_split_8(result.get("套内面积"))
    east, west, south, north = sub_introContent_split_9(input_str)
    construct_instruct = sub_introContent_split_10(result.get("建筑结构"))
    decoration_type = sub_introContent_split_11(result.get("装修情况"))
    villa_type = sub_introContent_split_12(result.get("别墅类型"))
    ti, hu = sub_introContent_split_13(result.get("梯户比例"))
    heating_type = sub_introContent_split_14(result.get("供暖方式"))
    elevator = sub_introContent_split_15(result.get("配备电梯"))
    
    args = (shi, ting, wei, 
            area, floor_type, construct_type, floor_loc, total_floors, area_in, 
            east, west, south, north, 
            construct_instruct, decoration_type, villa_type, 
            ti, hu, 
            heating_type, elevator)

    return args