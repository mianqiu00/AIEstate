import re
from utils import convert_date_format, OWNERSHIP_TYPE, APPLICATION_TYPE, HOUSELIFE_TYPE, HOUSE_PROPERTY_TYPE, SPARE_TYPE, MORTGAGE_REPAY_TYPE


def insert_space(pattern, input_str):
    if pattern in input_str:
        return input_str.replace(pattern, pattern + ' ').replace(' ' + pattern, '\n' + pattern)
    else:
        return input_str

def sub_transaction_split_7(input_str):
    def preprocess(input_str):
        mortgage, mortgage_amount, mortgage_bank, mortgage_repay = -1, -1, -1, -1

        if input_str == "暂无数据":
            return mortgage, mortgage_amount, mortgage_bank, mortgage_repay

        if "无抵押" in input_str:
            return 0, 0, 0, 0

        mortgage = 1
        input_str = input_str[3:].strip()

        match = re.search(r'([\d]+)(万元|万)?', input_str)
        if match:
            mortgage_amount = int(match.group(1))
            input_str = input_str[match.end():].strip()

        if '业主自还' in input_str or '客户偿还' in input_str:
            mortgage_repay = input_str[-4:]
            input_str = input_str[:-4].strip()
        if '金融公司垫资' in input_str:
            mortgage_repay = input_str[-6:]
            input_str = input_str[:-6].strip()

        mortgage_bank = input_str if input_str else -1

        return mortgage, mortgage_amount, mortgage_bank, mortgage_repay
    
    mortgage, mortgage_amount, mortgage_bank, mortgage_repay = preprocess(input_str)
    if mortgage_amount >= 10000: mortgage_amount /= 10000
    if not type(mortgage_repay) == int:
        mortgage_repay = MORTGAGE_REPAY_TYPE.get(mortgage_repay)
    return mortgage, mortgage_amount, mortgage_bank, mortgage_repay

def transaction_split(input_str):
    input_str = ' ' + input_str 
    input_str = insert_space("挂牌时间", input_str)
    input_str = insert_space("交易权属", input_str)
    input_str = insert_space("上次交易", input_str)
    input_str = insert_space("房屋用途", input_str)
    input_str = insert_space("房屋年限", input_str)
    input_str = insert_space("产权所属", input_str)
    input_str = insert_space("抵押信息", input_str)
    input_str = insert_space("房本备件", input_str)
    pattern = r"(?:\n挂牌时间\s*([\w\d]+))?" \
              r"(?:\n交易权属\s*([\w]+))?" \
              r"(?:\n上次交易\s*([\w\d]+))?" \
              r"(?:\n房屋用途\s*([\w]+))?" \
              r"(?:\n房屋年限\s*([\w]+))?" \
              r"(?:\n产权所属\s*([\w]+))?" \
              r"(?:\n抵押信息\s*([\w\x20]+))?" \
              r"(?:\n房本备件\s*([\w]+))?"
    
    match = re.search(pattern, input_str)
    keys = ["挂牌时间", "交易权属", "上次交易", "房屋用途", 
            "房屋年限", "产权所属", "抵押信息", "房本备件"]
    values = match.groups()
    result = {key: (value.strip() if value else None) for key, value in zip(keys, values)}
    
    listing_time = convert_date_format(result.get("挂牌时间"))
    ownership = OWNERSHIP_TYPE.get(result.get("交易权属"))
    last_transaction = convert_date_format(result.get("上次交易"))
    application = APPLICATION_TYPE.get(result.get("房屋用途"))
    houselife = HOUSELIFE_TYPE.get(result.get("房屋年限") if result.get("房屋年限") else "暂无数据")
    house_property = HOUSE_PROPERTY_TYPE.get(result.get("产权所属") if result.get("产权所属") else "暂无数据")
    mortgage_base = result.get("抵押信息") if result.get("抵押信息") else "暂无数据"
    mortgage, mortgage_amount, mortgage_bank, mortgage_repay = sub_transaction_split_7(mortgage_base)
    spare = SPARE_TYPE.get(result.get("房本备件") if result.get("房本备件") and not "经纪人" in result.get("房本备件") else "暂无数据")

    args = (listing_time, ownership, last_transaction, application, houselife, house_property, 
            mortgage, mortgage_amount, mortgage_bank, mortgage_repay, spare)
    return args