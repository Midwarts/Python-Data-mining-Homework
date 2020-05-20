"""
目的：定义圆类解决实际问题
作者：徐昭
"""
import math
class Circle(object):

    def __init__(self,radius):#初始化，radius为圆的半径
        self.radius= radius

    def perimeter(self):
        """计算圆的周长"""
        return 2*math.pi*self.radius
    def area(self):
        """计算圆的面积"""
        return math.pi*self.radius*self.radius

def main():
    """解决问题"""
    radius = float(input("pls input your 'r' : "))
    circle = Circle(radius)
    print("The perimeter is ",format(circle.perimeter(),".2f"))
    print("The area is ",format(circle.area(),".2f"))

if __name__ == '__main__':
    main()


