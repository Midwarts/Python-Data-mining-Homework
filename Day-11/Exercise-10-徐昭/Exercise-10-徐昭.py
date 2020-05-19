"""
目的：将弹幕json转化为excel
作者：徐昭
"""
import openpyxl
import json

# 新建表格
wb = openpyxl.Workbook()
sheet = wb.create_sheet()
# 美化表格
sheet.column_dimensions['A'].width = 10
sheet.column_dimensions['B'].width = 20
sheet.column_dimensions['C'].width = 20
sheet.column_dimensions['D'].width = 50
# 表头赋值
sheet['A1'] = '类别'
sheet['B1'] = '发布时间'
sheet['C1'] = '发布者'
sheet['D1'] = '弹幕内容'
json_path = 'E:\\Python\\danmu.json'
# 读取JSON文件
with open(json_path, 'r', encoding='utf8') as f:
    danmu = json.load(f)
    data = danmu["data"]
    # 循环填充表头下方的表格
    for j in range(0, len(data)):
        for id in range(0, 4):
            sheet[chr(ord('A') + id) + str(j + 2)] = data[j][id]
# 保存文件
wb.save('E:\\Python\\danmu.xlsx')
