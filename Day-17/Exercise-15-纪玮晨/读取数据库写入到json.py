import pymysql
import json

#连接数据库
db = pymysql.connect("rm-m5e63zf8ii67j7uq1zo.mysql.rds.aliyuncs.com","huabang_learning","huabang_201904","huabang_learning",charset = "utf8")

#使用cursor()方法创建游标对象
cursor = db.cursor()

sql = "select * from `jwc`"
cursor.execute(sql)#读取数据
all_data = cursor.fetchall()#所有数据

fields = [i[0] for i in cursor.description]#读取表头
print(fields)

with open("gdp.json","w") as f:
	json.dump(all_data,f)

f.close()

db.close()