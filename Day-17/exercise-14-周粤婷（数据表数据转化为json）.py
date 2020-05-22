import mysql.connector
import json
import os
con = mysql.connector.connect(user='root',passwd='',database='test')
mycursor =con.cursor()#用cursor的方法获取操作游标
mycursor.execute("SELECT * FROM Student")#用execute执行SQL语句
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
# print(myresult)
fields = mycursor.description#通过检索条件获取表头
# print(fields)
# print(len(fields))
mycursor.close()
con.close()
field_name = []
for field in fields:
      field_name.append(field[0])
print(field_name)
with open("%s/student_data.txt" % os.getcwd(),'w+') as f:
    for row in myresult:
        #建立data字典
        data = {}
        #将每一个元组（每一行）的数据写入字典
        for i in range(0,len(field_name)):
            data[field_name[i]] = row[i]
        data_json = json.dumps(data, ensure_ascii=False)
        # 写入文件
        f.write(data_json + '\n')
f.close()
