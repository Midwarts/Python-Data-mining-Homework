import math


class circle():

    def __init__(self, r):
        self._r = r              #把r属性绑定到self上，因为self就指向创建的实例本身

    def square(self):
        S = round(math.pi * self._r * self._r,2)
        print('该圆的面积为%.2f' %S)

    def circumference(self):
        C = round(2 * math.pi * self._r,2)
        print('该圆的周长为%.2f' %C)

def main():
    banjing = float(input("请输入你的半径："))
    X=circle(banjing)
    X.circumference()
    X.square()

if __name__ == "__main__":
    main()