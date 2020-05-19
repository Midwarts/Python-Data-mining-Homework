from threading import Thread,Lock
from time import time,sleep

L = Lock()

def count(self):
	num = 1
	while num < 11:
		L.acquire()#获取锁
		print("%s:%d"%(self,num))
		L.release()#释放锁
		num += 1
		sleep(0.5)

def main():
	t1 = Thread(target=count,args=("self1",))
	t1.start()
	t2 = Thread(target=count,args=("self2",))
	t2.start()
	t3 = Thread(target=count,args=("self3",))
	t3.start()
	t4 = Thread(target=count,args=("self4",))
	t4.start()
	t5 = Thread(target=count,args=("self5",))
	t5.start()

if __name__ == "__main__":
	main()