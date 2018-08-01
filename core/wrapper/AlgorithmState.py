import abc


class AlgorithmState(object, metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def createSnapshot(self, ActionvalueFunction, StateValueFunction, LearningRate, Epsilon):
        raise NotImplementedError("create Snapshot in Algorithmstate not implemented yet")