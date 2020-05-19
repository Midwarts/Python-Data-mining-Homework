import re

num = input("请输入字符串：")
result = re.findall(r"13\d{9}|14[5|7]\d{8}|15\d{9}|16\d{9}|17[3|6|7]\d{8}|18\d{9}|19\d{9}",num)#注意有些数字开头的号码第三位是有限制的
print(result)