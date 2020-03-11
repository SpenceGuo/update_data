import pymysql

# 打开数据库连接
db = pymysql.connect("10.10.10.10", "groupleader", "onlyleaders", "ncp")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果 country_records 表存在则删除
cursor.execute("DROP TABLE IF EXISTS country_records")

# 使用预处理语句创建表
sql = """CREATE TABLE country_records(
         confirmedCount  VARCHAR(20),
         suspectedCount  VARCHAR(20),
         curedCount VARCHAR(20),
         deadCount  VARCHAR(20),
         seriousCount  VARCHAR(20),
         suspectedIncreased  VARCHAR(20),
         confirmedIncreased  VARCHAR(20),
         curedIncreased  VARCHAR(20),
         deadIncreased  VARCHAR(20),
         seriousIncreased  VARCHAR(20),
         updateTime  VARCHAR(20),
         insickCount  VARCHAR(20),
         lastUpdate  VARCHAR(30),
         updateDate  VARCHAR(20),
         seriousRate  VARCHAR(20),
         seriousDayRate  VARCHAR(20),
         suspectedAccum  VARCHAR(20),
         suspectedDayProcessed  VARCHAR(20),
         suspectedConfirmedCount  VARCHAR(20),
         suspectedConfirmedRate  VARCHAR(20),
         suspectedProcessedRate  VARCHAR(20),
         suspectedDayConfirmedRate  VARCHAR(20)
         )ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql)

# 关闭数据库连接
db.close()
