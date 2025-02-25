from api import api_text_embedding


def baseInfo_split(input_str):
    input_str = input_str.split("本房源特色")[-1].strip()
    if "注：" in input_str:
        input_str = input_str.split("注：")[0]
    text_embedding = api_text_embedding(input_str)
    return text_embedding