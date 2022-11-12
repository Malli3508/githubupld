# finally block
'''
# finaly block
1.finallyblock is a predefined keyword ofif python.
2.in genral we use finally block with try except block.
3.one try can have maximum only one finally.
4.finally block should be after all except if not block.
5.finally block code will be executes all the time,no matter whether.
'''
try:
    f=open('d:/palleypython.text','r')
    mylist=f.readlines()
    print(mylist[0])#printing first line
    f.close()
except FileNotFoundError:
    print('file does not exist.ply try later')
except IndexError:
    print('invalid postion..')
finally:
    print('ths is finally block...')

