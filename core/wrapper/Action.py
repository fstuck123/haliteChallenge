import abc


class Action(object, metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def getAction(self, index):
        raise NotImplementedError("getAction must be implemented")


    @abc.abstractmethod
    def getOutputDimensions(self):
        raise NotImplementedError("The output dimensions of the Action must be defined")

