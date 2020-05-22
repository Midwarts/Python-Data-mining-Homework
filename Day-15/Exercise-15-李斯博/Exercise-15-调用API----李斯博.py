import requests

GET_API= "http://whois.pconline.com.cn/ipJson.jsp"
r = requests.get(GET_API) #调用返回IP信息的API
print(r.status_code) # 检查请求状态码
print(r.text)