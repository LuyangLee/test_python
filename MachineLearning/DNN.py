import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split

in_units = 2
h1_units = 20
out_units = 5
Lrate = 1e-4

def add_layer(input, in_size, out_size, activation_function=None):
    W = tf.Variable(tf.random.normal([in_size,out_size]))
    b = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    f = tf.matmul(input, W) + b
    if activation_function is None:
        output = f
    else:
        output = activation_function(f)
    return output

## input data
all_data = np.loadtxt('./data_2.csv')
x_train, x_test, y_train, y_test = train_test_split(all_data[:,0:2], all_data[:,2], test_size = 0.4 )
y_train = y_train.astype(int)
y_test = y_test.astype(int)
y_hot_train = np.eye(5)[y_train.reshape(-1) - 1]
y_hot_test = np.eye(5)[y_test.reshape(-1) - 1]
## change into one-hot code

## build NN
## define placehold
x = tf.compat.v1.placeholder(tf.float32, [None, in_units])
y_ = tf.compat.v1.placeholder(tf.float32, [None, out_units])

## build calcul graph
hidden = add_layer(x, in_units, h1_units, tf.nn.relu)
y = tf.nn.softmax(add_layer(hidden, h1_units, out_units))

## define loss
cross_entroy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.math.log(y), axis= 1))

train_step = tf.compat.v1.train.AdamOptimizer(Lrate).minimize(cross_entroy)
init_op = tf.compat.v1.global_variables_initializer()
## end build

## define judgement
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.compat.v1.Session() as sess:
    sess.run(init_op)
    for i in range(10000):
        train_step.run(feed_dict={x: x_train, y_: y_hot_train})
        # sess.run(train_step, feed_dict={x: x_train, y_: y_hot_train})
        if i%100 == 0:
            # print(sess.run(cross_entroy, feed_dict={x: x_train, y_: y_hot}))
            train_accuracy = accuracy.eval(feed_dict={x: x_test, y_:y_hot_test})
            print("training accuracy %g"%( train_accuracy))
    
    print("learning rate is %g, test accuracy %g"%(Lrate,accuracy.eval(feed_dict={x: x_test, y_:y_hot_test})))