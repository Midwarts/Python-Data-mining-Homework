import json
import re

PUNCTUATION_LIST = [ " ", "　", ",", "，", ".", "。", "!", "?", ";", "、", "~", "|", "·", ":", "+", "\-", "—", "*", "/", "／", "\\", "%",
    "=", "\"", "'", "（", "）", "(", ")", "\[", "\]", "【", "】", "{", "}", "《", "》", "→", "←", "↑", "↓", "↖", "↗", "↙",
    "↘", "$", "%", "_", "#", "@", "&", "√", "X", "♂", "♡", "♿", "⭐", "❤", "■", "⭕",
    "✂", "✈", "█", "ð", "▓", "ж", "⛽", "☞", "♥", "☯", "⚽", "☺", "㊙", "✨", "＊", "✌", "⚡", "⛷", "✊", "☔", "✌", "░"]
PUNCTUATION_STR="".join(PUNCTUATION_LIST)

def danmu_qingxi():
    list=[]                  #预先定义几个后期存储数据用的列表
    list_1=[]
    list_2=[]
    list_3=[]
    list_4=[]
    f=open(r'C:\Users\NealPayne\Desktop\聆听丶芒果鱼直播间时间切片弹幕.json','r',encoding='utf-8')            #打开文件
    file=json.load(f)      #转格式
    data=file['data']
    for i in data:
        if i[0]=='NM':                   #取出首项为"NM"的弹幕的第三项
            list.append(i[3])

         #合并大于三个的字母、数字
    for j in list:
        x=re.findall(r'([A-Za-z\u4e00-\u9fa5])\1{3,}',j)                     #用findall找到连续出现的字母 （返回的结果只有一个字母
        x_str="".join(x)                                                              #findall返回的对象是列表 转为字符串 方便*3
        y=x_str*3                                                                        #*3以便用来替换
        letter = re.sub(r'([A-Za-z\u4e00-\u9fa5])\1{3,}', y,j)            #用sub替换
        list_1.append(letter)

       #将全角字符转换为半角字符    直接用了师哥的函数（其实不确定有没有用
    for k in list_1:
        def str_2_byte_to_1_byte(k):
            result = ""
            for uchar in k:
                inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
                inside_code -= 65248
            result += chr(inside_code)
            return result

   #将所有英文字符转换为小写形式
    for l in list_1:
        lower=l.lower()
        list_2.append(lower)

     #剔除文本中的换行符(\n)和制表符(\t)
    for m in list_2:
        zhihang = m.replace('\n','')                  #剔除换行符
        zhibiao=zhihang.replace('\t','')           #剔除制表符
        list_3.append(zhibiao)

         #合并文本中连续的相同的标点符号(将大于等于2个连续的相同标点符号均替换为1个)   和替换中文字母原理一样
    for n in list_3:
        b=re.findall(r'([ ，.。！？;、~|·:+\-—*/／\%="（）()\[\]【】{}《》→←↑↓↖↗↙↘$%_@&√X♂♡♿⭐❤■⭕✂✈█ð▓ж⛽☞♥☯⚽☺㊙✨＊✌⚡⛷✊☔✌░//#])\1{1,}',n)               #！要转换成字符串 不能直接写表名
        b_str="".join(b)
        punctuation = re.sub(r'([ ，.。！？;、~|·:+\-—*/／\%="（）()\[\]【】{}《》→←↑↓↖↗↙↘$%_@&√X♂♡♿⭐❤■⭕✂✈█ð▓ж⛽☞♥☯⚽☺㊙✨＊✌⚡⛷✊☔✌░//#])\1{1,}', b_str, n)
        list_4.append(punctuation)



    z = open(r'C:\Users\NealPayne\Desktop\弹幕清洗.txt', 'w', encoding='utf-8')
    for a in list_4:
        z.write(a+'\n')
    print('操作完成！')



danmu_qingxi()





