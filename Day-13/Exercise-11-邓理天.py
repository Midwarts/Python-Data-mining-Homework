'''
定义一个圆类(Circle)，要求如下： ①根据半径实例化； ②包含可以返回圆的圆积的方法； ③包含可以返回圆的周长的方法。
'''
import math
class circle(object):#定义圆类

    def __init__(self,r):
        self.r = r

    def perimeter(self):#计算周长的方法
        return 2*math.pi*self.r

    def area(self):#计算面积的方法
        return math.pi*self.r*self.r

def main():
    n = float(input('请输入圆的半径：'))
    circle1 = circle(n)
    a = circle1.area()#调用面积方法
    b = circle1.perimeter()#调用周长方法
    print('圆的周长是',b)
    print('圆的面积是',a)#输出面积和周长

if __name__ == '__main__':
    main()