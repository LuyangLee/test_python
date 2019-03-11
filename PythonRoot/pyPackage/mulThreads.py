import threading
from queue import Queue
import time
import copy

lock = threading.Lock()
def norm(l):
    total = sum(l)
    print(total)

def multiCal(l, q, **keys):
    lock.acquire()
    thrResult = sum(l)
    q.put(thrResult)
    print('this thread {threadName} is {serialNum}'.format(threadName = threading.current_thread().name, serialNum = keys['serialNum']))
    lock.release()
    # print(keys)

# q = Queue()
# multiCal([123,1], q, serialNum = 1)
# way1: create thread subclass
class MyThread(threading.Thread):
    def __init__(self, target, args, kwargs):
        threading.Thread.__init__(self)
        self._target = target
        self._args = args
        self._kwargs = kwargs
    def run(self):
        print("这是第%d线程开始"%self._kwargs['serialNum'])
        self._target(*self._args, **self._kwargs)
        print("这是第%d线程结束"%self._kwargs['serialNum'])

def clasaMutiThr(l):
    q = Queue()
    threads = []
    total = 0
    for i in range(4):
        mt = MyThread(target = multiCal, args = (copy.copy(l), q), kwargs= {"serialNum":i})
        mt.start()
        threads.append(mt)
    for i in range(4):
        threads[i].join()
        total += q.get()
    print(total)


# way2: use threading function, create muti function need to be executed in mutiple threads
def multiThr(l):
    q = Queue()
    total = 0
    threads = []
    for i in range(4):
        t = threading.Thread(target= multiCal, args=(copy.copy(l), q),kwargs= {"serialNum": i}, name= 'fun_thread')
        t.start()
        threads.append(t)
    for i in threads:
        i.join()
    for _ in range(4):
        total += q.get()
    print(total)



def main():
        # s_t = time.time()
        # mutiThr([1, 2, 3, 4])
        # print("muti time is ", time.time() - s_t)
        calList = [1, 2, 3, 4, 5]
        multiThr(calList)


if __name__ == "__main__":
    main()