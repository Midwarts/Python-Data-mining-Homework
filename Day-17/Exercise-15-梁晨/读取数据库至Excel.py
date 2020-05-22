import xlwt
import pymysql
#读取数据表中的数据并写入到Excel中
def get_sel_excel(file_excel):
    #建立连接
    conn = pymysql.connect(
        host = "100.100.100.0",
        port = 3306,
        user = "lc",
        passwd = "200101",
        db = "bigdata",
        charset = "utf8"
    )
    # 建立游标
    cursor = conn.cursor()
    sel_sql = "select * from film_equip;"
    print("开始查询表！")
    # 执行sql语句
    cursor.execute(sel_sql)
    # 获取查询到结果
    res = cursor.fetchall()
    print(res)

    # 操作excel
    def w_excel(res):
        book = xlwt.Workbook()  # 新建一个excel
        sheet = book.add_sheet('equipment')  # 新建一个sheet页
        title = ['id', 'name', 'rent', 'kind']
        # 写表头
        i = 0
        for header in title:
            sheet.write(0, i, header)
            i += 1

        # 写入数据
        for row in range(1, len(res)):
            for col in range(0, len(res[row])):
                sheet.write(row, col, res[row][col])
                row += 1
                col += 1
        book.save('equipment.xls')
        print("导出成功！")

    w_excel(res)#储存
    if __name__ == "__main__":
        file_excel = r"E:\Users\admin\PycharmProjects\untitled\filming_equipment.xls"
        get_sel_excel(file_excel)