from core.wrapper.ActionValueFunction import ActionValueFunction
import tensorflow as tf


class ActionValueFunctionImpl1(ActionValueFunction):


    # output should be a class of action to choose from
    def init(self, state, sampleAction):
        self.inputDimensions = state.getDimensions();
        self.outputDimensions = sampleAction.getOutputDimensions();
        # not sure if inputDimensions can be concatinated that way
        self.x = tf.placeholder(tf.float32, [None, self.inputDimensions])
        self.y = tf.placeholder(tf.float32, [None, self.outputDimensions])


        self.weights = {
            # 5x5 conv
            'wc1': tf.Variable(tf.random_normal([5,5,self.inputDimensions.dimensions,32])),
            'wc2': tf.Varialbe(tf.random_normal([5,5, 32, 64])),
            # fully connected
            'wd1': tf.Variable(tf.random_normal([, 1024])),
            'out': tf.Variable(tf.random_normal([1024, self.outputDimensions]))

        }

        self.bias ={
            'bc1': tf.Variable(tf.random_normal(32)),
            'bc2': tf.Variable(tf.ranom_normal(64)),
            #fully connected
            'bd1': tf.Variable(tf.random_normal(1024)),
            'out': tf.Variable(tf.random_normal(self.outputDimensions))
        }

        # define net
        conv1 = self.conv(self.x, self.weights['wc1'], self.bias['bc1']);
        conv2 = self.conv(conv1, self.weights['wc2'], self.bias['bc2']);






    def conv(self, x, W, b, strides = 1):
        x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME');
        x = tf.nn.bias_add(x, b)
        return tf.nn.relu(x)
