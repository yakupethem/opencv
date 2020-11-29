import cv2
import tensorflow as tf
import imageio


hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))