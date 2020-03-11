import pymysql

# 打开数据库连接
db = pymysql.connect("10.10.10.10", "groupleader", "onlyleaders", "ncp")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果 by_area 表存在则删除
cursor.execute("DROP TABLE IF EXISTS by_area_province")

# 使用预处理语句创建表
sql = """CREATE TABLE by_area_province(
         name  VARCHAR(20),
         enName  VARCHAR(20),
         provinceName VARCHAR(20),
         maxZeroIncrDays  VARCHAR(20)
         )ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql)

# 关闭数据库连接
db.close()
