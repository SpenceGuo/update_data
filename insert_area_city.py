import pymysql
import json

#打开数据库连接
db = pymysql.connect("10.10.10.10", "groupleader", "onlyleaders", "ncp")

#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

name = ''
in_province = ''
enName = ''
cityName = ''
maxZeroIncrDays = ''

with open('by_area.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    # 将 JSON 对象转换为 Python 字典
    for item in json_data:
        if(item['name'] != '全国' and item['name'] != '非湖北'):
            for item1 in item['cityList']:
                in_province = item['name']

                if ('name' in item1):
                    name = str(item1['name'])
                else:
                    name = ''

                if ('enName' in item1):
                    enName = str(item1['enName']).replace('\'', ' ')
                else:
                    enName = ''

                if ('cityName' in item1):
                    cityName = str(item1['cityName'])
                else:
                    cityName = ''

                if ('maxZeroIncrDays' in item1):
                    maxZeroIncrDays = str(item1['maxZeroIncrDays'])
                else:
                    maxZeroIncrDays = ''

                sql = "INSERT INTO by_area_city(name, in_province, enName, cityName, maxZeroIncrDays) VALUES(\'" + name + "\',\'" + in_province + "\',\'" + enName + "\',\'" + cityName + "\',\'" + maxZeroIncrDays + "\')"
                print(sql)
                cursor.execute(sql)
                db.commit()

db.close()
