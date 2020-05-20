class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        per = 3.14 * 2 * self.radius
        return (per)

    def area(self):
        ar = 3.14 * self.radius * self.radius
        return (ar)


def main():
    r = float(input("请输入圆的半径:"))
    f = Circle(r)
    print('圆的面积为：%.2f' % float(f.area()))
    print('圆的周长为：%.2f' % float(f.perimeter()))


if __name__ == '__main__':
    main()
