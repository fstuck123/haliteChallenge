import abc

class Espsilon(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def decrease(self):
        raise NotImplementedError("Decrease Epsilon is not implemented")
