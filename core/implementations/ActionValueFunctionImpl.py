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

        widthFilter = 5;
        padding = 0
        stride = 2
        poolSize =3

        # calculate final dimensions before the fully connected network begins
        #conv layer
        finalX = (self.inputDimensions.x() - widthFilter + 2 * padding) / (stride + 1)
        #max pool layer
        finalX = (finalX - poolSize) / (poolSize + 1)
        finalX = (finalX - widthFilter + 2 * padding) / (stride + 1)
        # max pool layer
        finalX = (finalX - poolSize) / (poolSize + 1)
        finalY = (self.inputDimensions.y() - widthFilter + 2 * padding) / (stride + 1)
        # max pool layer
        finalY = (finalY - poolSize) / (poolSize + 1)
        finalY = (finalY - widthFilter + 2 * padding) / (stride + 1)
        # max pool layer
        finalY = (finalY - poolSize) / (poolSize + 1)

        self.weights = {
            # 5x5 conv
            'wc1': tf.Variable(tf.random_normal([widthFilter,widthFilter,self.inputDimensions.dimensions,32])),
            'wc2': tf.Varialbe(tf.random_normal([widthFilter,widthFilter, 32, 64])),
            # fully connected
            'wd1': tf.Variable(tf.random_normal([finalX * finalY * 64, 1024])),
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
        conv1 = self.conv(self.x, self.weights['wc1'], self.bias['bc1'], stride);
        conv1 = self.maxpool2d(conv1, k=poolSize)
        conv2 = self.conv(conv1, self.weights['wc2'], self.bias['bc2'], stride);
        conv2 = self.maxpool2d(conv2, k=poolSize)

        #reshape conv2 to be a two dimensional input
        fc1 = tf.reshape(conv2, [-1, self.weights['wd1'].get_shape().as_list()[0]])

        fc1 = tf.add(tf.matmul(fc1, self.weights['wd1']), self.bias['bd1'])
        fc1 = tf.nn.relu(fc1)

        dropout = 0.5
        fc1 = tf.nn.dropout(fc1, dropout)

        self.out = tf.add(tf.matmul(fc1, self.weights['out']), self.bias['out'])









    def conv(self, x, W, b, strides = 2):
        x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME');
        x = tf.nn.bias_add(x, b)
        return tf.nn.relu(x)

    def maxpool2d(self, x, k=2):
        return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1],
                              padding='SAME')
