import time
class Media:
    count=0
    def __init__(self,name,address):
        self.name=name
        self.address=address
        Media.count+=1
    def _str_(self):
        print("媒体名是:%s , 媒体网址是:%s" % (self.name, self.address))
class media(Media):
    def _str_(self):
        print("媒体名是:%s" % (self.name))
def main():
    a1 = Media("a", "A")
    b1 = Media("b", "B")
    c1 = Media("c", "C")
    print(Media.count)
    a1._str_()
    b1._str_()
    c1._str_()
    time.sleep(1)
    print("重写后结果：")
    a1 = media("a", "A")
    b1 = media("b", "B")
    c1 = media("c", "C")
    a1._str_()
    b1._str_()
    c1._str_()


if __name__ == '__main__':
    main()

