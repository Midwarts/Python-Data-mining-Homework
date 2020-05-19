import json
import re


#导入弹幕文件
with open(r"C:\Users\admin\Documents\GitHub\Python-Data-mining-Tutorial\Week-02\萝莉酱直播间时间切片弹幕.json", encoding='utf-8') as f:


    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    data = json.loads(f.read())
    list1 = data['data']
#筛选nm形式弹幕
    list2 = []
    for i in list1:
        if i[0] == "NM":
            c = i[3]
            list2.append(c)

#将全角字符转化为半角字符
def str_2_byte_to_1_byte(string):
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

list3=[]
for word2 in list2:
    word3 = str_2_byte_to_1_byte(word2)
    list3.append(word3)


#去重复标点符号
PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]

list4=[]
list5=[]
for word3 in list3:
    for i in PUNCTUATION_LIST:
        pattern = r'['+i+r']{2,}'
        find = re.findall(pattern,word3)
        if len(find) != 0:
            list4.append(word3)
            sub1 = re.sub(pattern,i,word3)
            list5.append(sub1)
for i in list3:
    if i not in list4:
        list5.append(i)


#去除重复中文与英文
list6=[]
for i in list5:
    pattern_wrongletter =re.compile(r'([\u4E00-\u9FA5])\1{3,}')  # ascii码
    find_letter = re.findall(pattern_wrongletter, i)
    if len(find_letter) > 0:
        for m in find_letter:
            wrongletter = str('["' + m + '"]{3,}')
            correctletter = re.sub(wrongletter, m * 3, i)
            list6.append(correctletter)
            list5.remove(i)
for i in list5:
    list6.append(i)

list7=[]
for i in list6:
    pattern_wrongletter=re.compile(r'([a-zA-Z])\1{3,}')
    find_letter= re.findall(pattern_wrongletter,i)
    if len(find_letter)>0:
        for h in find_letter:
            wrongletter = str('["' + h + '"]{3,}')
            correctletter=re.sub(wrongletter, h * 3, i)
            list7.append(correctletter)
            list6.remove(i)
for i in list6:
    list7.append(i)


#英文大写转小写
list8=[]
for i in list7:
    lowerletter=str.lower(i)
    list8.append(lowerletter)

#提出换行符和制表符
list9=[]
for i in list8:
    doublecode=r"[\n\t]"
    find_double=re.findall(doublecode,i)
    if len(find_double) > 0:
        blank = re.sub(doublecode, "", i)
        list9.append(blank)
        list8.remove(i)
for i in list8:
    list9.append(i)

#加入换行符
correct_barrage = str('\n'.join(list9))





with open("萝莉弹幕.txt", "w",encoding='utf-8') as f:
    f.write(correct_barrage)
