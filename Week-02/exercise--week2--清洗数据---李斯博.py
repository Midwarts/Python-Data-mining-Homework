import json
import re

PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]

def Merges(text):      #合并文本中连续的相同的标点符号
    Punctuation = [x+x for x in PUNCTUATION_LIST]
    for i in Punctuation:
        while i in text:
            text = text.replace(i,i[0])
    return text

def get_solo_chinese(text):     #合并文本中连续的相同的中文汉字
    text_chinese = re.findall("[\u4e00-\u9fa5]{4,}", text)
    for i in text_chinese:
        while i in text:
            text = text.replace(i, i[0] + i[1] + i[2])
    return text

def get_solo_alphabet(text):      #合并文本中连续的相同的英文字母
    word_list = list(map(chr,range(ord("a"),ord("z")+1)))
    text_alphabet = re.findall("[a-zA-Z]{4,}", text)
    for i in text_alphabet:
        while i in text:
            text = text.replace(i, i[0] + i[1] + i[2])
    return text


def str_replace_n(text):    #剔除文本中的换行符(\n)
        text = text.replace('\\n', '')
        return text

def str_replace_t(text):    #剔除文本中的制表符(\t)
        text = text.replace('\\t', '')
        return text


def change_form(text):      # 将所有英文字符转换为小写形式
    text = text.lower()
    return text

def half(text):     #将全角字符转换为半角字符
    def str_2_byte_to_1_byte(text):
        result = ""
        for uchar in text:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
                inside_code -= 65248
            result += chr(inside_code)
        return result

with open(r'D:\360MoveData\Users\23612\Desktop\聆听丶芒果鱼直播间时间切片弹幕.json', encoding='utf-8') as f:
    data = f.read()
    json_data = json.loads(data)
    str = ""
    for i in json_data["data"]:
        if i[0] == "NM":
            str += ("\n" + i[3])
with open(r'D:\360MoveData\Users\23612\Desktop\聆听丶芒果鱼直播间时间切片弹幕.json', 'w', encoding="utf-8") as fo:
    fo.write(str)
    fo.close()

with open(r'D:\360MoveData\Users\23612\Desktop\聆听丶芒果鱼直播间时间切片弹幕.json', 'r', encoding='UTF-8') as f:
   exchange=f.read()
   exchange1 = Merges()
   exchange2 = get_solo_chinese(exchange1)
   exchange3 = get_solo_alphabet(exchange2)
   exchange4 = str_replace_n(exchange3)
   exchange5 = str_replace_t(exchange4)
   exchange6 = change_form(exchange5)
   exchange7 = half(exchange6)
print(exchange7)
with open("result.txt", "w",encoding="utf-8") as fs:
    fs.write(exchange7)
