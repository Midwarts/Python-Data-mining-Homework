'''
调用返回自己IP信息的API，其Url如下：http://whois.pconline.com.cn/ipJson.jsp
'''
import requests

response = requests.get('http://whois.pconline.com.cn/ipJson.jsp')#获取请求状态码 200为正常
if(response.status_code == 200):#获取相应内容
    print(response.text)#获取输出相应内容
else:
    print("请求失败!")

