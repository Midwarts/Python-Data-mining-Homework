import json
import re
PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "!", "?","？", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]

danmu=""
# 合并文本中连续的相同的标点符号
def get_solo(text):
    duels = [x + x for x in PUNCTUATION_LIST]
    for d in duels:
        while d in text:
            text = text.replace(d, d[0])
    return text

# 合并文本中连续的相同的中文汉字

def get_solo_chinese(text):
    text_chinese = re.findall("[\u4e00-\u9fa5]{4,}", text)
    for d in text_chinese:
        while d in text:
            text = text.replace(d, d[0] + d[1] + d[2])
    return text

#合并文本中连续的相同的英文字母
def get_solo_alphabet(text):
    text_alphabet = re.findall("[a-zA-Z]{4,}", text)
    for d in text_alphabet:
        while d in text:
            text = text.replace(d, d[0] + d[1] + d[2])
    return text

# 剔除文本中的换行符(\n)和制表符(\t)
def str_replace(text):
    text = text.replace('\n', '').replace('\t','')
    return text

# 将所有英文字符转换为小写形式
def text_transform(text):
    text = text.lower()
    return text

# 将全角字符转换为半角字符
def str_2_byte_to_1_byte(text):
    result = ""
    for uchar in text:
        inside_code = ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif 65281 <= inside_code <= 65374:
            inside_code -= 65248
        result += chr(inside_code)
    return result

with open('C:\\Users\\cbb\\Desktop\\聆听丶芒果鱼直播间时间切片弹幕.json',encoding='utf8')as f:
    data = f.read()
    jsonFile = json.loads(data)
    for i in jsonFile["data"]:
        if i[0] == "NM":
            danmu += ("\n" + i[3])
            
file = open('C:\\Users\\cbb\\Desktop\\result.txt', 'w', encoding='UTF-8')
file.write(danmu)
file.close()

if __name__ == '__main__':
    danmu = get_solo(danmu)
    danmu = get_solo_chinese(danmu)
    danmu = get_solo_alphabet(danmu)
    danmu = str_replace(danmu)
    danmu = text_transform(danmu)
    danmu = str_2_byte_to_1_byte(danmu)

print("操作成功")
