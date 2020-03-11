import pymysql
import json

#打开数据库连接
db = pymysql.connect("10.10.10.10", "groupleader", "onlyleaders", "ncp")

#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

name = ''
enName = ''
provinceName = ''
maxZeroIncrDays = ''

with open('by_area.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    # 将 JSON 对象转换为 Python 字典
    for item in json_data:
        if ('name' in item):
            name = str(item['name'])
        else:
            name = ''

        if ('enName' in item):
            enName = str(item['enName'])
        else:
            enName = ''

        if ('provinceName' in item):
            provinceName = str(item['provinceName'])
        else:
            provinceName = ''

        if ('maxZeroIncrDays' in item):
            maxZeroIncrDays = str(item['maxZeroIncrDays'])
        else:
            maxZeroIncrDays = ''

        sql = "INSERT INTO by_area_province(name, enName, provinceName, maxZeroIncrDays) VALUES(\'" + name + "\',\'" + enName + "\',\'" + provinceName + "\',\'" + maxZeroIncrDays + "\')"
        print(sql)
        cursor.execute(sql)
        db.commit()

db.close()
