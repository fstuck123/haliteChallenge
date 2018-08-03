import abc


class Action(object, metaclass=abc.ABCMeta):

    #action index is in reference to the absolute index of the class in the prediction output
    @abc.abstractmethod
    def getAction(self, index):
        raise NotImplementedError("getAction must be implemented")


    #every entry with a True is a probability
    # every entry with a False is a regression prediction between 0 and 1
    @abc.abstractmethod
    def getActionProbabilities(self):
        raise NotImplementedError("getActionProbabilities not implemented")


    @abc.abstractmethod
    def getOutputDimensions(self):
        raise NotImplementedError("The output dimensions of the Action must be defined")

