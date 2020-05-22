count = 0
class Media(object):

    def __init__(self, name, address):
        self._name = name
        self._address = address
        global count
        count += 1
    # 包含一个计数器的属性，可以统计一共实例化了多少个媒体#

    def result(self):
        print('名称：', self._name)
        print('网址：', self._address)

class Str(Media):
    def __init__(self, name, address, str):
        super().__init__(name, address)
        self._str = str

    def str(self):
        return "媒体的名称是:%s" % self._name
    # 重写媒体类的__str__方法，另其返回媒体名#

def main():
    media = {"有道": "http://fanyi.youdao.com/", "新京报": "http://www.bjnews.com.cn/graphic/",
             "国家统计局": "http://www.stats.gov.cn/"}
    for key in media.keys():
        x = Media(key, media[key])
        x.result()
    print("一共实例化了%d个媒体" % count)

    for key in media.keys():
        name = Str(key, media[key], key)
        name.str()

if __name__ == '__main__':
    main()
