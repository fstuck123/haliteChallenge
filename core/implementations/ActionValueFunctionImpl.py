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
        self.conv1 = self.conv(self.x, self.weights['wc1'], self.bias['bc1'], stride);
        self.conv1 = self.maxpool2d(self.conv1, k=poolSize)
        self.conv2 = self.conv(self.conv1, self.weights['wc2'], self.bias['bc2'], stride);
        self.conv2 = self.maxpool2d(self.conv2, k=poolSize)

        #reshape conv2 to be a two dimensional input
        self.fc1 = tf.reshape(self.conv2, [-1, self.weights['wd1'].get_shape().as_list()[0]])

        self.fc1 = tf.add(tf.matmul(self.fc1, self.weights['wd1']), self.bias['bd1'])
        self.fc1 = tf.nn.relu(self.fc1)

        dropout = 0.5
        self.fc1 = tf.nn.dropout(self.fc1, dropout)

        self.out = tf.add(tf.matmul(self.fc1, self.weights['out']), self.bias['out'])

        # calculate Error and optimize error (no logs or softmax)
        self.error = tf.reduce_sum(tf.square(self.out - self.y))
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(self.error)

        # init tensorflow
        self.gpuMemFraction = 0.05
        self.gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=self.gpuMemFraction)
        self.sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, gpu_options=self.gpu_options))
        self.init = tf.global_variables_initializer()
        self.sess.run(self.init)



    def evaluate(self, state):
        input = state.getValue();
        prediction = self.sess.run(self.out, feed_dict={self.x : input})
        return prediction;


    def update(self, state, action, nextState, stateValueFunction, learningRate, targetValue):
        self.sess.run(self.optimizer, feed_dict={self.y : targetValue})







    def conv(self, x, W, b, strides = 2):
        x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME');
        x = tf.nn.bias_add(x, b)
        return tf.nn.relu(x)

    def maxpool2d(self, x, k=2):
        return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1],
                              padding='SAME')
