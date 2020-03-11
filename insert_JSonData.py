import pymysql
import json

#打开数据库连接
db = pymysql.connect("localhost", "root", "", "ncp")

#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

name = ''
enName = ''
provinceName = ''
lastUpdate = ''
updateTime = ''
zipCode = ''
confirmedCount = ''
suspectedCount = ''
curedCount = ''
deadCount = ''
insickCount = ''
confirmedIncreased = ''
curedIncreased = ''
deadIncreased = ''
maxZeroIncrDays = ''

with open('by_area.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    # 将 JSON 对象转换为 Python 字典
    for item in json_data:
        if ('name' in item):
            name = item['name']
        else:
            name = ''

        if ('enName' in item):
            enName = item['enName']
        else:
            enName = ''

        if ('provinceName' in item):
            provinceName = item['provinceName']
        else:
            provinceName = ''

        if ('lastUpdate' in item):
            lastUpdate = item['lastUpdate']
        else:
            lastUpdate = ''

        if ('updateTime' in item):
            updateTime = item['updateTime']
        else:
            updateTime = ''

        if ('zipCode' in item):
            zipCode = item['zipCode']
        else:
            zipCode = ''

        if ('confirmeCount' in item):
            confirmedCount = item['confirmeCount']
        else:
            confirmedCount = ''

        if ('suspectedCount' in item):
            suspectedCount = item['suspectedCount']
        else:
            suspectedCount = ''

        if ('curedCount' in item):
            curedCount = item['curedCouunt']
        else:
            curedCount = ''

        if ('deadCount' in item):
            deadCount = item['deadCounut']
        else:
            deadCount = ''

        if ('insickCount' in item):
            insickCount = item['insickCount']
        else:
            insickCount = ''

        if ('confirmedIncreased' in item):
            confirmedIncreased = item['confirmedIncreased']
        else:
            confirmedIncreased = ''

        if ('curedIncreased' in item):
            curedIncreased = item['curedIncreased']
        else:
            curedIncreased = ''


        # for item1 in item['records']:
        #     print(item1['lastUpdate'])
        # print(item)

"""

"""
# # Python 字典类型转换为 JSON 对象
# data = {
#     "name": "广东省",
#     "enName": "Guangdong",
#     "provinceName": "广东省",
#     "records": "01",
#     "lastUpdate": "2020-03-09T04:09:24.843Z",
#     "updateTime": "3/9",
#     "zipCode": "440000",
#     "confirmedCount": 1352,
#     "suspectedCount": 0,
#     "curedCount": 1260,
#     "deadCount": 8,
#     "insickCount": 84,
#     "cityList": "01",
#     "confirmedIncreased": 0,
#     "curedIncreased": 4,
#     "deadIncreased": 1,
#     "maxZeroIncrDays": 3
# }
#
# json_str = json.dumps(data)
# print("Python 原始数据：", repr(data))
#
# # 将 JSON 对象转换为 Python 字典
# data2 = json.loads(json_data)
# print("data2['name']: ", data2['name'])
# print("data2['url']: ", data2['enName'])
