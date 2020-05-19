'''
使用多线程实现5个线程分别报数（每个线程每隔0.5秒报一个数，从1报到10）
'''
import threading
import time


def run(n):#报数函数
    count = 1
    while count < 11:#持续报数
        print("进程", n, ":", count)
        time.sleep(0.5)#休息0.5秒
        count += 1


if __name__ == '__main__':
    test1 = threading.Thread(target=run, args=("test1",))
    test2 = threading.Thread(target=run, args=("test2",))
    test3 = threading.Thread(target=run, args=("test3",))
    test4 = threading.Thread(target=run, args=("test4",))
    test5 = threading.Thread(target=run, args=("test5",))#定义五个进程
    test1.start()
    test2.start()
    test3.start()
    test4.start()
    test5.start()#开始报数
