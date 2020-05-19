import json
import os
import re
#创建txt文件并打开
path = os.getcwd()
if os.path.exists("data.txt"):
    f = open("data.txt", "w+",encoding='utf-8')
else:
    if os.path.isdir(path) :
        f = open("data.txt","w+")
#取出弹幕内容，成单独的列表
json_data = open("聆听丶芒果鱼直播间时间切片弹幕.json","rb")
info_data = json.load(json_data)
list_data = info_data["data"]
list1 = []
for i in list_data:
    if i[0]=="NM":
        list1.append(i[3])
#来自参考资料
PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]
#提前定义一个可以筛选要求文字和英文的函数
charac=re.compile(u'[\u4e00-\u9fa5]+')
def func(_list):
    if _list[i] != _list[i + 1] and _list[i] != _list[i - 1]:
        return True
    if _list[i] == _list[i + 1] and _list[i] != _list[i - 1] and _list[i] != _list[i + 2] or _list[i] == _list[
        i - 1] and _list[i] != _list[i - 2] and _list[i] != _list[i + 1]:
        return True
    if _list[i] == _list[i + 1] == _list[i + 2] and _list[i] != _list[i+3] and _list[i] != _list[i - 1] or _list[i] == _list[i + 1] == _list[i - 1] and _list[i] != _list[i+2] and _list[i] != _list[i - 2] or _list[i] == _list[i - 1] == _list[i - 2] and _list[i] != _list[i+1] and _list[i] != _list[i - 3]:
        return True
    else:
        return False
#来自参考资料
def str_2_byte_to_1_byte(string):
    result = ""
    for uchar in string:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        result += chr(inside_code)
    return result
#将list1中的每一条弹幕内容拿出来筛选
for i in list1:
    #全半角转化
    str_2_byte_to_1_byte(i)
    str_orig = i
    list_orig = list(str_orig)
    list_punc =[]
    n = len(list_orig)
    for i in range(n-3):#如果是n-1，报错超出范围
        if list_orig[i] in PUNCTUATION_LIST:
            if list_orig[i] != list_orig[i+1]:
                list_punc.append(list_orig[i])
        if charac.search(list_orig[i]) or re.search(r'[a-zA-Z]+', list_orig[i]) :
            if func(list_orig):
                list_punc.append(list_orig[i])
            else:
                ind = int(list_orig.index(list_orig[i]))
                list_orig[ind]=""#只能用空替换，如果用remove会导致range范围不大对，虽然我也不懂为啥
        if list_orig[i] not in PUNCTUATION_LIST and charac.search(list_orig[i])==None and re.search(r'[a-zA-Z]+',list_orig[i])==None:
            list_punc.append(list_orig[i])
    list_punc.append(list_orig[-1])
    str_new = "".join(list_punc)
    str.replace("\n","",str_new)
    str.replace("\t","",str_new)
    str_new.upper()#大写转小写
    print (str_new)
    f.write(str_new+"\n")
f.seek(0)
f.close()
#头秃，感觉这个办法好复杂好复杂，但是是我唯一能想到的办法了