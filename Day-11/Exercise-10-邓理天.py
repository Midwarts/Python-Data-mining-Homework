'''
将当前文件夹下的“聆听丶芒果鱼直播间时间切片弹幕.json”转存为Excel格式，转存要求如下：
将列表中的每一个元素(一条弹幕信息)转存为Excel中的一行，并在Excel中增加表头一行，各列的名称分别为“类别”、“发布时间”、“发布者”、“弹幕内容”。
'''
if __name__ == '__main__':
    import json
    import csv
    with open(r'E:\作业\Python-Data-mining-Homework-master\Day-09\聆听丶芒果鱼直播间时间切片弹幕.json', encoding='utf-8',
              errors='ignore') as f:  # 打开json文件
        data = f.read()
        json_data = json.loads(data)  # 读取json文件
    with open(r'E:\作业\Python-Data-mining-Homework-master\Day-11\out.csv','w', encoding='utf-8',
              errors='ignore',newline='') as f2: #打开CSV文件
        csv_writer = csv.writer(f2) #读取csv文件
        title = ["类别","发布时间","发布者","弹幕内容"]
        csv_writer.writerow(title)#添加表头
        for i in json_data['data']:
            csv_writer.writerow(i) #json数据转存入csv
    f.close()
    f2.close()
