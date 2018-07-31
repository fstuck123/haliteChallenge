import abc


class State(object, metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def getDimensions(cls):
        raise NotImplementedError("User must define Dimensions of the State space")

    @abc.abstractclassmethod
    def getValue(cls):
        raise  NotImplementedError("User must define the return of the state value")
