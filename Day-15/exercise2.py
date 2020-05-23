import requests
#请求豆瓣电影中《肖申克的救赎》页面
url= 'https://movie.douban.com/subject/1292052/'
cookies= {'key':'value'}
headers = {"user-agent":"Mozilla/5.0 (Linux;X11)"}
r = requests.post(url, headers=headers,cookies=cookies).text
print (r)