import abc

class Espsilon(object, metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def decrease(cls):
        raise NotImplementedError("Decrease Epsilon is not implemented")
