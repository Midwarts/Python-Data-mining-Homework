'''
将当前文件夹下的“聆听丶芒果鱼直播间时间切片弹幕.json”转存为txt格式，转存要求如下：
将弹幕类型为(列表中的第1项)为“NM”的弹幕的弹幕内容(列表中的第4项)取出，存为一条弹幕一行的txt格式。
'''
if __name__ == '__main__':
    import json
    with open(r'E:\作业\Python-Data-mining-Homework-master\Day-09\聆听丶芒果鱼直播间时间切片弹幕.json', encoding='utf-8',
              errors='ignore') as f:  # 打开json文件
        data = f.read()
        text = json.loads(data)  # 读取json文件
        result = []  # 新建序列用于储存
    for i in text['data']:  # 循环结构 遍历每一组数据
        if i[0] == 'NM':  #条件语句 判断第一列是否为目标
            result.append(i[3])  #添加入序列
            result.append('\n')  #换行
    with open(r'E:\作业\Python-Data-mining-Homework-master\Day-09\输出.txt', 'w',encoding='utf-8',
              errors='ignore') as f2:  #打开存储文件
        f2.writelines(result)  #存入数据
    f.close()
    f2.close()  #关闭文件
