import abc

class LearningRate(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def decrease(self):
        raise NotImplementedError("Decrease Learningrate is not implemented yet")