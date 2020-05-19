import json, xlwt
#读取弹幕文件导入python
with open(r"C:\Users\admin\Documents\GitHub\Python-Data-mining-Tutorial\Week-02\萝莉酱直播间时间切片弹幕.json", encoding='utf-8') as f:
    data = json.load(f)
    list1 = data['data']#转存为字典？
    # 创建excel文件
    book = xlwt.Workbook()
    # 创建一个表
    sheet = book.add_sheet('弹幕')
    # 存入第一行标题
    title = ['类别','发布时间','发布者','弹幕内容','弹幕包含颜文字']
for col in range(len(title)):
    sheet.write(0, col, title[col])
#写入数据（其实这一步不是很懂）
for i in range(0,len(list1)):#内容中的每一个词条
    for j in range(5):
        sheet.write(i+1,j,list1[i][j])
                  #（第几条词条，列数，内容）
        #保存表
        book.save('弹幕.xls')



