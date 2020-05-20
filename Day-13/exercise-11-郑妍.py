from math import pi
class Circle(object):

    def __init__(self, r):
        self.r = r

    def gets(self):
        s = pi*self.r**2
        print('此半径下的面积是',s)


    def getc(self):
        c = 2*pi*self.r
        print('此半径下的周长是',c)

def main():
    r1 = Circle(float(input('请输入半径：')))
    r1.gets()
    r1.getc()

if __name__ == '__main__':
    main()
