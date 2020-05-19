"""
作者：puess
"""

import threading
from time import time, sleep

def count():
    count=1
    for counter in range(1, 11):
        print(counter)
        sleep(0.2)
        counter += 1


def main():
    start = time()
    threads = []
    for i in range(5):
       k = threading.Thread(target=count, args=())
    threads.append(k)

    for i in threads:
        i.start()
        i.join()
    print('报数结束')

    end = time()
    print('报数耗费%d秒' % (end - start))

if __name__ == '__main__':
    main()