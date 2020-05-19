if __name__ == '__main__':
    import openpyxl
    import json
    wb = openpyxl.Workbook()
    sheet = wb.create_sheet("Mysheet", 0)
    with open('D:\\中国传媒大学\\大一下\\jupyter\\聆听丶芒果鱼直播间时间切片弹幕.json', 'r', encoding='utf8') as f:
        danmu = json.load(f)
        data = danmu["data"]
    sheet['A1'] = '类别'
    sheet['B1'] = '发布时间'
    sheet['C1'] = '发布者'
    sheet['D1'] = '弹幕内容'
    for j in range(0, len(data)):
        for i in range(0, 4):
            sheet[chr(ord('A') + i) + str(j + 2)] = data[j][i]
    sheet.column_dimensions['A'].width = 5
    sheet.column_dimensions['B'].width = 25
    sheet.column_dimensions['C'].width = 20
    sheet.column_dimensions['D'].width = 45
    wb.save('danmu.xlsx')
