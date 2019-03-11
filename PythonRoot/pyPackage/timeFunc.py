# -*- coding:utf-8 -*-
import time,threading

# timestamp
print('clock()', time.clock())
print('time()', time.time())

print('clock2()', time.clock())
print('mktime()', time.mktime(time.localtime()))
# struct_time
print('localtime()',time.localtime())
print('gptime()',time.gmtime())
print('strptime()', time.strptime("2019-3-4","%Y-%m-%d"))
# str time
print('strftime()',time.strftime("%Y-%m-%d %X %Z").encode(encoding= 'utf-8'))
print("asctime()", time.asctime(time.localtime()))
print("ctime()", time.ctime(time.time()))

