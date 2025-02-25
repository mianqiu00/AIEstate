SEED = 2025

DATA_COLUMNS = ['baseUrl', 'url', 'title', 'priceTotal', 'priceUnit', 'roomInfo', 
                'typeInfo', 'areaInfo', 'aroundInfo', 'introContent', 'transaction', 
                'baseInfo']

HOUSEINFO_DICT = {
    'priceTotal': '总价格',  # 房屋的总价格
    'shi': '室',  # 房屋的卧室数量
    'ting': '厅',  # 房屋的客厅数量
    'wei': '卫生间',  # 房屋的卫生间数量
    'floor_loc': '所在楼层',  # 房屋所在的楼层
    'total_floors': '总楼层',  # 房屋所在建筑的总楼层数
    'east': '房屋面朝东',  # 房屋是否朝东
    'west': '房屋面朝西',  # 房屋是否朝西
    'south': '房屋面朝南',  # 房屋是否朝南
    'north': '房屋面朝北',  # 房屋是否朝北
    'floor_type': '户型结构',  # 房屋的户型结构（如平层、复式等）
    'decoration_type': '装修类型',  # 房屋的装修类型（如精装、简装等）
    'area': '建筑面积',  # 房屋的建筑面积
    'construct_time': '建筑时间',  # 房屋的建筑时间
    'construct_type': '建筑类型',  # 房屋的建筑类型（如砖混、钢混等）
    'location': '所在区',  # 房屋所在的区域
    'lng': '经度',  # 房屋所在地的经度
    'lat': '纬度',  # 房屋所在地的纬度
    'area_in': '套内面积',  # 房屋的套内面积
    'construct_instruct': '建筑结构',  # 房屋的建筑结构（如框架结构、剪力墙结构等）
    'villa_type': '别墅类型',  # 若户型结构为别墅，则表示别墅类型
    'ti': '梯',  # 如果有电梯，表示电梯数量
    'hu': '户',  # 如果有电梯，表示每层户数
    'heating_type': '供暖方式',  # 房屋的供暖方式（如集中供暖、自采暖等）
    'elevator': '是否有电梯',  # 房屋是否有电梯
    'listing_time': '挂牌时间',  # 房屋的挂牌时间
    'ownership': '交易权属',  # 房屋的交易权属（如商品房、经济适用房等）
    'last_transaction': '上次交易时间',  # 房屋的上次交易时间
    'application': '房屋用途',  # 房屋的用途（如住宅、商业等）
    'houselife': '房屋年限',  # 房屋的使用年限
    'house_property': '产权所属',  # 房屋的产权所属（如个人、公司等）
    'mortgage': '是否抵押',  # 房屋是否抵押
    'mortgage_amount': '抵押金额',  # 如果有抵押，表示抵押金额
    'mortgage_repay': '偿还类型',  # 如果有抵押，表示偿还类型
    'spare': '房本备件',  # 房本备件情况
    'quota_policy': '限购政策',  # 房屋所在地的限购政策
    'LPR_policy': '利率政策'  # 房屋所在地的利率政策
}

ROOMINFO_COLUMNS = ['shi', 'ting', 'wei', 'floor_loc', 'total_floors']

TYPEINFO_COLUMNS = ['east', 'west', 'south', 'north', 'floor_type', 'decoration_type', 'villa_type']

AREAINFO_COLUMNS = ['area', "area_in", 'construct_time', 'construct_type', 'construct_instruct']

AROUNDINFO_COLUMNS = [('lng', 'lat'), 'location']

BASEINFO_COLUMNS = ['ti', 'hu', 'heating_type', 'elevator']

TRANSACTION_COLUMNS = ['listing_time', 'ownership', 'last_transaction', 'application', 'houselife', 
                       'house_property', 'mortgage', 'mortgage_amount', 'mortgage_repay', 'spare']

MACROINFO_COLUMNS = ['quota_policy', 'LPR_policy']

LOCATION_MAPPING = {
    '海淀': 1, 
    '朝阳': 2, 
    '东城': 3, 
    '西城': 4,
}

FLOOR_MAPPING = {
    '低楼层': 2,
    '底层': 1,
    '中楼层': 3,
    '顶层': 5,
    '高楼层': 4,
    '地下室': 0,
}

FLOOR_TYPE_MAPPING = {
    '跃层': 1, 
    '错层': 2, 
    '暂无数据': -1, 
    '平层': 3, 
    '复式': 4,
}

DECORATION_TYPE_MAPPING = {
    '毛坯': 1, 
    '精装': 2, 
    '其他': 3, 
    '简装': 4,
}

CONSTRUCT_TYPE_MAPPING = {
    '塔楼': 1, 
    '板楼': 2, 
    '平房': 3, 
    '板塔结合': 4, 
    '暂无数据': -1,
}

CONSTRUCT_INSTRUCT_MAPPING = {
    '混合结构': 1, 
    '钢混结构': 2, 
    '未知结构': 7, 
    '砖混结构': 3, 
    '框架结构': 4, 
    '砖木结构': 5, 
    '钢结构': 6,
}

VILLA_TYPE_MAPPING = {
    '叠拼': 1, 
    '联排': 2, 
    '独栋': 3,
}

HEATING_TYPE = {
    '集中供暖': 1, 
    '自供暖': 2, 
}

OWNERSHIP_TYPE = {
    '已购公房': 1, 
    '央产房': 2, 
    '二类经济适用房': 3, 
    '私产': 4, 
    '自住型商品房': 5, 
    '一类经济适用房': 6, 
    '定向安置房': 7, 
    '限价商品房': 8, 
    '商品房': 9
}

APPLICATION_TYPE = {
    '集体宿舍': 1, 
    '车库': 2, 
    '公寓': 3, 
    '普通住宅': 4, 
    '酒店式公寓': 5, 
    '服务式公寓': 6, 
    '平房': 7, 
    '商业办公类': 8, 
    '别墅': 9, 
    '四合院': 10, 
    '住宅式公寓': 11, 
    '商务型公寓': 12, 
}

HOUSELIFE_TYPE = {
    '满两年': 1, 
    '暂无数据': -1, 
    '未满两年': 0, 
    '满五年': 2
}

HOUSE_PROPERTY_TYPE = {
    '共有': 1, 
    '暂无数据': -1, 
    '非共有': 0
}

SPARE_TYPE = {
    '暂无数据': 0, 
    '已上传房本照片': 1, 
}

MORTGAGE_REPAY_TYPE = {
    '无抵押': 0.0, 
    '业主自还': 1, 
    '客户偿还': 2, 
    '金融公司垫资': 3, 
}

COLUMN_NAME_MAPPINGS = {
    'location': LOCATION_MAPPING,
    'floor_loc': FLOOR_MAPPING,
    'floor_type': FLOOR_TYPE_MAPPING,
    'decoration_type': DECORATION_TYPE_MAPPING,
    'construct_type': CONSTRUCT_TYPE_MAPPING,
    'construct_instruct': CONSTRUCT_INSTRUCT_MAPPING,
    'villa_type': VILLA_TYPE_MAPPING,
    'heating_type': HEATING_TYPE,
    'ownership': OWNERSHIP_TYPE,
    'application': APPLICATION_TYPE,
    'houselife': HOUSELIFE_TYPE,
    'house_property': HOUSE_PROPERTY_TYPE,
    'spare': SPARE_TYPE,
    'mortgage_repay': MORTGAGE_REPAY_TYPE,
}