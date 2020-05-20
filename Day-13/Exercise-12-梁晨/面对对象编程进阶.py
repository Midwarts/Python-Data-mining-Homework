class Media(object):
    #媒体类Media
    #实例化时获取媒体名、媒体网址，并包含可以返回媒体名、媒体网址的方法
    def __init__(self,name,html):
        self.name = name
        self.html = html



    def returnname(self):
        #返回媒体名
        print(self.name)


    def returnhtml(self):
        #返回媒体网址
        print(self.html)

    def __str__(self):
        #媒体类的__str__方法
        print('媒体名为%s' % self.name)




list = []
a = Media("腾讯","www.tengxun.com")
b = Media("优酷","www.youku.com")
c = Media("爱奇艺","www.aiqiyi.com")

list.append(a)
list.append(b)
list.append(c)


def countnum(list):
    print("总共实例化%d个媒体" % len(list))


#方法一
#换成a，b也是一样的
c.returnname()
c.returnhtml()
c.__str__()
print(countnum(list))

#方法二
#定义列表
medialist =[("a","b"),("c","d"),("e","f")]
for h in medialist:
    i = Media(h[0],h[1])
    i.returnhtml()
    i.returnname()





