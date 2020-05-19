import xlwt
import json

book = xlwt.Workbook(encoding='utf-8')
sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)

style = xlwt.XFStyle()

sheet1.write(0, 0, '类别', style)
sheet1.write(0, 1, '发布时间', style)
sheet1.write(0, 2, '发布者', style)
sheet1.write(0, 3, '弹幕内容', style)
sheet1.write(0, 4, '弹幕包含颜文字', style)
with open(r"E:\python\Exercise-01-刘雨萱\Test-03-刘雨萱\萝莉酱直播间时间切片弹幕.json", "rb") as file:
    content = json.load(file)["data"]
q = 0
for i in content:
    q += 1
    for j in range(5):
        sheet1.write(q, j, i[j])
print("导入成功")

book.save("E:\python\Exercise-01-刘雨萱\Exercise-10-刘雨萱\\test.xlsx")
