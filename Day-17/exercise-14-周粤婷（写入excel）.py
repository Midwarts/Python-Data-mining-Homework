import mysql.connector
from openpyxl import Workbook
wb = Workbook()
sheet = wb['Sheet']
cnn = mysql.connector.connect(user='root',passwd='',database='test')
mycursor =cnn.cursor()#用cursor的方法获取操作游标
mycursor.execute("SELECT * FROM Student")#用execute执行SQL语句
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
print(myresult)
fields = mycursor.description#通过检索条件获取表头
# print(fields)
# print(len(fields))
cursor.close()
conn.close()
field_name = []
for field in fields:
      field_name.append(field[0])
sheet.append(field_name)
for row in range(2,len(myresult)+2):
    for col in range(1,len(fields)+1):
        # print(myresult[row-2])#元组数据
        # print(type(myresult[row-2][col-1]))#元组内的元素
        sheet.cell(row=row,column=col).value = u'%s' % myresult[row-2][col-1]
    # sheet.append({row:u'%s' % list(myresult[row-2])})#试图一行写入但是不行
wb.save("数据库写入表格.exel")