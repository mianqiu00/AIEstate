import re
from utils import FLOOR_MAPPING

def roomInfo_split(input_str):
    num_bedrooms = -1
    num_living_rooms = -1
    floor_loc = -1
    total_floors = -1
    is_garage = 0

    pattern = r"(\d+)室(\d+)厅 (.*?)/共(\d+)层"
    match = re.search(pattern, input_str)

    if match:
        num_bedrooms = match.group(1)
        num_living_rooms = match.group(2)
        floor_loc = match.group(3)
        total_floors = match.group(4)
    elif '车位' in input_str:
        is_garage = 1
        if '暂无数据' in input_str:
            pass
        else:
            pattern = r"车位 (.*?)/共(\d+)层"
            match = re.search(pattern, input_str)
            if match:
                floor_loc = match.group(1)
                total_floors = match.group(2)
            else:
                print(input_str, '1')
                input()
    elif '暂无数据' in input_str:
        pattern = r"(\d+)室(\d+)厅 暂无数据"
        match = re.search(pattern, input_str)
        if match:
            num_bedrooms = match.group(1)
            num_living_rooms = match.group(2)
        else:
            pattern = r"暂无数据 (.*?)/共(\d+)层"
            match = re.search(pattern, input_str)
            if match:
                floor_loc = match.group(1)
                total_floors = match.group(2)
            else:
                print(input_str, 3)
                input()
    else:
        print(input_str, 2)
        input()
    
    return num_bedrooms, num_living_rooms, FLOOR_MAPPING.get(floor_loc, -1), total_floors, is_garage