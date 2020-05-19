import json
import re

with open(r"D:\huabang-study\Python-Data-mining-Homework\Day-09\聆听丶芒果鱼直播间时间切片弹幕.json", encoding='utf-8') as f:
    content = json.loads(f.read())
    list1 = content['data']
    list2 = []
    for i in list1:
        if i[0] == "NM":
            c = i[3]
            list2.append(c)
            line = str('\n'.join(list2))
    print(line)
    
with open("result.txt", "w",encoding="utf-8") as fs:
	fs.write(line)