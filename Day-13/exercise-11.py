import math
class Circle(object):
    # 建立类
    def __init__(self, radius, unit):#设置对象，半径，单位
        self.radius = radius#半径
        self.unit = unit#单位
        print(self.radius,self.unit)

    def Area(self):#面积
        area = self.radius**2*math.pi
        print('圆的面积是',area)

    def Perimeter(self):#周长
        perimeter = 2*math.pi*self.radius
        print('圆的周长是',perimeter)


def main():
    x = input('请输入圆的半径')
    y = input('请输入你想要的单位')
    R = Circle(int(x), str(y))#设置对象，开始实例化
    R.Area()#面积对象输出
    R.Perimeter()#周长对象输出

if __name__ == '__main__':
    main()










