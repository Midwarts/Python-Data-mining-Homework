import requests
url="https://v.qq.com/x/page/z0858j68r6a.html"
r = requests.get('https://v.qq.com/x/page/z0858j68r6a.html') # 向网站发送get请求
print(r.status_code) # 获取返回状态,输出状态码
print(r.text) # 打印解码后的返回数据
