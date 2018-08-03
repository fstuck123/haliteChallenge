from core.wrapper.Policy import Policy
import numpy as np
import numpy.random as random


class PolicyImpl(Policy):


    def init(self, greedyPolicy, epsilonPolicy, action):
        self.greedyPolicy = greedyPolicy
        self.epsilonPolicy = epsilonPolicy
        self.action = action
        self.actionClasses = action.getActionProbabilities()
        self.getClassIndices()
        self.maxClasses = len(self.classIndices)



    def getEpsilonGreedyAction(self, state, actionValueFunction):
        if np.random() < self.greedyPolicy.getValue():
            self.getRandomAction();
        else:
            self.getGreedyAction(state, actionValueFunction);
        return [self.actionPrediction, self.regression]


    def getGreedyAction(self, state, actionValueFunction):
        prediction = actionValueFunction.evaluate(state);
        self.getAction(prediction)
        return [self.actionPrediction, self.regression]





    def getAction(self, prediction):
        classes = []
        self.regression =[]
        for i in range(len(prediction)):
            if self.actionClasses[i] :
                # is a class
                classes.append(prediction[i]);
            else:
                self.regression.append(prediction[i]);

        # get action
        index = np.argmax(classes);
        self.actionPrediction = self.classIndices[index];


    def getClassIndices(self):
        self.classIndices = []
        self.regressionCounter =0
        for i in range(len(self.action.getOutputDimensions())):
            if self.actionClasses[i] :
                # is a class
                self.classIndices.append(i)
            else:
                self.regressionCounter = self.regressionCounter + 1

    def getRandomAction(self):
        self.actionPrediction = random.randint(0, self.maxClasses);
        self.regression = random.rand(self.regressionCounter)

