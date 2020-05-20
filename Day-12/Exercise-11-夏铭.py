from math import pi

class Circle(object):

    def __init__(self, r):
        self.r = r

    def calculate_c(self):
        c=2*pi*self.r
        print('圆的周长为：',c)

    def calculate_s(self):
        s=pi*self.r*self.r
        print('圆的面积为：',s)

def main():
    yuan1=Circle(3)
    yuan1.calculate_c()
    yuan1.calculate_s()

if __name__ == '__main__':
    main()

