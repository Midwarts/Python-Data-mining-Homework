class Media():
    count = 0  # 计数器

    def __init__(self, name, url):
        self.name = name
        self.url = url
        Media.count += 1

    # 实例化获取媒体名，返回媒体名
    def _name(self):
        return (self._name)
    # 获取媒体网址，返回媒体网址
    def _url(self):
        return (self._url)
    # 重写媒体类的__str__方法，另其返回媒体名
    def __str__(self):
        return ("媒体名为%s"% self._name)

def main():
    media = {"百度": "baidu.com", "360": "360.com", "google": "google.com"}
    for key in media.keys():
        result = (Media(key, media[key]))
        print(result._name())
        print(result._url())
        print(result.__str__())
    print("一共实例化了%d个媒体 "% Media.count)

if __name__ == '__main__':
    main()