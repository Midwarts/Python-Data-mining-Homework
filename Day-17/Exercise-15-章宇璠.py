import pypyodbc
import xlwt
import json
#写入excel表中
def write_excel (path, sheet_name, value):
    index = len(value)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
    workbook.save(path)
    print("xls格式表格写入数据成功！")
#写入json格式中
def write_json(add, arr):
    with open(add, 'a', encoding='utf-8', newline='') as f:
        json.dump(arr, f)
    f.close()
    return
def main():
    path_excel = "D:\\中国传媒大学\\大一下\\jupyter\\Database-excel.xls"
    path_json = "D:\\中国传媒大学\\大一下\\jupyter\\Database-json.json"
    str = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=D:\\中国传媒大学\\大一下\\jupyter\\data.accdb'
    try:
        db = pypyodbc.win_connect_mdb(str)  # 打开数据库连接
        curser = db.cursor()  # 产生cursor游标
        curser.execute("SELECT * FROM 职位简介 WHERE 职务='导演' ORDER BY ID;")
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

