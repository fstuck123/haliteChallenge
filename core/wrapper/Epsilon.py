import abc

class Epsilon(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def decrease(self):
        raise NotImplementedError("Decrease Epsilon is not implemented")


    @abc.abstractmethod
    def getValue(self):
        raise NotImplementedError("get Value of Epsilon not implemented")
