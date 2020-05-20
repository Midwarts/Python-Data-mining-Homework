import math

class Circle:

    def __init__(self, radius):
        self.r = radius

#圆的面积
    def area(self):
        S = float(math.pi * self.r * self.r)
        print('圆的面积为%d' %S)

#圆的周长
    def perimeter(self):
        C = float(2 * math.pi * self.r)
        print('圆的周长为%d' %C)

def main():
    radius = float(input("请输入你的半径："))
    circle = Circle(radius)
    circle.area()
    circle.perimeter()

if __name__ == "__main__":
    main()
