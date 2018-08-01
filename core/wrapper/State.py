import abc


class State(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getDimensions(self):
        raise NotImplementedError("User must define Dimensions of the State space")

    @abc.abstractmethod
    def getValue(self):
        raise  NotImplementedError("User must define the return of the state value")
