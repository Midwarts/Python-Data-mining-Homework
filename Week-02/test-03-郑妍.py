import re
PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／",r"\\","%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]
def str_2_byte_to_1_byte(string):
    result = ""
    for uchar in string:
        inside_code = ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif 65281 <= inside_code <= 65374: 
            inside_code -= 65248
        result += chr(inside_code)
    return result


import json
with open("聆听丶芒果鱼直播间时间切片弹幕.json", "r", encoding='utf-8') as a:
    data = json.loads(a.read())
    list0 = data['data']
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    for word1 in list0:
        if word1[0] == "NM":
            c = word1[3]
            list1.append(c)
#将NM条件下的弹幕整合到list2完成

for word1 in list1:
    word2 = str_2_byte_to_1_byte(word1)
    list2.append(word2)
#全角换半角完成

            
for word2 in list2:
    for i in PUNCTUATION_LIST:
        pattern = r'['+i+r']{2,}'
        find = re.findall(pattern,word2)
        if len(find) != 0:
            list8.append(word2)
            sub1 = re.sub(pattern,i,word2)
            list3.append(sub1)
for i in list2:
    if i not in list8:
        list3.append(i)
#标点符号整理完成


for word3 in list3:
    pattern_character = r'([\u4E00-\u9FA5])\1{3,}'
    find_character = re.findall(pattern_character,word3)
    if len(find_character) > 0:
        for i in find_character:
            b = str('["'+i+'"]{3,}')
            c = re.sub(b,i*3,word3)
            list4.append(c)
            list3.remove(word3)
for word3 in list3:
    list4.append(word3)
#重复汉字整理完成
##这里有个问题……如果我在整理标点符号的时候用同样list.remove是无法得出正确的结果的……这是为什么？？

for word4 in list4:
    pattern_letter = r'([a-zA-Z])\1{3,}'
    find_letter = re.findall(pattern_letter,word4)
    if len(find_letter) > 0:
        for i in find_letter:
            b = str('["'+i+'"]{3,}')
            c = re.sub(b,i*3,word4)
            list5.append(c)
            list4.remove(word4)
for word4 in list4:
    list5.append(word4)
#重复字母整理完成


for word5 in list5:
    pattern_0 = r"[\n\t]"
    find_0 = re.findall(pattern_0,word5)
    if len(find_0) >0:
        c = re.sub(pattern_0,"",word5)
        list6.append(c)
        list5.remove(word5)
for word5 in list5:
    list6.append(word5)
#整理制表符、换行符完成


for word6 in list6:
    word7 = str.lower(word6)
    list7.append(word7)
#转换小写完成


strall = str('\n'.join(list7))
with open("test-03-郑妍.txt", 'w',encoding='utf-8') as b:
    b.write(strall)

