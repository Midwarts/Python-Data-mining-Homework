import pymysql
import xlwt

def get_excel(file_excel):
    #建立连接
    con = pymysql.connect(
        host = "100.100.100.0",
        port = 3306,
        user = "test",
        passwd = "123",
        db = "bigdata",
        charset = "utf8"
    )

    cursor = con.cursor()
    sel_sql = "select * from exercise-14-郑妍;"
    cursor.execute(sel_sql)
    res = cursor.fetchall()
    w_excel(res)
    w_json(res)


def w_excel(res):
    book = xlwt.Workbook() 
    sheet = book.add_sheet('sheet1') 
    title = ['id','姓名','出生日期','年龄','性别']

    #写入数据
    for row in range(0,len(res)):
        for col in range(0,len(res[row])):
            sheet.write(row,col,res[row][col])
        row+=1
    col+=1
    book.save('exercise-14-郑妍')


if __name__ == "__main__":
    file_excel = r"exercise-14-郑妍.xls"
    get_excel(file_excel)
