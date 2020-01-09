# -*- coding: utf-8 -*-

import tensorflow as tf


# base tensorflow demo
def test_tf_1():
    matrix1 = tf.constant([[3., 3.]])
    matrix2 = tf.constant(2., shape=(2, 2))

    product = tf.matmul(matrix1, matrix2)

    sess = tf.Session()
    result = sess.run(product)

    print(result)
    sess.close()


if __name__ == '__main__':
    test_tf_1()

