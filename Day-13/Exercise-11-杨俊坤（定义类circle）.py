import math
class Circle:                         #定义类Circle
    def __init__(self,radius):           #初始操作
        self.radius=radius
    def get_area(self):                  #求面积的方法
        self.area=round(self.radius*self.radius*math.pi,2)
        print('圆的面积是：',self.area)
    def get_perimeter(self):           #求周长的方法
        self.perimeter=round(self.radius*2*math.pi,2)
        print('圆的周长是：',self.perimeter)

def main():
    radius=float(input('请输入圆的半径：'))
    result=Circle(radius)                        #括号内是半径 可自定义实例化对象/？
    result.get_area()                   #使用方法
    result.get_perimeter()             #使用方法

if __name__ == '__main__':
    main()
