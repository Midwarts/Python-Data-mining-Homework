import json
import re

PUNCTUATION_list = [
    " ", "　", ",", "，", ".", "。", "！", "？", "；", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]


def single(text):
    duels = [x + x for x in list(PUNCTUATION_list)]
    for a in duels:
        while a in text:
            text = text.replace(a, a[0])
    return text


def Chinese(text, n, x):
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


def English(text):
    text_chinese = re.findall("[a-zA-Z]{4,}", text)
    for d in text_chinese:
        while d in text:
            text = text.replace(d, d[0] + d[1] + d[2])
    return text


def nort(text):
    duels = [x for x in list("\t")]
    for d in duels:
        while d in text:
            text = text.replace(d, "")
    return text


def Aa(text):
    for i in range(len(text)):
        if ord(text[i]) > 64 and ord(text[i]) < 91:
            a = chr(ord(text[i]) + 32)
            text = text.replace(text[i], a)
    return text


def str_byte(text):
    result = ""
    for uchar in text:
        inside_code = ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif 65281 <= inside_code <= 65374:
            inside_code -= 65248
        result += chr(inside_code)
    return result


def run():
    try:
        with open(r'C:\Users\Surface\Desktop\聆听丶芒果鱼直播间时间切片弹幕.json', 'rb') as f:
            data = f.read()
            json_data = json.loads(data)
            str = ""
            for i in json_data["data"]:
                if i[0] == "NM":
                    str += ("\n" + i[3])
        with open(r'C:\Users\Surface\Desktop\弹幕.txt', 'w', encoding="utf-8") as fo:
            fo.write(str)
            fo.close()
    except IOError as e:
        print(e)


if __name__ == '__main__':
    run()
    with open(r'C:\Users\Surface\Desktop\弹幕.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
        text = single(text)
        text = Chinese(text, 3, 3)
        text = English(text)
        text = nort(text)
        text = str_byte(text)
    with open(r'C:\Users\Surface\Desktop\result.txt', "w", encoding='UTF-8') as fs:
        text_exchange = text.lower()
        fs.write(text_exchange)
        fs.close()
    print("Success!")
