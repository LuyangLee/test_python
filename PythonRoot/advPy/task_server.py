# summary:
#     use queue to communicate with client
# Author:
#     sophialee
# Date:
#     2019-3-11

from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
import random,time, queue
# queue between different process
TASKNUM = 10
task_queue = queue.Queue(TASKNUM)
result_queue = queue.Queue(TASKNUM)

def get_task_queue():
    return task_queue

def get_result_queue():
    return result_queue

def communi():
    # 将队列绑定到manager中实现分布式计算
    BaseManager.register("get_task_queue",callable= get_task_queue)
    BaseManager.register("get_result_queue", callable= get_result_queue)
    # 绑定端口，并设置验证码
    sManager = BaseManager(address= ('127.0.0.1', 5000), authkey=b'abc')
    sManager.start()
    try:
        task = sManager.get_task_queue()
        result = sManager.get_result_queue()
        for i in range(TASKNUM):
            n = random.randint(0, 1000)
            task.put(n)
            print("this task is %d"%i)
        while not result.full():
            time.sleep(1)
        for i in range(result.qsize()):
            r = result.get()
            print("this {0} result is{1}".format(i, r))
    except:
        print("manager error")
    finally:
        sManager.shutdown()

if __name__ == "__main__":
    freeze_support()
    communi()

