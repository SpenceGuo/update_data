import pymysql
import json

#打开数据库连接
db = pymysql.connect("10.10.10.10", "groupleader", "onlyleaders", "ncp")

#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

name = ''
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

with open('by_area.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    # 将 JSON 对象转换为 Python 字典
    for item in json_data:
        if(item['name'] != "全国"):
            for key in item['records']:
                if ('name' in key):
                    name = str(item['name'])
                else:
                    name = item['name']

                if ('lastUpdate' in key):
                    lastUpdate = str(key['lastUpdate'])
                else:
                    lastUpdate = ''

                if ('updateTime' in key):
                    updateTime = str(key['updateTime'])
                else:
                    updateTime = ''

                if ('zipCode' in key):
                    zipCode = str(key['zipCode'])
                else:
                    zipCode = ''

                if ('confirmedCount' in key):
                    confirmedCount = str(key['confirmedCount'])
                else:
                    confirmedCount = ''

                if ('suspectedCount' in key):
                    suspectedCount = str(key['suspectedCount'])
                else:
                    suspectedCount = ''

                if ('curedCount' in key):
                    curedCount = str(key['curedCount'])
                else:
                    curedCount = ''

                if ('deadCount' in key):
                    deadCount = str(key['deadCount'])
                else:
                    deadCount = ''

                if ('insickCount' in key):
                    insickCount = str(key['insickCount'])
                else:
                    insickCount = ''

                if ('confirmedIncreased' in key):
                    confirmedIncreased = str(key['confirmedIncreased'])
                else:
                    confirmedIncreased = ''

                if ('curedIncreased' in key):
                    curedIncreased = str(key['curedIncreased'])
                else:
                    curedIncreased = ''

                if ('deadIncreased' in key):
                    deadIncreased = str(key['deadIncreased'])
                else:
                    deadIncreased = ''

                sql = "INSERT INTO province_records(name, lastUpdate, updateTime, zipCode, confirmedCount, suspectedCount, curedCount, deadCount, insickCount, confirmedIncreased, curedIncreased, deadIncreased) VALUES (\'" + name + "\',\'" + lastUpdate + "\',\'" + updateTime + "\',\'" + zipCode + "\',\'" + confirmedCount + "\',\'" + suspectedCount + "\',\'" + curedCount + "\',\'" + deadCount + "\',\'" + insickCount + "\',\'" + confirmedIncreased + "\',\'" + curedIncreased + "\',\'" + deadIncreased + "\')"
                print(sql)
                cursor.execute(sql)
                db.commit()

        else:
            print(item)
            continue

        # sql = "INSERT INTO province_records(name, lastUpdate, updateTime, zipCode, confirmedCount, suspectedCount, curedCount, deadCount, insickCount, confirmedIncreased, curedIncreased, deadIncreased) VALUES (\'"+name+ "\',\'" +lastUpdate+ "\',\'" +updateTime+ "\',\'" +zipCode+ "\',\'" +confirmedCount+ "\',\'" +suspectedCount+ "\',\'" +curedCount+ "\',\'" +deadCount+ "\',\'" +insickCount+ "\',\'" +confirmedIncreased+ "\',\'" +curedIncreased+ "\',\'" +deadIncreased+ "\')"
        # print(sql)
        # cursor.execute(sql)
        # db.commit()

db.close()
