import tensorflow as tf
import numpy as np
import write_log
# 梯度下降优化器
# 梯度下降算法可以求任何可导的复杂函数的极值，不管它是有多少元的函数
# step1:定义训练数据
x_data = np.random.rand(100)
y_data = 0.1 * x_data ** 2 + 5 * x_data + 0.2
# step2：定义模型
a = tf.Variable(0., name="a")
b = tf.Variable(0., name="b")
c = tf.Variable(0., name="c")
x_input = tf.placeholder(dtype=tf.float32)
y_input = tf.placeholder(dtype=tf.float32)
y = a * x_input ** 2 + b * x_input + c
loss = tf.reduce_mean(tf.square(y - y_input))
# step3：定义梯度降落操作
gd = tf.train.GradientDescentOptimizer(0.2)
gd_compute_op = gd.compute_gradients(loss)
gd_apply_op = gd.apply_gradients(gd_compute_op)
# step4:开始训练
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    writer = write_log.get_writer(sess)
    for _ in range(10000):
        print(sess.run([a, b, c]))
        sess.run(train, feed_dict={x_input: x_data, y_input: y_data})
