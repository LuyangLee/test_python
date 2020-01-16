import tensorflow as tf 
import os
import numpy as np
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 构建神经网络层的函数
def add_layer(inputs, in_size, out_size, layer, activation_function=None):
    layer_name = "layer_%s"%layer
    with tf.name_scope("layer"):
        with tf.name_scope("weight"):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name="W")
            tf.summary.histogram(layer_name + "/Weights", Weights)
        with tf.name_scope("bias"):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name= 'B')
            tf.summary.histogram(layer_name + "/Biases", biases)
        with tf.name_scope("Wx_plus_b"):    
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name + "/outputs", outputs)
        return outputs

# 构建数据占位
xs =  tf.placeholder(tf.float32, [None, 1])
ys =  tf.placeholder(tf.float32, [None, 1])

# 构建神经网络
l1 = add_layer(xs, 1, 10, 'hidden1', activation_function=tf.nn.relu)
prediction = add_layer(l1, 10, 1, 'prediction1', activation_function=None)

#构建损失函数和反向传播
with tf.name_scope("loss"):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                        reduction_indices=[1]))
    tf.summary.scalar("loss", loss)
learning_rate = 0.1
with tf.name_scope("train"):
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

x_data = np.linspace(-1,1,300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
fig = plt.figure(facecolor= 'y')
axe = fig.add_subplot(111)
axe.patch.set_facecolor('#FFB6C1')
axe.scatter(x_data, y_data)
plt.ion()
plt.show()

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("log\\",sess.graph)

    STEPS = 1000
    for i in range(STEPS):
        sess.run(train_step, feed_dict = {xs:x_data, ys:y_data})
        if i %50 == 0:
            try:
                axe.lines.remove(line[0])
            except:
                pass
            pre_value = sess.run(prediction, feed_dict = {xs:x_data})
            line = axe.plot(x_data, pre_value, 'v-.', label = 'test1', color = "#FF3030")
            plt.savefig('test')
            rs = sess.run(merged, feed_dict={xs:x_data, ys:y_data})
            writer.add_summary(rs, i)


