class Media(object):
    count = 0

    def __init__(self, name, site):
        self.name = name
        self.site = site
        Media.count += 1

    def name(self):
        return self.name

    def site(self):
        return self.site

    def __str__(self):
        return "In __str__:\n媒体名：{} ". \
            format(self.name)


def main():
    media1 = Media('南方周末', 'http://www.infzm.com/')
    media2 = Media('财新网', 'http://www.caixin.com/')
    media3 = Media('腾讯新闻', 'https://news.qq.com/')
#返回媒体名、媒体网址的方法
    print(media1.__dict__)
    print(media2.__dict__)
    print(media3.__dict__)
#统计一共实例化了多少个媒体
    print('实例化了%x个媒体'%(Media.count))
#重写媒体类的__str__方法，另其返回媒体名。
    print(media1)
    print(media2)
    print(media3)

if __name__ == '__main__':
    main()
