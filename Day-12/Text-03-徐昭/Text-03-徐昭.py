"""
目的：按照要求清洗弹幕文件
作者：徐昭
"""
# -*- coding:utf-8 -*-
import re
import json

# 符号集
PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "", "", "",
    "", "$", "%", "_", "#", "@", "&", "√", "X", "", "♡", "", "", "", "■", "",
    "", "", "█", "ð", "▓", "ж", "", "☞", "", "", "", "", "", "", "＊", "", "", "", "", "", "", "░"
]
# 字母集
ALPHABET = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 90)]


# 修改连续字母和标点符号的写法
def match(List, text, n, x):  # 集合 文本 大于等于n个保留x个
    exi = {}
    cnt = 1
    pre = text[0]
    ans = pre
    for i in List:
        exi[i] = 1
    for i in range(1, len(text)):
        if exi.get(text[i]) and text[i] == pre:
            cnt = cnt + 1
        else:
            cnt = 1
        if n == x + 1 and cnt < n:
            ans = ans + text[i]
        if n == x and cnt <= n:
            ans = ans + text[i]
        pre = text[i]
    return ans


# 修改连续文字的写法
def matchChinese(text, n, x):  # 文本 大于等于n个保留x个
    cnt = 1
    pre = text[0]
    ans = pre
    for i in range(1, len(text)):
        if text[i] == pre:
            cnt = cnt + 1
        else:
            cnt = 1
        if n == x + 1 and cnt < n:
            ans = ans + text[i]
        if n == x and cnt <= n:
            ans = ans + text[i]
        pre = text[i]
    return ans


# 删除换行符和制表符
def find(text):
    ans = ""
    for i in text:
        if i != '\n' and i != '\t':
            ans += i
    return ans

# 全角符改为半角符
def zhuanhuan(string):
    """ 将全角字符转化为半角字符
    :param string: <str> 需要转化为半角的字符串
    :return: <str> 转化完成的字符串
    """
    result = ""
    for uchar in string:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        result += chr(inside_code)
    return result

# 弹幕json文件的路径
json_path = 'E:\\Python\\danmu.json'
gai = []  # 将修改过后的弹幕数据存储到这里
with open(json_path, 'r', encoding='utf-8', errors='ignore') as f:  # 我只需要读取json文件就好了
    danmu = json.load(f)  # 读取弹幕文件中的弹幕
    data = danmu["data"]
    for i in data:
        if i[0] == "NM":
            gai.append(i[3])
    # 主要问题的修改
    for i in gai:
        match(PUNCTUATION_LIST, i, 3, 1)
        match(ALPHABET, i, 3, 3)
        matchChinese(i, 3, 3)
        find(gai)
        i.lower()
        zhuanhuan(i)
# 最后存储工作
filename = 'E:\\Python\\gaixie.txt'
with open(filename, 'w', errors='ignore') as f2:  # 只需要可写
    for i in gai:
        f2.write(i)
        f2.write("\n")  # 一行存储一条弹幕

print("操作完成！")
