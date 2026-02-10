ITEM_MAP = {
    "10941": "53%vol 500ml贵州茅台酒（甲辰龙年）",
    "10942": "53%vol 375ml×2贵州茅台酒（甲辰龙年）",
    "10056": "53%vol 500ml茅台1935",
    "2478": "53%vol 500ml贵州茅台酒（珍品）"
}

# 需要预约的商品(默认只预约2个兔茅)
########################
ITEM_CODES = ['10941', '10942']

# push plus 微信推送,具体使用参考  https://www.pushplus.plus
# 例如： PUSH_TOKEN = '123456'
########################
# 不填不推送消息，一对一发送
PUSH_TOKEN = None
########################

import os
# credentials 路径
# 默认使用项目目录下的 credentials 文件
########################
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), 'credentials')
########################

# 预约规则配置
########################
# 预约本市出货量最大的门店
MAX_ENABLED = True
# 预约你的位置附近门店
DISTANCE_ENABLED = False
########################
