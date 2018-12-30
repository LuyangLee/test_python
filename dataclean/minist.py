from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets(".\\MINIST_DATA\\",one_hot=True)

# print("training data ", mnist.train.num_examples)
# print("validation data ", mnist.validation.num_examples)
# print('testing data ', mnist.test.num_examples)

batch_size = 100
x, y = mnist.train.next_batch(batch_size)
print(x.shape)
print(y.shape)