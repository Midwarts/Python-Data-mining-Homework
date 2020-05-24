import json
str = ""
with open('C:/Users/86130/Desktop/萝莉酱直播间时间切片弹幕.json', 'r',encoding='utf-8') as f:
    data = f.read()
    json_data = json.loads(data)
    for i in json_data["data"]:
        if i[0] == "NM":
            str += "\n" + i[3]
    fo = open('result.txt', 'w', encoding='utf-8')
    fo.write(str)
    fo.close()
    print('操作完成!')