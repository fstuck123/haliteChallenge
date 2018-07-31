import abc

class Environment(object, metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def getNextState(cls, action):
        raise NotImplementedError("next state must be implemented")

    @abc.abstractclassmethod
    def getReward(cls):
        raise NotImplementedError("reward not implemented")


    @abc.abstractclassmethod
    def terminated(cls):
        raise NotImplementedError("terminated must be implemented")