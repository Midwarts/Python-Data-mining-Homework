if __name__ == '__main__':

import re
tel = 'isoiqjxsjwljq138309jnkjn07025ishxnkwlnXKS18832745678SJXOIXNSXAL13529535005SHJXKXNA'
x = re.findall(r'1\d{10}',tel)
print(x)

#这是电话号码

import re
emall = input('请输入要测试的代码')
if re.match(r'^[0-9a-zA-Z]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',emall):
    print('是邮箱地址')
else:
    print('不是邮箱地址')
#这是电子邮箱

import re
inter = 'https://www.youku.com/'
z = re.findall(r'[a-zA-Z]+://[^\s]*[.com|.cn]', inter)
if re.findall(r'[a-zA-Z]+://[^\s]*[.com|.cn]', inter):
    print(z)
else:
    print('找不到URL')

#这是url





