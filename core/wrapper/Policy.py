import abc

# get*Action functions return a list
# first the index of the choosen action and
# in the second list the regression values
# the index of the action is so the action class can be querried for the corresponding value
class Policy(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init(self, greedyPolicy, epsilonPolicy, action):
        raise NotImplementedError("init must be implemented")

    @abc.abstractmethod
    def getEpsilonGreedyAction(self, state, actionValueFunction):
        raise NotImplementedError("epsilon greedy must be added")


    @abc.abstractmethod
    def getGreedyAction(self, state, actionValueFunction):
        raise NotImplementedError("greedy algorithm must be added")