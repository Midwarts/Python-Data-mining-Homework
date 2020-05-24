import math
class Circle():

    def __init__(self, r):
        self._r = r

    def square(self):
        square = int(math.pi * self._r * self._r)
        print('该圆的面积为%d' %square)

    def circumference(self):
        circumference = int(2 * math.pi * self._r)
        print('该圆的周长为%d' %circumference)

def main():
    radius = int(input("请输入半径："))
    circle = Circle(radius)
    circle.square()
    circle.circumference()

if __name__ == "__main__":
    main()