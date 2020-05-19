import urllib.request
import ssl,sys

# 1. 完成一次网络请求
resp = urllib.request.urlopen('http://www.baidu.com')
print(resp.read())

# 2. 高德寻址API的调用

# 接入该api并读取
ip_url='https://restapi.amap.com/v3/ip?key=31a1a59a98d0bd6fd4a79bb56bc092a4'
ip_data=urllib.request.urlopen(ip_url).read()

# 解码
ip_data=ip_data.decode('utf-8')

# 转成字典
ip_final=eval(ip_data)
S = [[round(float(y[0]), 3), round(float(y[1]), 3)]
     for y in (x.split(",") for x in ip_final['rectangle'].split(";"))]

# 写出当前ip所在的位置信息
print('----------位置信息----------')
print('省份名称：',ip_final['province'])
print('城市名称：',ip_final['city'])
print('矩形区域范围：',S)
print('-----------结束-------------')
