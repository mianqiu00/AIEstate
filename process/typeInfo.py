from utils import FLOOR_TYPE_MAPPING, DECORATION_TYPE_MAPPING

def typeInfo_split(input_str):
    typeInfo_str = input_str.split()[-1]
    loc_str = ''.join(input_str.split()[:-1])
    floor_type = typeInfo_str.split("/")[0]
    decoration_type = typeInfo_str.split("/")[-1]
    east, west, south, north = 0, 0, 0, 0
    if '东' in loc_str: east = 1
    if '西' in loc_str: west = 1
    if '南' in loc_str: south = 1
    if '北' in loc_str: north = 1
    if '暂无数据' in loc_str: east, west, south, north = -1, -1, -1, -1
    return east, west, south, north, FLOOR_TYPE_MAPPING.get(floor_type), DECORATION_TYPE_MAPPING.get(decoration_type)