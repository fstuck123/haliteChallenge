import abc

class ActionValueFunction(object, metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def init(cls):
        raise NotImplementedError("init ActionValueFunciton must be implemented")


    @abc.abstractclassmethod
    def update(cls, state, action, nextState, stateValueFunction, learningRate):
        raise NotImplementedError("update ActionValueFunction not implemented yet")