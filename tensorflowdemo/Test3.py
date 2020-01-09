# -*- coding: utf-8 -*-

import tensorflow as tf


# tensorflow count demo
def test_tf_variable_1():

    state = tf.Variable(0, name="counter")
    one = tf.constant(2)
    new_value = tf.add(state, one)
    update = tf.assign(state, new_value)

    # init all variables
    init_op = tf.initialize_all_variables()

    # run session
    with tf.Session() as sess:
        sess.run(init_op)
        print("init state", sess.run(state))
        for i in range(3):
            sess.run(update)
            print("add state", sess.run(state))


if __name__ == '__main__':
    test_tf_variable_1()
