from multiprocessing import Process,Queue
import subprocess
import os,time,random


def write(q):
    print("this Process is {process}".format(process = os.getpid()))
    for i in ['1', '2', '3']:
        print('Put %s to queue...' % i)
        q.put(i)
        # time.sleep(random.random())

def read(q):
    print("this Process is {process}".format(process = os.getpid()))
    while True:
        result = q.get(True)
        print('Get %s from queue.' % result)

def main():
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q,) )
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

if __name__ == "__main__":
    main() 