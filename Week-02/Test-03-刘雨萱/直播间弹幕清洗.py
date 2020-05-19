'''
直播间弹幕清洗
好多内容都是参考CSDN以及其他同学的作业，大家真的太强了！！！！
'''
import json
import re
PUNCTUATION_list= [
    " ", "　", ",", "，", ".", "。", "！", "？", "；", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]

# 合并文本中连续的相同的标点符号的函数.来自同学作业参考
def get_solo(text):
    duels = [x + x for x in list(PUNCTUATION_list)]
    for d in duels:
        while d in text:
            text = text.replace(d, d[0])
    return text

# 合并连续的相同的中文汉字1.这个方法总是输出“ expected string or bytes-like object”,不太清楚是哪里的问题，最终换了一种方法
# def get_CN(text):
#     def get_solo1(text):
#         text_chinese = re.findall("[\u4e00-\u9fa5]{4,}", text)
#         for d in text_chinese:
#             while d in text:
#                 text = text.replace(d, d[0] + d[1] + d[2])
#         return text

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

#合并连续的相同的英文字符
def get_EG(text):
    text_chinese = re.findall("[a-zA-Z]{4,}", text)
    for d in text_chinese:
        while d in text:
            text = text.replace(d, d[0] + d[1] + d[2])
    return text

#删去制表符和换行符(为保留格式，未清理换行符）
def get_NT(text):
    duels = [x for x in list("\t")]
    for d in duels:
        while d in text:
            text = text.replace(d, "")
    return text

# 将所有英文字符转换为小写形式.参考同学作业
def Aa(text):
    for i in range(len(text)):
        if ord(text[i])>64 and ord(text[i])<91:
            a=chr(ord(text[i])+32)
            text=text.replace(text[i],a)
    return text

# 将全角字符转化为半角字符
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


def main():
    try:
        with open('E:\python\Exercise-01-刘雨萱\Test-03-刘雨萱\萝莉酱直播间时间切片弹幕.json', "r",
                  encoding='utf-8') as f:
            data = f.read()
            json_data = json.loads(data)
            str = ""
            for i in json_data["data"]:
                if i[0] == "NM":
                    str += ("\n" + i[3])
            fo = open("E:\\python\\Exercise-01-刘雨萱\\Test-03-刘雨萱\\result", "w", encoding='utf-8')
            fo.write(str)
            fo.close()

        if __name__ == '__main__':
            with open("result", "r", encoding='utf-8') as f:
                text = f.read()
                text = get_solo(text)
                text = countChinese(text, 3, 3)
                text = get_EG(text)
                text = get_NT(text)
                text = str_2_byte_to_1_byte(text)
            with open("E:\\python\\Exercise-01-刘雨萱\\Test-03-刘雨萱\\final_result", "w", encoding='utf-8') as g:
                text_exchange = text.lower()
                g.write(text_exchange)
                g.close()
            print("操作完成")

    except IOError as e:
        print(e)


if __name__ == '__main__':
    main()

