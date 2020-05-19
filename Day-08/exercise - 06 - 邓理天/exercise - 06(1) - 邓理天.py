'''
使用正则表达式提取字符串中包含的所有手机号码
'''
if __name__ == "__main__":
    import re  # 引用re模块
    str = input('请输入字符串：')  # 用户键入字符串
    phone = re.findall('1[3|5|8]\d{9}', str)  # 匹配手机号码，手机号码为11位数字，前两位为13/15/18
    print(phone)


