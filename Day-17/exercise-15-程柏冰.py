# coding=utf-8
import pypyodbc
import xlwt
from xlwt import Workbook
import json

#链接access数据库
def mdb_conn(db_name, password = ""):
    str = 'Driver={Microsoft Access Driver (*.mdb)};PWD' + password + ";DBQ=" + db_name
    conn = pypyodbc.win_connect_mdb(str)
    return conn

def mdb_sel(cur, sql):
    try:
        cur.execute(sql)
        return cur.fetchall()
    except:
        return []

if __name__ == '__main__':
    pathfile = 'C:\\Users\\cbb\\Desktop\\exercise-14-程柏冰.accdb'
    tablename = '影视设备租借中传'
    conn = mdb_conn(pathfile)
    cur = conn.cursor()
    sql = "SELECT 影视设备租借中传.[ID],影视设备租借中传.[租金],影视设备租借中传.[设备],影视设备租借中传.[租赁公司位置] FROM 影视设备租借中传"
    sel_data = mdb_sel(cur, sql)
    print(sel_data)

# 创建一个Excel文件
    w = Workbook()
    ws = w.add_sheet('datas', cell_overwrite_ok=True)
    for i in range(len(sel_data)):

        for j in range(len(sel_data[i])):

            ws.write(i, j, sel_data[i][j])
            ws.write(0, 0, 'ID')
            ws.write(0, 1, '租金')
            ws.write(0, 2, '设备')
            ws.write(0, 3, '租赁公司位置')

    cur.close()
    conn.close()
    w.save('C:\\Users\\cbb\\Desktop\\exercise-15-程柏冰.xls')

#创建一个Json文件
    with open('C:\\Users\\cbb\\Desktop\\exercise-15-程柏冰.json', 'a', encoding='utf-8') as f:
        f.write(str(sel_data))
        f.close()
