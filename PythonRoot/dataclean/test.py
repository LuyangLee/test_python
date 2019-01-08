import os
import numpy as np
import re
import time
# s_latency s_download 都是取得chunk的大小
client_rebuf = np.array([],dtype=np.float)
client_buffer = np.array([],dtype=np.float)
chunk_latency = np.array([],dtype = np.float)
chunk_download = np.array([],dtype = np.float)
chunk_size = np.array([],dtype = np.float)
split_str = '\s+'
n_lines = 0
sum_chunk_latency = 0.0
sum_chunk_download = 0.0
sum_chunk_size = 0.0
with open('./test2.txt', 'r') as f:
    for line in f:
        n_lines += 1
        if line[0] is 'r':
            # a = re.split(split_str, line)
            # if(n_lines % 50 ==0):
            #     s_latency = np.append(s_latency, sum_latency)
            #     sum_latency = 0.0
            # l_i = a.index('latency')
            # sum_latency += float(a[l_i + 1] )
            a = re.split(split_str, line)
            # print(n_lines)
            cr_i = a.index('client_rebuf')
            cb_i = a.index('client_buffer')
            dec_i = a.index('decision_flag')
            lat_i = a.index('latency')
            down_i = a.index('download_duration')
            size_i = a.index('frame_size')
            client_rebuf = np.append(client_rebuf, float(a[cr_i + 1]))
            client_buffer = np.append(client_buffer,float(a[cb_i + 1]))
            if a[dec_i + 1] is '0':
                sum_chunk_latency += float(a[lat_i + 1] )
                sum_chunk_download += float(a[down_i + 1] )
                sum_chunk_size += float(a[size_i + 1])
            elif a[dec_i + 1] is '1':
                chunk_latency = np.append(chunk_latency, sum_chunk_latency)
                chunk_download =np.append(chunk_download, sum_chunk_download)
                chunk_size = np.append(chunk_size,sum_chunk_size)
                sum_chunk_latency = 0.0
                sum_chunk_download =0.0
                sum_chunk_size = 0.0
# print 'end'
# print "client_rebuf " + np.max(client_rebuf)
# print "client_buffer" + np.max(client_buffer)
# print "max_latency" + np.max(s_latency)
# print "min" + np.min(s_latency)
# print "mean" + np.mean(s_latency)
# print "std" + np.std(s_latency)
print ('end')
print ("client_rebuf " + str(np.max(client_rebuf)))
print ("client_buffer " + str(np.max(client_buffer)))
print ("max_latency " + str(np.max(chunk_latency)))
print ("min " + str(np.min(chunk_latency)))
print ("mean " + str(np.mean(chunk_latency)))
print ("std " + str(np.std(chunk_latency)))

print ("mean " + str(np.mean(chunk_download)))
print ("mean " + str(np.mean(chunk_size)))
print ("throughout " + str(np.mean(chunk_size) / np.mean(chunk_download)))
np.savetxt('./client_rebuf.txt',client_rebuf)
np.savetxt('./client_buffer.txt',client_buffer)
np.savetxt('./chunk_latecy.txt', chunk_latency)
f.close()

