# import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# input = tf.Variable(tf.ones([1, 84, 84, 1]))
# filter =tf.Variable(tf.ones([8, 8, 1, 1]))

# with tf.Session() as sess:
#     tf.global_variables_initializer()
#     res = tf.nn.conv2d(input, filter, [1, 4, 4, 1], padding = 'SAME')
#     print(res.shape)
x = '0x2308'
print(x.encode(encoding = 'uni'))