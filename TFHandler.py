# coding=utf-8
"""
2017.2.27
my api for tensorflow
"""
import tensorflow as tf


class TFHandler(object):
    def __init__(self):
        self.tf = tf
        self.sess = tf.Session()
        self.saver = tf.train.Saver()

    def save(self):
        pass

    def restore(self):
        pass

    def load(self):
        pass


if __name__ == '__main__':
    pass
