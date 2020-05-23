import pypyodbc
import xlwt
import json
#写入excel表中
def write_excel (path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")
#写入json格式中
def write_json(add, arr):
    with open(add, 'a', encoding='utf-8', newline='') as f:
        json.dump(arr, f)
    f.close()
    return


def main():
    path_excel = "E:\python\Exercise-01-刘雨萱\Exercise-14-刘雨萱\\Database-excel.xlsx"
    path_json = "E:\python\Exercise-01-刘雨萱\Exercise-14-刘雨萱\\Database-json.json"
    str = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=E:\python\Database-刘雨萱.accdb'
    try:
        db = pypyodbc.win_connect_mdb(str)  # 打开数据库连接
        curser = db.cursor()  # 产生cursor游标
        curser.execute("select * from address order by id desc")
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






'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=E:\python\Database-刘雨萱.accdb'
("E:\python\Exercise-01-刘雨萱\Exercise-14-刘雨萱\\Database-excel.xlsx")


