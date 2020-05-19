'''
直播间弹幕数据清洗
实现要求
清洗当前文件夹下的“聆听丶芒果鱼直播间时间切片弹幕.json”，清洗要求如下：
将弹幕类型为(列表中的第1项)为“NM”的弹幕的弹幕内容(列表中的第4项)取出，存为一条弹幕一行的txt格式。
合并文本中连续的相同的标点符号(将大于等于2个连续的相同标点符号均替换为1个)
合并文本中连续的相同的中文汉字(将大于等于3个连续的中文汉字均替换为3个)
合并文本中连续的相同的英文字母(将大于等于3个连续的英文字母均替换为3个)
剔除文本中的换行符(\n)和制表符(\t)
将所有英文字符转换为小写形式
将全角字符转换为半角字符
'''
import json
import string
from markupsafe import unichr


def str_combine(strs):  # 合并标点、中文、英文，统一大小写，剔除换行符与制表符
    n = 0
    combine_str = ""
    strs = strs.replace('\t', '')  # 剔除制表符
    strs = strs.replace('\n', '').replace('\r', '')  # 剔除换行符
    while n < len(strs):  # 条件语句，开始遍历
        if strs[n] in string.punctuation:  # 判断是否为标点
            if strs[n] == strs[n - 1]:  # 判断是否连续出现2次以上
                n += 1
            else:
                combine_str=combine_str+strs[n]
                n += 1
        elif '\u4e00' <= strs[n] <= '\u9fa5':  # 判断是否为中文
            if n < 3:  #判断是否出现在第三位以后
                combine_str = combine_str + strs[n]
                n += 1
            else:
                if strs[n] == strs[n - 1] == strs[n - 2] == strs[n - 3]:  # 判断是否连续出现3次以上
                    n += 1
                else:
                    combine_str = combine_str + strs[n]
                    n += 1

        elif (strs[n] >= u'\u0041' and strs[n] <= u'\u005a') or (
                strs[n] >= u'\u0061' and strs[n] <= u'\u007a'):  # 判断是否为英文
            k = strs[n]
            strs=strs[:n]+k.lower()+strs[(n+1):] #全体大写改为小写
            if n < 3:#判断是否出现在第三位以后
                combine_str = combine_str + strs[n]
                n += 1
            else:
                if strs[n] == strs[n - 1] == strs[n - 2] == strs[n - 3]:  # 判断是否连续出现3次以上
                    n += 1
                else:
                    combine_str = combine_str + strs[n]
                    n += 1

        else:
            combine_str = combine_str + strs[n]
            n += 1


    return combine_str #返回结果


def strQ2B(ustring):  # 全角转半角
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += unichr(inside_code)
    return rstring


if __name__ == '__main__':
    with open(r'E:\作业\Python-Data-mining-Homework-master\Day-09\聆听丶芒果鱼直播间时间切片弹幕.json', encoding='utf-8',
              errors='ignore') as f:  # 打开json文件
        data = f.read()
        text = json.loads(data)  # 读取json文件
        result = []  # 新建序列用于储存
    for i in text['data']:  # 循环结构 遍历每一组数据
        if i[0] == 'NM':  # 条件语句 判断第一列是否为目标
            i[3] = str_combine(i[3])
            i[3] = strQ2B(i[3])
            result.append(i[3])  # 添加入序列
            result.append('\n')  # 换行
    with open(r'E:\作业\Python-Data-mining-Homework-master\Day-09\输出.txt', 'w', encoding='utf-8',
              errors='ignore') as f2:  # 打开存储文件
        f2.writelines(result)  # 存入数据
    f.close()
    f2.close()  # 关闭文件
