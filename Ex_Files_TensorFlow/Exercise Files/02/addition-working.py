import os
# import TensorFlow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# Turn off TensorFlow warning messages in program output
# Tells TensorFlow not to output as many log messages as it normally does
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define computational graph
# Define the X and Y input nodes -> will be placeholder nodes that get assigned
# a new value every time we make a calculation.
X = tf.placeholder(tf.float32, name="X")    # pass on data type and name as parameters
Y = tf.placeholder(tf.float32, name="Y")

# Define the node that does addition operation
# Add tf.add node
addition = tf.add(X, Y, name="addition")    # links X and Y nodes to the computational graph

# Create the session
# To execute operations in the graph, we have to create a session.
with tf.Session() as session:
    # pass the operation we want to run
    # When addition operations runs, it needs to grab values of X and Y nodes & also need
    # to feed in values for X and Y -> supply parameter called 'feed dict'
    # feed dict parameter and then pass in X and Y ans five them each a ray value

    # Pass in arrays, and result is also an array. Tensors are multi-dimensional arrays
    # result = session.run(addition, feed_dict=({X: [1], Y: [4]}))
    # result = session.run(addition, feed_dict=({X: [1, 2, 3], Y: [4, 5, 6]}))
    result = session.run(addition, feed_dict=({X: [[1, 2, 3], [4, 5, 6]], Y: [[7, 8, 9], [10, 11, 12]]}))

    print(result)