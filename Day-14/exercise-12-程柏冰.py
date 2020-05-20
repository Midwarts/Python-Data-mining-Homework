class Media:
    count = 0

    def __init__(self,name,url):
        self.name = name
        self.url = url
        Media.count += 1

    def __str__(self):
        return "媒体名为:{}".format(self.name)

media1 = Media("百度","http://zhanzhang.baidu.com/sitesubmit/index")
print(media1)
media2 = Media("360","http://hao.360.cn/url.html")
print(media2)
media3 = Media("谷歌","http://www.sousuoyinqingtijiao.com/google/")
print(media3)
print("共实例化媒体：",Media.count)
