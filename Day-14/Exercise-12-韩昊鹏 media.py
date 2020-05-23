class Media():

    # 计数器
    num = 0

    def __init__(self, name, url):
        Media.num = Media.num + 1
        self.name = name
        self.url = url

    # 返回媒体名、媒体网址
    def out(self):
        print("媒体名：", self.name)
        print("媒体网址：", self.url)

    # 重写__str__
    def __str__(self):
        return print("该媒体的媒体名为:"+str(self.name))


Meiti = {"寿喜锅": "szd.perfect.awsl", "甜筒": "szd.perfect.awsl", "DQ暴风雪": "szd.perfect.awsl", "抹茶奶盖": "szd.perfect.awsl"}

for a in Meiti:      #默认循环的代入变量a是字典里的键
    m = (Media(a, Meiti[a]))
    m.out()
    m.__str__()

print("\n"+"共实例化了%d个媒体" % Media.num)