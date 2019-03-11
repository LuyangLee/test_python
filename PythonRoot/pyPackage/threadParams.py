# Summary:
#     use thread.local to transit params
# Author:
#    sophialee
# Date:
#    2019-3-11
import time,os
import threading

local_school = threading.local()
def getInfo():
    print("wo can get Info from {process}, the value is {val}".format(process = threading.current_thread().name, val = local_school.student))

def stu_thread(name):
    local_school.student = name
    getInfo()

if __name__ == "__main__":
    t1 = threading.Thread(target= stu_thread, args=('Meiko',))
    t2 = threading.Thread(target= stu_thread, args=('Ming',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()