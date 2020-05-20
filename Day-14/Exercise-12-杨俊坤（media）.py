''''
编写一个媒体类Media，要求如下： ①包含一个计数器的属性，可以统计一共实例化了多少个媒体； ②实例化时获取媒体名、媒体网址，并包含可以返回媒体名、媒体网址的方法； ③重写媒体类的__str__方法，另其返回媒体名。
'''
class Media():
    count=0                #计数器
    def __init__(self,name,website):           #激活 实例化
        self.name=name
        self.website=website
        Media.count+=1
    def get_name(self):                #返回媒体名
        return self.name
    def get_website(self):              #返回媒体网址
        return self.website
    def __str__(self):
        return "名字是:%s " % (self.name)                 #这里用return就可以改写了
def main():               #下面都是调用
        media=Media(2,3)           #括号内是可自定义对象
        print(media.get_name())
        print(media.get_website())
        print(media)
        print('共实例了',Media.count,'个媒体对象')
if __name__ == '__main__':
    main()
