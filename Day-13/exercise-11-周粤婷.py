class Circle(object):
    '''一个圆类'''

    def __init__(self, r):
        self.r=r
    def area(self):
        s = 3.14*self.r*self.r
        return s
    def perimeter(self):
        c = 2*3.14*self.r
        return c
def main():
    r1 = Circle(int(input("请输入圆的半径：")))
    print("该圆的面积为：%s" % r1.area())
    print("该圆的周长为：%s" % r1.perimeter())

if __name__ == '__main__':
    main()
