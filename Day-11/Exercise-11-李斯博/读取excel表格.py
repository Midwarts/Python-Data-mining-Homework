import json
def read(file):
    with open(file, 'r', encoding='utf8') as f:  # 将json文件转化为字典
        data1 = json.load(f)
        data = data1["data"]
    return data

def write():
    a = read('json')
    print(a)
    title = ["类别", "发布时间", "发布者", "弹幕内容"]
    book = xlwt.Workbook()  # 创建excel对象
    sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)# 添加一个sheet页
    for i in range(len(title)):# 循环列
        sheet.write(0, i, title[i])# 将title数组中的字段写入到0行i列中
    for line in a:#　循环字典
        print('line:', line)
        sheet.write(int(line), 0, line) #　将line写入到第int(line)行，第0列中
        for i in range(len(a[line])):
            sheet.write(int(line), i + 1, a[line][i])
    book.save('聆听丶芒果鱼直播间时间切片弹幕.xls')

if __name__ == '__main__':
    write(r'D:\360MoveData\Users\23612\Desktop\聆听丶芒果鱼直播间时间切片弹幕.json')
