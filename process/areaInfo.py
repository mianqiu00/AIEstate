from utils import CONSTRUCT_TYPE_MAPPING


def areaInfo_split(input_str):
    area, construct = input_str.split()
    area = float(area.split('平米')[0])
    if  '/' in construct:
        if '-1年' in input_str: 
            construct_time = -1
        else:
            construct_time = int(construct[:4])
    else:
        construct_time = -1
    construct_type = construct.split('/')[-1]
    return area, construct_time, CONSTRUCT_TYPE_MAPPING.get(construct_type)