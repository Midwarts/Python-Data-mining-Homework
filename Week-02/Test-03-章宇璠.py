import json
PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "！", "？", "；", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]
ALPHABET = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 90)]
#合并文本中连续的相同的英文字母
def get_three(text):
    duels = [x + x + x for x in list(ALPHABET)]
    for t in text:
        while t in duels:
            text = text.replace(t, t[t])
    return text

# 合并文本中连续的相同的标点符号的函数
def get_solo(text):
    duels = [x + x for x in list(PUNCTUATION_LIST)]
    for d in duels:
        while d in text:
            text = text.replace(d, d[0])
    return text

# 合并文本中连续的相同的中文汉字
def countChinese(text, n, x):
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

# 剔除文本中的换行符(\n)和制表符(\t)
def find(text):
    ans = ""
    for i in text:
        if i != '\n' and i != '\t':
            ans += i
    return ans

# 将全角字符转化为半角字符
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

# 将所有英文字符转换为小写形式
def Aa(text):
    for i in range(len(text)):
        if ord(text[i])>64 and ord(text[i])<91:
            a=chr(ord(text[i])+32)
            text=text.replace(text[i],a)
    return text




def main():
    try:
        result = []
        with open('D:\\中国传媒大学\\大一下\\jupyter\\聆听丶芒果鱼直播间时间切片弹幕.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)
            get_solo(data)
        for i in range(len(data['data'])):
            if data['data'][i][0] == 'NM':
                result.append(get_solo(data[('data')][i][3]))
        for i in result:
            countChinese(i, 3, 3)

        a = open("D:\\中国传媒大学\\大一下\\jupyter\\out.txt", 'w+', encoding='UTF-8')
        for i in range(len(result)):
            print(Aa(str_2_byte_to_1_byte(find(get_three(result[i])))), file=a)
        a.close()
    except IOError as e:
        print(e)

    print('保存数据完成!')

if __name__ == '__main__':
    main()









