class media():
    count = 0  # 记录实例化次数
    def __init__(self, name, url):
        self.name = name
        self.url = url
        media.count += 1
    def output(self):# 获取名称和网址
        print('名称为：', self.name)
        print('网址为：', self.url)
    def __str__(self):# 重写媒体方法
        print('媒体名：', self.name)
web = {"百度": "www.baidu.com", "网易": "www.163.com"}
for b in web.keys():
    i = media(b, web[b])
    i.output()
    i.__str__()
print('共实例化了%s个媒体' % media.count)