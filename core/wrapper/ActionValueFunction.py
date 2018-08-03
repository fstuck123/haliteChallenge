import abc

class ActionValueFunction(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init(self, state, sampleAction):
        raise NotImplementedError("init ActionValueFunciton must be implemented")


    @abc.abstractmethod
    def update(self, state, action, nextState, stateValueFunction, learningRate):
        raise NotImplementedError("update ActionValueFunction not implemented yet")


    @abc.abstractmethod
    def evaluate(self, state):
        raise NotImplementedError("evaluation of ActionValueFunction has not been implemented yet")