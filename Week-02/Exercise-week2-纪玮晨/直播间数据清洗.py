import json
import re

PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]

def single_mark(text):      #合并文本中连续的相同的标点符号(将大于等于2个连续的相同标点符号均替换为1个)
    mark_list = [x+x for x in PUNCTUATION_LIST]
    for i in mark_list:
        while i in text:
            text = text.replace(i,i[0])
    return text

def single_character(text):     #合并文本中连续的相同的中文汉字(将大于等于3个连续的中文汉字均替换为3个)
    character_list0 = re.findall('[\u4e00-\u9fa5]',text)#汉字的unicode编码
    character_list = []
    for i in character_list0:
        if i not in character_list:
            character_list.append(i)
    four_list = [x+x+x+x for x in character_list]
    for i in four_list:
        while i in text:
            text = text.replace(i,i[0:3])
    return text

def single_word(text):      #合并文本中连续的相同的英文字母(将大于等于3个连续的英文字母均替换为3个)
    new_text = text.lower()#这一步实现了全部小写
    word_list = list(map(chr,range(ord("a"),ord("z")+1)))
    four_word_list = [x+x+x+x for x in word_list]
    for i in four_word_list:
        while i in new_text:
            new_text = new_text.replace(i,i[0:3])
    return new_text

def del_sign(text):     #剔除文本中的换行符(\n)和制表符(\t)
    text = text.replace('\n','').replace('\t','')
    return text

def half(text):     #将全角字符转换为半角字符
    half_list = []
    for i in text:
        num = ord(i)
        if num == 0x3000:       #全角空格变成半角空格
            num = 32
        elif 0xFF01 <=num <= 0xFF5E:        #其余的全角字符转换
            num -= 0xFEE0
        num = chr(num)
        half_list.append(num)
    return '\n'.join(half_list)


with open(r"D:\huabang-study\Python-Data-mining-Homework\Week-02\聆听丶芒果鱼直播间时间切片弹幕.json", encoding='utf-8') as f:
    content = json.loads(f.read())
    list1 = content['data']
    list2 = []
    for i in list1:
        if i[0] == "NM":
            c = i[3]
            list2.append(c)
            line = str('\n'.join(list2))

s1 = single_mark(line)
s2 = single_character(s1)
s3 = single_word(s2)
s4 = del_sign(s3)
s5 = half(s4)

print(s5)

with open("result.txt", "w",encoding="utf-8") as fs:
    fs.write(s5)