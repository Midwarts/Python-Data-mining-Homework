import pypyodbc
import win32com.client
import json
import time
path=r'D:\\python\\access.accdb'# 数据库文件
con=win32com.client.Dispatch(r'ADODB.Connection')
DSN="PROVIDER=Microsoft.ACE.OLEDB.12.0;DATA SOURCE="+path+";"
con.Open(DSN)
rs=win32com.client.Dispatch(r'ADODB.Recordset')
rs.Cursorlocation=3
rs.Open('SELECT TOP 1 * FROM 表1',con)
for i in range(0,rs.Fields.Count):
    print(rs.Fields[i].Name)
conn = pypyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + path + ";Uid=;Pwd=;")
cursor = conn.cursor()
SQL = "SELECT 表1.[编号], 表1.[名字], 表1.[年龄], 表1.[收养时间]FROM 表1;"#
cursor.execute(SQL)
data = cursor.fetchall()
print(data)
s = list(data[0]),list(data[1]),list(data[2]),list(data[3])
data = list(s)
print(data)
data[0][3] = time.strftime('%Y-%m-%d %H:%M:%S')
data[1][3] = time.strftime('%Y-%m-%d %H:%M:%S')
data[2][3] = time.strftime('%Y-%m-%d %H:%M:%S')
data[3][3] = time.strftime('%Y-%m-%d %H:%M:%S')
print(data)
data1 = {"number": data[0][0], "name": data[0][1], "age": data[0][2], "date": data[0][3]}
data2 ={"number": data[1][0], "name": data[1][1], "age": data[1][2], "date": data[1][3]}
data3 = {"number": data[2][0], "name": data[2][1], "age": data[2][2], "date": data[2][3]}
data4 = {"number": data[3][0], "name": data[3][1], "age": data[3][2], "date": data[3][3]}
data=[data1,data2,data3,data4]
print(data)
with open("D:\\python\\test.json", 'w', encoding='utf-8') as  f:
    for i in range(0,4):
        json.dump(data[i], f, indent=4, ensure_ascii=False)
print("写入json操作完成")


