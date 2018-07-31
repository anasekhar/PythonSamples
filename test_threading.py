

import threading
import time

def worker(num):

    print("woker {}".format(num))


def myservice():
    print(threading.currentThread().getName(),'starting')
    time.sleep(3)
    print(threading.currentThread().getName(),'ending')

thread = []

for i in range(4):
    t = threading.Thread(target=worker,args=(i,))
    t = threading.Thread(target=myservice)
    thread.append(t)
    t.start()


