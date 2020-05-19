import json
import re
import string

# 读入json文件
with open(r"E:\大学\项目\华榜\培训\Python-Data-mining-Tutorial\Week-02\萝莉酱直播间时间切片弹幕.json", "rb") as file:
    content = json.load(file)
print("文件成功读入！")

# 找到符合要求的弹幕并存入列表
result = [str(x[3]) + "\n" for x in content["data"] if (x[0] == "NM")]
print("Biu——符合要求的字符加载成功！")
# 初始化
print("~~~~~~~~~~~~~~~~~~~~~~~~~开启清洗~~~~~~~~~~~~~~~~~~~~~~~~~")

# 剔除文本中的换行符(\n)和制表符(\t)
print("1. 剔除换行符和制表符w")
for i in result:
    i = re.sub('[\n\t]', '', i)

# 将所有英文字符转换为小写形式
print("2. 英文字母全部换成小写w")
for r in result:
    r = r.lower()

# 将全角字符转换为半角字符
print("3. 全角字符换成半角w")
for e in result:
    for uchar in e:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        uchar = chr(inside_code)

# 合并文本中连续的标点符号(将大于等于2个连续的相同标点符号均替换为1个)
# 这样的样例可以跑起来
'''for i in [",",".","!"]：
    location = str(re.sub(r"["+i+r"]{2,}",i,"123,123sdf138,,,49,,,,,,32?!!!?") for i in [",",".","!"]
    print(location)'''
# 但是放入标点符号列表后持续报错
# 我实在是找不到哪儿错了QAQQQQ
print("4. 合并连续的标点符号")
for s in result:
    Punctuation = [
    " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"
]
    punctuation = "".join(Punctuation)
    for l in re.findall("([" + punctuation +"]) \\1{2,}",s):
        s = re.sub("["+l+"]{2,}",l,s)
    s = re.sub("-{2,}","-",s)


# 合并中英文
print("5. 合并连续的标点符号")


class samples:

    def short(self, source: str):
        # 至少3个字符才需要缩减，因此如果输入字符串长度不到3，就直接返回
        if len(source) < 3:
            return source
        # 否则，维护一个头指针和一个尾指针，将当前数据段缓存到buffer里
        front, rear = 0, 0
        out, buffer = "", ""
        source = source + "\n"
        for i in range(0, len(source)):
            if source[rear] == source[front]:
                buffer += source[front]
            else:
                rear = front
                if len(buffer) >= 3:
                    out += buffer[0]
                else:
                    out += buffer
                buffer = source[front]
            front += 1
        return out


S = samples()
for u in result:
    u = S.short(u)

print("1555551数据终于洗完啦！")

# 写入txt
with open(r"E:\大学\项目\华榜\培训\Exercise\Nanding.txt", "w") as file:
    file.writelines(result)

print("清洗干净的txt文件已生成~请查收哟~")
print("------------------------End---------------------")