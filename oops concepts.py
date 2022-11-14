#creating multiple threads
def m1():
    print('hii')
def m2():
    print('bye')
m1()
m2()
from threading import Thread
class MyThread(Thread):
    def run(self):
        print('this is our thread')
        print(self.getName)
class A(Thread):
    def run(self):
        print('this code is excuted by thread2...')
m1=MyThread()
m1.start()
m2=A()
m2.start()


