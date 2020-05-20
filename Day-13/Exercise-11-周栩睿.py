π=3.14
class Circle:
    def __init__(self, r=0):
        self.r = r
    def calculate_s(self):
        return π * (self.r ** 2)
    def calculate_c(self,):
        return π * self.r
def main():
    circle=Circle(3)
    s=circle.calculate_s()
    c=circle.calculate_c()
    print("圆的面积为：",circle.calculate_s(),"圆的周长为：",circle.calculate_c())
if __name__ == '__main__':
    main()