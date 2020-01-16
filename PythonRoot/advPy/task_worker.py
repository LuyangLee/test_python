# summary:  
#     use Queue to communicate with client
# Author:
#     sophialee
# Date:
#     2018-3-11
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
import os,queue,random,sys,time

BaseManager.register("get_task_queue")
BaseManager.register("get_result_queue")
work = BaseManager(address= ('127.0.0.1', 5000), authkey=b'abc')
try:
    work.connect()
except:
    print("连接失败")
    sys.exit()
print("连接成功")
task = work.get_task_queue()
result = work.get_result_queue()
print(task.empty())

while not task.empty():
    num = task.get(timeout = 1)
    sleeptime = random.randint(0,3)
    time.sleep(sleeptime)
    print("run task %d"%num)
    result.put((num, sleeptime))

if __name__ == '__main__':
    pass
