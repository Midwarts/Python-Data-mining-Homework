'''
!/usr/bin/env python
-*- coding:utf-8 -*-
Author:liuyuxuan
定义一个圆类(Circle)，要求如下： ①根据半径实例化； ②包含可以返回圆的圆积的方法； ③包含可以返回圆的周长的方法。
'''
import math
class circle(object):
    def __init__(self,r):
        self.r=r #初始化方法
    def square(self):
        s=math.pi*self.r*self.r
        print("The square of your circle is %d"%s)#计算圆的面积
    def round(self):
        C=2*math.pi*self.r
        print("The round of your circle is %d"%C)#计算圆的周长

def main():
    Radiu=float(input("please input the Radiu of the circle:"))
    Circle=circle(Radiu)
    Circle.square()
    Circle.round()
if __name__ == '__main__':
    main()
