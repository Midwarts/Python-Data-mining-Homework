import xlwt
import json
#打开一个excel文件
book = xlwt.Workbook(encoding = 'utf-8')
#创建一个工作表
sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok = True)
#创建标题样式
style = xlwt.XFStyle() # 初始化样式
font = xlwt.Font() # 为样式创建字体
font.name = '宋体'
font.bold = True # 加粗
style.font = font
#创建标题单元格背景
pat = xlwt.Pattern()
pat.pattern = xlwt.Pattern.SOLID_PATTERN
pat.pattern_fore_colour = 5
style.pattern = pat
#居中
alignment = xlwt.Alignment()
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment
#写入初始化标题
sheet1.write(0,0,'类别',style)
sheet1.write(0,1,'发布时间',style)
sheet1.write(0,2,'发布者',style)
sheet1.write(0,3,'弹幕内容',style)
sheet1.write(0,4,'弹幕包含颜文字',style)
#写入萝莉酱数据
with open(r"E:\大学\项目\华榜\培训\Python-Data-mining-Tutorial\Week-02\萝莉酱直播间时间切片弹幕.json", "rb") as file:
    content = json.load(file)["data"]
q = 0
for i in content:
    q += 1
    for j in range(5):
        sheet1.write(q,j,i[j])
#设置列宽与保存excel文件
sheet1.col(0).width = 444
sheet1.col(1).width = 1360
sheet1.col(2).width = 1450
sheet1.col(3).width = 1900
sheet1.col(4).width = 1000
book.save("E:\大学\项目\华榜\培训\Exercise\excel_data.xls")