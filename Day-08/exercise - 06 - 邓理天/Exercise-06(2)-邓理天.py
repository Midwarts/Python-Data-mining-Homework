'''
使用正则表达式判断字符串是否为邮箱地址
'''
if __name__ == "__main__":
    import re
    account = input('请输入邮箱：')  # 用户键入字符串
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+'  # 邮箱格式的正则表达式
    if re.match(pattern, account):  # match匹配，判断输出
        print("您输入的字符串是邮箱地址")
    else:
        print("您输入的字符串不是邮箱地址")
