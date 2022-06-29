from multiprocessing import Process
import time

def f(name):
    print('hello', name)
    print('end sub process')

if __name__ == '__main__':
    print('start main process')
    time.sleep(1)
    print('start sub process')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    print('end main process')