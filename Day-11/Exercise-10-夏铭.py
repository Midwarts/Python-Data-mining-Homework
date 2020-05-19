import json
import openpyxl

def read():
    with open('聆听丶芒果鱼直播间时间切片弹幕.json', 'r', encoding='utf-8') as f:
        json_data=json.load(f)
        data=json_data['data']
        return data
    #路径需更改

def write_excel_xlsx(path, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    sheet['A1'] = '类别'
    sheet['B1'] = '发布时间'
    sheet['C1'] = '发布者'
    sheet['D1'] = '发布内容'
    for i in range(1, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
    workbook.save('聆听丶芒果鱼直播间时间切片弹幕.xlsx')#路径自由选择
    print("xlsx格式表格写入数据成功！")


if __name__ == '__main__':
    data = read()
    write_excel_xlsx('聆听丶芒果鱼直播间时间切片弹幕', '弹幕', data)