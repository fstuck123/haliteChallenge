import abc

class Environment(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getNextState(self, action):
        raise NotImplementedError("next state must be implemented")

    @abc.abstractmethod
    def getReward(self):
        raise NotImplementedError("reward not implemented")

    @abc.abstractmethod
    def init(self):
        raise NotImplementedError("init Environment must be implemented. Return is the first state")


    @abc.abstractmethod
    def terminated(self):
        raise NotImplementedError("terminated must be implemented")