import abc


class Policy(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init(self, greedyPolicy, epsilonPolicy):
        raise NotImplementedError("init must be implemented")

    @abc.abstractmethod
    def getEpsilonGreedyAction(self, state, actionValueFunction):
        raise NotImplementedError("epsilon greedy must be added")


    @abc.abstractmethod
    def getGreedyAction(self, state, actionValueFunciton):
        raise NotImplementedError("greedy algorithm must be added")