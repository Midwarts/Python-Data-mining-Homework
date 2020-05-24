#调用返回自己IP信息的API，其Url如下：http://whois.pconline.com.cn/ipJson.jsp
import requests
r = requests.get('http://whois.pconline.com.cn/ipJson.jsp')
print(r.text)
#请求豆瓣电影中《肖申克的救赎》页面，并在控制台输出请求结果，其Url如下：:https://movie.douban.com/subject/1292052/
import requests
url='https://movie.douban.com/subject/1292052/'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}#防止反爬
response=requests.get(url,headers=headers).text
print(response)