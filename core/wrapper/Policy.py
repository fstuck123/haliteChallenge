import abc


class Policy(object, metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def init(cls, greedyPolicy, epsilonPolicy):
        raise NotImplementedError("init must be implemented")

    @abc.abstractclassmethod
    def getEpsilonGreedyAction(cls, state, actionValueFunction):
        raise NotImplementedError("epsilon greedy must be added")


    @abc.abstractclassmethod
    def getGreedyAction(cls, state, actionValueFunciton):
        raise NotImplementedError("greedy algorithm must be added")