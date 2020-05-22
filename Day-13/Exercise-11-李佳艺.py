from math import pi

''' 定义一个圆类Circle，要求根据半径实例化，并包含可以返回圆的圆积、周长的方法'''

r = float(input("请输入圆的半径:"))


class Circle(object):
    def __init__(self, r):
        self.r = r

    def area(self):
        self.area = pi * r * r
        return self.area

    def perimeter(self):
        self.perimeter = 2 * pi * r
        return self.perimeter


def main():
    ra = Circle(r)
    print('圆的面积为：%.2f' % float(ra.area()))
    print('圆的周长为：%.2f' % float(ra.perimeter()))


if __name__ == '__main__':
    main()
