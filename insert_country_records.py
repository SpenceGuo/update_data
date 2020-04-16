import pymysql
import json

#打开数据库连接
db = pymysql.connect("10.10.10.10", "groupleader", "onlyleaders", "ncp")

#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

confirmedCount = ''
suspectedCount = ''
curedCount = ''
deadCount = ''
seriousCount = ''
suspectedIncreased = ''
confirmedIncreased = ''
curedIncreased = ''
deadIncreased = ''
seriousIncreased = ''
updateTime = ''
insickCount = ''
lastUpdate = ''
updateDate = ''
seriousRate = ''
seriousDayRate = ''
suspectedAccum = ''
suspectedDayProcessed = ''
suspectedConfirmedCount = ''
suspectedConfirmedRate = ''
suspectedProcessedRate = ''
suspectedDayConfirmedRate = ''

with open('by_area.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    # 将 JSON 对象转换为 Python 字典
    for key in json_data:
        #print(key['records'])
        for item in key['records']:
            if ('confirmedCount' in item):
                confirmedCount = str(item['confirmedCount'])
            else:
                confirmedCount = ''

            if ('suspectedCount' in item):
                suspectedCount = str(item['suspectedCount'])
            else:
                suspectedCount = ''

            if ('curedCount' in item):
                curedCount = str(item['curedCount'])
            else:
                curedCount = ''

            if ('deadCount' in item):
                deadCount = str(item['deadCount'])
            else:
                deadCount = ''

            if ('seriousCount' in item):
                seriousCount = str(item['seriousCount'])
            else:
                seriousCount = ''

            if ('suspectedIncreased' in item):
                suspectedIncreased = str(item['suspectedIncreased'])
            else:
                suspectedIncreased = ''

            if ('confirmedIncreased' in item):
                confirmedIncreased = str(item['confirmedIncreased'])
            else:
                confirmedIncreased = ''

            if ('curedIncreased' in item):
                curedIncreased = str(item['curedIncreased'])
            else:
                curedIncreased = ''

            if ('deadIncreased' in item):
                deadIncreased = str(item['deadIncreased'])
            else:
                deadIncreased = ''

            if ('seriousIncreased' in item):
                seriousIncreased = str(item['seriousIncreased'])
            else:
                seriousIncreased = ''

            if ('updateTime' in item):
                updateTime = str(item['updateTime'])
            else:
                updateTime = ''

            if ('insickCount' in item):
                insickCount = str(item['insickCount'])
            else:
                insickCount = ''

            if ('lastUpdate' in item):
                lastUpdate = str(item['lastUpdate'])
            else:
                lastUpdate = ''

            if ('updateDate' in item):
                updateDate = str(item['updateDate'])
            else:
                updateDate = ''

            if ('seriousRate' in item):
                seriousRate = str(item['seriousRate'])
            else:
                seriousRate = ''

            if ('seriousDayRate' in item):
                seriousDayRate = str(item['seriousDayRate'])
            else:
                seriousDayRate = ''

            if ('suspectedAccum' in item):
                suspectedAccum = str(item['suspectedAccum'])
            else:
                suspectedAccum = ''

            if ('suspectedDayProcessed' in item):
                suspectedDayProcessed = str(item['suspectedDayProcessed'])
            else:
                suspectedDayProcessed = ''

            if ('suspectedConfirmedCount' in item):
                confirmedCount = str(item['suspectedConfirmedCount'])
            else:
                suspectedConfirmedCount = ''

            if ('suspectedConfirmedRate' in item):
                suspectedConfirmedRate = str(item['suspectedConfirmedRate'])
            else:
                suspectedConfirmedRate = ''

            if ('suspectedProcessedRate' in item):
                suspectedProcessedRate = str(item['suspectedProcessedRate'])
            else:
                suspectedProcessedRate = ''

            if ('suspectedDayConfirmedRate' in item):
                suspectedDayConfirmedRate = str(item['suspectedDayConfirmedRate'])
            else:
                suspectedDayConfirmedRate = ''

            sql = "INSERT INTO country_records(confirmedCount, suspectedCount, curedCount, deadCount, seriousCount, suspectedIncreased, confirmedIncreased, curedIncreased, deadIncreased, seriousIncreased, updateTime, insickCount, lastUpdate, updateDate, seriousRate, seriousDayRate, suspectedAccum, suspectedDayProcessed, suspectedConfirmedCount, suspectedConfirmedRate, suspectedProcessedRate, suspectedDayConfirmedRate) VALUES(\'" + confirmedCount + "\',\'" + suspectedCount + "\',\'" + curedCount + "\',\'" + deadCount + "\',\'" + seriousCount + "\',\'" + suspectedIncreased + "\',\'" + confirmedIncreased + "\',\'" + curedIncreased + "\',\'" + deadIncreased + "\',\'" + seriousIncreased + "\',\'" + updateTime + "\',\'" + insickCount + "\',\'" + lastUpdate + "\',\'" + updateDate + "\',\'" + seriousRate + "\',\'" + seriousDayRate + "\',\'" + suspectedAccum + "\',\'" + suspectedDayProcessed + "\',\'" + suspectedConfirmedCount + "\',\'" + suspectedConfirmedRate + "\',\'" + suspectedProcessedRate + "\',\'" + suspectedDayConfirmedRate + "\')"
            print(sql)
            cursor.execute(sql)
            db.commit()

        break

db.close()
