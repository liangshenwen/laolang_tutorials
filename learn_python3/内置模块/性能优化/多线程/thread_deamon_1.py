import time
import threading

def run():
    time.sleep(2)
    print('current thread name: ', threading.current_thread().name)
    time.sleep(2)
    print('current thread end： ', threading.current_thread().name)


if __name__ == '__main__':

    start_time = time.time()

    print('main thread:', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.daemon = True
        t.start()

    print('main thread end', threading.current_thread().name)
    print('total time', time.time()-start_time)