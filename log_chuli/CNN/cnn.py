from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
mnist = input_data.read_data_sets("MINIST_DATA/",one_hot= True)
sess = tf.Session()

# weight
def weight_variable(wshape):
    initial = tf.truncated_normal(wshape, stddev= 0.1)
    return tf.Variable(initial)

def bias_variable(bshape):
    initial = tf.constant(0.1, shape= bshape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides = [1, 1, 1], padding = 'SAME')

def max_pool(x):
    return tf.nn.max_pool(x, )