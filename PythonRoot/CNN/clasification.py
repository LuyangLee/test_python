# summary
#   classification quetion
# Author
#   sophialee
# Date
#   2019-3-19
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

# 传入数据集
minist = input_data.read_data_sets("./MINIST_DATA", one_hot= True)
pix = 28 * 28
print(pix)
# 构建运算变量
x_data = tf.placeholder(dtype= tf.float32, shape=[None, pix])
x_label = tf.placeholder(dtype= tf.float32, shape=[None, 10])

# 构建神经网络层的函数
def add_layer(inputs, in_size, out_size, layer, activation_function=None):
    layer_name = "layer_%s"%layer
    with tf.name_scope("layer"):
        with tf.name_scope("weight"):
            # in_size 接受的是上一层的，特别的第一层接受的是输入图片的大小(一般都是转化为二位的矩阵传入)输出的是下一层
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


def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={x_data: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={x_data: v_xs, x_label: v_ys})
    return result

# 和回归相似，输入大小是图片等数据，输出的大小是类别数目
hidden1 = add_layer(x_data, pix, 100, 'hidden1',activation_function= tf.nn.relu)
hidden2 = add_layer(hidden1, 100, 100, 'hidden2',activation_function= tf.nn.relu)
prediction = add_layer(hidden2, 100, 10,"out", activation_function= tf.nn.softmax)

# 损失函数和 优化反向传播
loss = tf.reduce_mean(-tf.reduce_sum(x_label * tf.log(tf.clip_by_value(prediction, 1e-10, 1.0)), reduction_indices=[1]))
tf.summary.scalar('loss',loss)
learning_rate = 0.1
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

# 训练
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    # 标量集合和图表集合
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter('log\\', sess.graph)
    saver = tf.train.Saver()
    STEPS = 500
    for i in range(STEPS):
        batch_xs, batch_ys = minist.train.next_batch(100)
        sess.run(train_step, feed_dict={x_data:batch_xs, x_label:batch_ys})
        if i %50 ==0:
            sess.run(loss,feed_dict={x_data:batch_xs, x_label:batch_ys})
            rs = sess.run(merged, feed_dict={x_data:batch_xs, x_label:batch_ys})
            writer.add_summary(rs, i)
            print(compute_accuracy(
                minist.test.images, minist.test.labels))

