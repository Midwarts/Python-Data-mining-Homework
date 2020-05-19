str=""
import json
import re
def get_solo(text):
    duels = [x + x for x in list(" ""　" ",""，"".""。""!""?"";""、""~""|""·"":""+""\-""—""*""/""／""\\""%"
    "=""\"""'""（""）""("")""\[""\]""【""】""{""}""《""》""→""←""↑""↓""↖""↗""↙""↘""$""%""_""#""@""&""√""X""♂""♡""♿""⭐""❤""■""⭕""✂""✈""█""ð""▓""ж""⛽""☞""♥""☯""⚽""☺""㊙""✨""＊""✌""⚡""⛷""✊" "☔""✌""░")]
    for d in duels:
        while d in text:
            text = text.replace(d, d[0])
    return text
def get_solo1(text):
    text_chinese = re.findall("[\u4e00-\u9fa5]\1{4,}", text)
    for d in text_chinese:
        while d in text:
            text = text.replace(d, d[0] + d[1] + d[2])
    return text
def get_solo2(text):
    text_chinese = re.findall("[a-zA-Z]\1{4,}", text)
    for d in text_chinese:
        while d in text:
            text = text.replace(d, d[0] + d[1] + d[2])
    return text
def get_solo3(text):
    duels = [x for x in list("\n""\t")]
    for d in duels:
        while d in text:
            text = text.replace(d, "")
    return text
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
with open('D:\python\zhouxuruixiaopengyou\Python-Data-mining-Tutorial\Week-02\萝莉酱直播间时间切片弹幕.json', "r",
          encoding='utf-8') as f:
    data = f.read()
    data = get_solo3(data)
    json_data = json.loads(data)
    for i in json_data["data"]:
        if i[0] == "NM":
            str += ("\n" + i[3])
    fo = open("D:\\python\\zhouxuruixiaopengyou\\text\\TEST03\\result.txt", "w", encoding='utf-8')
    fo.write(str)
    fo.close()
if __name__ == '__main__':
    with open("D:\\python\\zhouxuruixiaopengyou\\text\\TEST03\\result.txt", "r", encoding='utf-8') as f:
        text = f.read()
        text =get_solo(text)
        text = get_solo1(text)
        text = get_solo2(text)
        text = str_2_byte_to_1_byte(text)
    with open("D:\\python\\zhouxuruixiaopengyou\\text\\TEST03\\result——final.txt", "w", encoding='utf-8') as g:
        text = text.lower()
        g.write(text)
        g.close()
print("操作完成")













