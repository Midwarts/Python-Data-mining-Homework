"""
目的：编写媒体类并解决实际问题
作者：徐昭
"""
count = 0  # 静态全局变量count，用于记录类被实例化的次数
Medium = []#储存实例化的对象

class Media:
    def __init__(self, name, address):
        self._name = name
        self._address = address
        global count
        count += 1
        """类被实例化的时候自动调用__init__()方法
        每调用一次计数count加一"""

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def __str__(self):
        """直接print类时，打印媒体的名称"""
        # print(name)
        return "媒体的名称是:%s" % self._name


def main():
    """解决问题"""
    name = input("请输入您存储的媒体名称，并以中文逗号分隔: ")
    name = name.split("，")  # 将字符串转化为列表
    address = input("请按以上顺序输入您存储的媒体地址，并以英文逗号分隔: ")
    address = address.split(",")
    for id in range(len(name)):
        temp_media = Media(name[id], address[id])
        Medium.append(temp_media)
        del temp_media

def show():
    for media in Medium:
        print("媒体名称:%s,地址:%s" % (media.get_name(), media.get_address()) )
        print(media)


if __name__ == '__main__':
    main()
    show()
    print("您一共创建了%d个对象" % count)