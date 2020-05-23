import requests

#调用返回自己IP信息的API
URL = 'http://whois.pconline.com.cn/ipJson.jsp'
try:
    r = requests.get(URL)
except requests.RequestException as e:
    print(e)
else:
    print(r.status_code)    #检测响应状态码

