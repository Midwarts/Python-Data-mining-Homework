'''
!/usr/bin/env python
-*- coding:utf-8 -*-
Author:liuyuxuan
 编写一个媒体类Media
'''
class Media():
    count = 0  # 计数器

    def __init__(self, name, url):
        self.name = name
        self.url = url  # 初始化方法
        Media.count += 1  # 要使得计数器全局有效，就定义为类的属性

    # 实例化时获取媒体名、媒体网址，并包含可以返回媒体名、媒体网址的方法
    def catch(self):
        print("名称:", self.name)
        print("网址:", self.url)

    # 重写媒体类的__str__方法，另其返回媒体名
    def __str__(self):
        return ("媒体名为%s"%self.name)


prime = {"百度": "baidu.com", "360": "360.com", "google": "google.com"}
for key in prime.keys():
    result = Media(key, prime[key])
    result.catch()
    result.__str__()
print("一共实例化了%s个媒体"%Media.count)
