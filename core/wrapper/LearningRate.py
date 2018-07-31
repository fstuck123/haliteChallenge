import abc

class LearningRate(object, metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def decrease(cls):
        raise NotImplementedError("Decrease Learningrate is not implemented yet")