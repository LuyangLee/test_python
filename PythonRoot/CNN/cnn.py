from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
mnist = input_data.read_data_sets("MINIST_DATA/",one_hot= True)
sess = tf.Session()

# build neural 
# weight
def weight_variable(wshape):
    initial = tf.truncated_normal(wshape, stddev= 0.1)
    return tf.Variable(initial)

def bias_variable(bshape):
    initial = tf.constant(0.1, shape= bshape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides = [1, 1, 1, 1], padding = 'SAME')

def max_pool(x):
    return tf.nn.max_pool(x, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')

# inputdata[numbers, size] label[numbers, size]
x_input = tf.placeholder(dtype = tf.float32, shape = [None, 784])
y_label = tf.placeholder(dtype = tf.float32, shape = [None, 10])

# change put into true size
x_image = tf.reshape(x_input, [-1, 28, 28, 1])

# begin cnn
w1 = weight_variable([5, 5, 1, 32])
b1 = bias_variable([32])
c1 = conv2d(x_image, w1)
a1 = tf.nn.relu(c1 + b1)
p1 = max_pool(a1)