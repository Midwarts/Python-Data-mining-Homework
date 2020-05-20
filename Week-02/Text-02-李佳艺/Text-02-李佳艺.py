import json
import re

PUNCTUATION_LIST = [
    " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]


def full_to_half(string):
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


def cleaning(source, del_space=False, del_t=True, del_r=True, del_n=True, half=True, upper=False,
             lower=False, merge_3_chinese=False, merge_3_english=False, merge_3_punctuation=False):

    if del_space:
        source = source.replace(" ", "").replace("　", "")
    if del_t:
        source = source.replace("\t", "")
    if del_r:
        source = source.replace("\r", "")
    if del_n:
        source = source.replace("\n", "")
    if half:
        source = full_to_half(source)
    if upper:
        source = source.upper()
    if lower:
        source = source.lower()
    if merge_3_chinese:
        for chinese_character in re.findall("([\u4e00-\u9fa5])\1{3,}", source):
            source = re.sub("[" + chinese_character + "]{3,}", chinese_character * 3, source)
    if merge_3_english:
        for english_character in re.findall("([A-Za-z])\1{3,}", source):
            source = re.sub("[" + english_character + "]{3,}", english_character * 3, source)
    if merge_3_punctuation:
        punctuation_list = "".join(PUNCTUATION_LIST)
        for match_punctuation in re.findall("([" + punctuation_list + "])\1{2,}", source):
            source = re.sub("[" + match_punctuation + "]{2,}", match_punctuation * 3, source)
        source = re.sub("-{2,}", "---", source)
    return source


if __name__ == '__main__':
    with open("F:\\实验室\\jupyter\\聆听丶芒果鱼直播间时间切片弹幕.json", encoding="UTF-8")as file:
        danmu_json = json.loads(file.read())

        danmu_list = list()

        for danmu in danmu_json["data"]:
            if danmu[0] == "NM":
                danmu_list.append(
                    cleaning(danmu[3], lower=True, merge_3_chinese=True, merge_3_english=True, merge_3_punctuation=True)
                )
    with open("结果.txt", "w+", encoding="UTF-8") as file:
        file.write("\n".join(danmu_list))