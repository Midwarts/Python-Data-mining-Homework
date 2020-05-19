'''
使用正则表达式提取网页源代码中的所有Url
'''
import re
code = input("请输入网页源代码:") # 用户键入字符串
url = r'https?://(?:[-\w.]|(?:%[\da-zA-Z]))+' # url的正则表达式(师哥我这一串是借鉴网上的但也还没完全搞明白。。。
print(re.findall(url,code))#输出
