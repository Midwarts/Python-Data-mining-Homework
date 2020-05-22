'''
编写一个媒体类Media，要求如下：
①包含一个计数器的属性，可以统计一共实例化了多少个媒体；
②实例化时获取媒体名、媒体网址，并包含可以返回媒体名、媒体网址的方法；
③重写媒体类的__str__方法，另其返回媒体名。
'''

class Media(object):#定义媒体类
    count = 0

    def __init__(self,name,address):
        self.name = name
        self.address = address
        Media.count += 1#计数+1

    def __str__(self):
        return "媒体名是：%s,媒体网址是：%s" % (self.name,self.address)#返回的方法


class one_media(Media):#子类
    def __init__(self,name,address):
        super().__init__(name,address)#继承

    def __str__(self):
        return "媒体名是：%s" % (self.name)#重写


def main():
    name = 'BBC'
    address = 'www.bbc.uk'
    print(Media(name,address).__str__())
    print(one_media(name,address).__str__())#输出

if __name__ == '__main__':
    main()