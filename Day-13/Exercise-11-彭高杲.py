import math


class Circle():

    def __init__(self, r):
        self.r = r

    def mianji(self):
        S = round(math.pi * self.r * self.r, 3)
        print('该圆的面积为%d' %S)

    def zhouchang(self):
        C = round(2 * math.pi * self.r, 3)
        print('该圆的周长为%d' %C)

def main():
    banjing = float(input("请输入你的半径："))
    yuan = Circle(banjing)
    yuan.mianji()
    yuan.zhouchang()

if __name__ == "__main__":
    main()
