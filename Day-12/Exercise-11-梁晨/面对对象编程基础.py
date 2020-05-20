class Circle(object):
    #创建一个圆的类
    def __init__(self,radius=0,pi=3.14):
       #初始化方法    :radius:半径  pi:圆周率
        self.radius = radius
        self.pi = pi

    def perimeter(self):
        """圆的周长函数"""
        c = 2*self.radius*self.pi
        print(c)
        
    def square(self):
        """圆的面积函数"""
        s=self.pi*(self.radius**2)
        print(s)

def main():
    circle1 = Circle(1)
    circle1.perimeter()
    circle1.square()

if __name__ == "__main__":
    main()