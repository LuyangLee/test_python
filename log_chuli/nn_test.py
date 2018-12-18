import tensorflow as tf
from numpy.random import RandomState
import random

x_input = tf.placeholder(tf.float32, name = "x_input")
y_input = tf.placeholder(tf.float32, name = 'y_input')

w1 = tf.Variable(tf.random_normal([2, 3],stddev= 1, seed= 1))
w2 = tf.Variable(tf.random_normal([3, 1],stddev= 1, seed= 1))

batch_size = 8
# 构建神经网络
a = tf.matmul(x_input, w1)
y = tf.matmul(a, w2)

#定义损失函数和优化
y = tf.sigmoid(y)
entropy = -tf.reduce_mean( y_input * tf.log(tf.clip_by_value(y, 1e-10, 1.0))  
                            + ( 1-y)*tf.log(tf.clip_by_value(1-y, 1e-10, 1.0))
                          )
train_step = tf.train.AdamOptimizer(0.0001).minimize(entropy)

#新建数据集
rdm = RandomState(seed = 1)
data_size = 128
X = rdm.rand(data_size, 2)
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

#tf的初始化
with tf.Session() as sess:
    initial = tf.global_variables_initializer()
    sess.run(initial)
    print(sess.run(w1))
    print(sess.run(w2))
    STEPS = 5000
    for i in range(STEPS):
        start = (i * batch_size) % data_size
        end = min(start + batch_size, batch_size)

        sess.run(train_step, feed_dict={x_input: X[start:end], y_input:Y[start:end]})

        if i % 1000 == 0:
            run_options = tf.RunOptions(trace_level = tf.RunOptions.FULL_TRACE)
            run_metadata = tf.RunMetadata()
            total_entropy = sess.run(entropy, feed_dict = {x_input:X, y_input:Y}, options = run_options, run_metadata = run_metadata)
            train_writer.add_run_metadata(run_metadata,i)
            print(i,total_entropy)
