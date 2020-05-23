
import requests
import re
import json

r = requests.get('http://whois.pconline.com.cn/ipJson.jsp')

text = re.findall("{[^{}]+\}", r.text)[0] #提取网站信息

data = json.loads(text)  #转换为python对象

for dict_key, dict_value in data.items():
    print(dict_key,': ',dict_value)

#以下是肖申克的救赎
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}

proxies = {
    "http": "http://123.207.96.189:80"
}

url = 'https://movie.douban.com/subject/1292052/'  # 网址

response = requests.get(url, proxies = proxies,headers=headers)
text = response.text
print(text)