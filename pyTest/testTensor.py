import os 
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

# #常量
# a = tf.constant([1.0, 2.0], name = 'a')
# b = tf.constant([0.0, 1.0], name =  'b')
# result = a + b 
# x = tf.constant([[1.0, 0.0],[2.0, 1.0]], name = 'x')

# with tf.Session() as sess:
#     print(sess.run(result)) #得到真实的数字
#     print(x.eval(session=sess)) #或者用这种方式
#     print(a)#得到张量的属性
#     print(x.get_shape()) #格式为（单个维度数组长度，维度数）一维中的一会默认不显示出来，
    
#或者运用下面方法，设置为默认会话
#变量
w1 = tf.Variable(tf.zeros([2,4], dtype= 'float32'), name = 'w1')
w2 = tf.Variable(tf.ones([2,4], dtype = 'float32'), name = 'w2')
w3 = tf.Variable(tf.random_normal([2,3],mean = 1.0, stddev = 1,seed = 1))
w4 = tf.Variable(tf.random_normal([3,1],mean = 1.0, stddev= 1, seed = 1))
x = tf.placeholder(tf.float32,name= "input")
a = tf.matmul(x, w3)
y = tf.matmul(a, w4)
sess = tf.Session()
init = tf.global_variables_initializer()
with sess.as_default():
    sess.run(init)
    print(sess.run(y,feed_dict = {x:[[0.7, 0.9]]}))

writer = tf.summary.FileWriter(".\\log",tf.get_default_graph())
writer.close()



# g1 = tf.Graph()
# with g1.as_default():
#     v = tf.get_variable("v",shape = [1], initializer = tf.zeros_initializer)


# g2 = tf.Graph()
# with g2.as_default():
#     v = tf.get_variable("v",shape = [1], initializer=tf.ones_initializer)

# with tf.Session(graph=g1) as sess:
#     tf.global_variables_initializer().run()
#     with tf.variable_scope("",reuse=True):
#         print(sess.run(tf.get_variable("v")))
