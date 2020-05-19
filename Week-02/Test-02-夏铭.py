import json

PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]

danmu = ''

with open('聆听丶芒果鱼直播间时间切片弹幕.json', 'r',
          encoding='UTF-8')as f:  # 需更改文件路径
    dict = json.load(f)
    for n in dict['data']:
        if n[0] == 'NM':
            danmu += n[3] + '\n'


# 全角改半角
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


# 合并文本中连续的相同的标点符号
def get_solo_biaodian(text):
    duels = [x + x for x in PUNCTUATION_LIST]
    for d in duels:
        while d in text:
            text = text.replace(d, d[0])
    return text


# 合并文本中连续的相同的中文汉字和英文字母
def get_easy(text):
    num = 0
    newtext = text[0]
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            num = num + 1
        else:
            num = 0
        if num < 3:
            newtext = newtext + text[i]
    return newtext


# 剔除文本中的换行符(\n)和制表符(\t)
def str_replace_n(text):
    text = text.replace('\\n', '')
    return text


def str_replace_t(text):
    text = text.replace('\\t', '')
    return text


# 将所有英文字符转换为小写形式
def change_form(text):
    text = text.lower()
    return text


if __name__ == '__main__':
    danmu = str_2_byte_to_1_byte(danmu)
    danmu = get_solo_biaodian(danmu)
    danmu = get_easy(danmu)
    danmu = str_replace_n(danmu)
    danmu = str_replace_t(danmu)
    danmu = change_form(danmu)
    print(danmu, '\n弹幕清洗完成')
    file = open('danmu.txt', 'w', encoding='UTF-8')  # 需更改文件路径
    file.write(danmu)
    file.close()
