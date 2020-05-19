import re
import urllib.request

web = input("请输入网址：")
response = urllib.request.urlopen(web)
html = response.read()
tag = re.findall(r'<a href="([a-zA-z]+://[^\s]*)"', str(html))
print(tag)