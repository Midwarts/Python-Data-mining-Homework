import pypyodbc
import xlwt
import json

def write_excel (path, sheet_name, value):#将数据表写入excel
    index = len(value) # 获取需要写入数据的行数
    workbook = xlwt.Workbook()# 新建工作文件
    sheet = workbook.add_sheet(sheet_name)# 新建表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])# 根据对应行和列写入数据
    workbook.save(path)# 存储
    print("写入exerl表完成")

def write_json(add, arr):#将数据表写入json
    with open(add, 'a', encoding='utf-8', newline='') as f:
        json.dump(arr, f)
    f.close()
    return
def main():
    path_excel = "D:\360MoveData\Users\23612\Desktop\\大二下\\python华榜\\excel\\lisibo数据库.xls"
    path_json = "D:\360MoveData\Users\23612\Desktop\\大二下\\python华榜\\lisibo数据库.json"
    str = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=D:\360MoveData\Users\23612\Desktop\\大二下\\python华榜\\lisibo数据库.accdb'
    try:
        db = pypyodbc.win_connect_mdb(str)  # 打开数据库连接
        curser = db.cursor()  # cursor游标
        curser.execute(" Book number 书籍编号  作者='高尔基' press BY ID;price BY ID; ")
        for col in curser.description:  # 显示行描述
            result = curser.fetchall()
        for row in result:  # 输出各字段的值
            print(row)
        write_excel(path_excel, 'sheet_1', result)
        write_json(path_json, result)
    except IOError as e:
        print(e)


if __name__ == '__main__':
    main()