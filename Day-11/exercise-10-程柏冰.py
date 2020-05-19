import json
import xlwt

data=[]
with open('C:\\Users\\cbb\\Desktop\\聆听丶芒果鱼直播间时间切片弹幕.json',encoding='utf8') as f:
    for line in f:
        data.append(json.loads(line))
workbook = xlwt.Workbook("exercise-10-程柏冰.xls")
worksheet = workbook.add_sheet("first_sheet")
worksheet.write(0, 0, '类别')
worksheet.write(0, 1, '发布时间')
worksheet.write(0, 2, '发布者')
worksheet.write(0, 3, '弹幕内容')
for i in range(len(data[0]['data'])):
    for j in range(4):
        worksheet.write(i+1, j, data[0]['data'][i][j])
workbook.save('C:\\Users\\cbb\\Desktop\\exercise-10-程柏冰.xls')