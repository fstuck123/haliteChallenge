import abc

class ActionValueFunction(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init(self):
        raise NotImplementedError("init ActionValueFunciton must be implemented")


    @abc.abstractmethod
    def update(self, state, action, nextState, stateValueFunction, learningRate):
        raise NotImplementedError("update ActionValueFunction not implemented yet")