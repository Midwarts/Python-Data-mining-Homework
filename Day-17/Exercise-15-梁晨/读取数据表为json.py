import json
import pymysql


class Equipment(object):
    # 创建一个类，赋予每个字段为元素的一个属性，将列表中的每一项加入这个类
    def __init__(self, ID, name, rent, kind):
        self.ID = ID
        self.name = name
        self.rent = rent
        self.kind = kind



#读取数据表中的数据并写为Json格式的数据
#链接数据库
conn = pymysql.connect(
            host="100.100.100.0",
            port=3306,
            user="lc",
            passwd="200101",
            db="bigdata",
            charset="utf8"
        )
# 建立游标
cursor = conn.cursor()
sel_sql = "select * from film_equip;"
print("开始查询表！")
# 执行sql语句
cursor.execute(sel_sql)
# 获取查询到结果
res = cursor.fetchall()#返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))

#循环读取元组数据
#将元组数据转换为列表类型，每个条数据元素为字典类型:[{'字段1':'字段1的值','字段2':'字段2的值',...,'字段N:字段N的值'},{第二条数据},...,{第N条数据}]
equi_list=[]
for i in res:
        h = list(str(i()))
        equi_list.append(h)

#放到类里去赋予属性
equip_list1=[]
for i in equi_list:
    h=Equipment(i[0],i[1],i[2],i[3])
    equip_list1.append(h)

#转json
data = json.dumps(equip_list1)

#存为json文件
f = open(r'D:\getui\film_equip.txt','w+')
#写数据
f.write(data)
#关闭文件
f.close()