from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np 

mnist = input_data.read_data_sets("./MINIST_DATA", one_hot= True)
PIX = 28 * 28
MODEL_SAVE_INTERVAL = 100
NN_MODEL = 'result\\nn_model_ep_500.ckpt'
SUMMARY_DIR = 'result'
# 数据输入流定义
x_data = tf.placeholder(dtype= tf.float32, shape= [None, PIX], name= 'input')
y_label = tf.placeholder(dtype= tf.float32, shape= [None, 10], name= 'output')

def compute_accuracy(v_xs, v_ys):
    global out
    y_pre = sess.run(out, feed_dict={x_data: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={x_data: v_xs, y_label: v_ys})
    return result

# 定义神经网络,权重，偏差，卷积函数,池化函数
def weights(shape):
    return (tf.Variable(tf.truncated_normal(shape= shape, stddev= 0.1)))

def bias(shape):
    return (tf.Variable(tf.constant(0.1, shape= shape)))

def conv2d(x, W):
    return tf.nn.conv2d(x, W, [1, 1, 1, 1], padding= 'SAME')

def max_pool(x):
    return tf.nn.max_pool(x, ksize= [1, 2, 2, 1], strides= [1, 2, 2, 1], padding= 'SAME')

# 搭建神经网络第一层
x_image = tf.reshape(x_data, [-1, 28, 28, 1])
# 卷积核filter
W_conv1 = weights([5,5,1,32])
# bias一定和weights输出一致
B_conv1 = bias([32])
C_conv1 = tf.nn.relu((conv2d(x_image, W_conv1) + B_conv1))
P_conv1 = max_pool(C_conv1)

# 搭建神经网络第二层
W_conv2 = weights([5, 5, 32, 64])
B_conv2 = bias([64])
C_conv2 = tf.nn.relu(conv2d(P_conv1 ,W_conv2) + B_conv2)
P_conv2 = max_pool(C_conv2)

# 搭建全连接层
P_flatten = tf.reshape(P_conv2, [-1, 7*7*64])
w_fc = weights([7*7*64, 1024])
b_fc = bias([1024])
f_fc = tf.nn.relu(tf.matmul(P_flatten, w_fc) + b_fc)

# 输出softmax层
w_fc2 = weights([1024, 10])
b_fc2 =bias([10])
out = tf.nn.softmax(tf.matmul(f_fc, w_fc2) + b_fc2)

# 自定义损失函数
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_label * tf.log(tf.clip_by_value(out, 1e-10, 1.0)), reduction_indices=[1]))
trian_step = tf.train.AdamOptimizer().minimize(cross_entropy)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    STEPS = 1000
    saver = tf.train.Saver()
    nn_model = NN_MODEL
    if nn_model is not None:
        saver.restore(sess, nn_model)
        print("model saved")
    for i in range(STEPS):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(trian_step, feed_dict = {x_data:batch_xs,y_label:batch_ys })
        if i % 50 ==0:
            print(compute_accuracy(mnist.test.images[:1000], 
                                   mnist.test.labels[:1000]))
        if i % MODEL_SAVE_INTERVAL == 0:
            save_path = saver.save(sess, SUMMARY_DIR + "/nn_model_ep_" +
                                       str(i) + ".ckpt")
