#author:zhouyueting
#name:json转exel
from openpyxl import Workbook
import json
import os
wb = Workbook()
sheet = wb['Sheet']
json_data = open("聆听丶芒果鱼直播间时间切片弹幕.json","rb")
info_data = json.load(json_data)
list_data = info_data["data"]
print(list_data)
sheet["A1"]="类别"
sheet["B1"]="发布时间"
sheet["C1"]="发布者"
sheet["D1"]="发布内容"
n = 1
for i in list_data:
    n += 1
    sheet["A%d" % n] = i[0]
    sheet["B%d" % n] = i[1]
    sheet["C%d" % n] = i[2]
    sheet["D%d" % n] = i[3]
wb.save("弹幕数据.exel")