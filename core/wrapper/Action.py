import abc


class Action(object, metaclass=abc.ABCMeta):


    @abc.abstractclassmethod
    def getAction(cls, index):
        raise NotImplementedError("getAction must be implemented")




