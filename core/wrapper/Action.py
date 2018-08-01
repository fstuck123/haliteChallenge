import abc


class Action(object, metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def getAction(self, index):
        raise NotImplementedError("getAction must be implemented")




