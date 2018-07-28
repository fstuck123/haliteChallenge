import pickle
import os
from states.HaliteStates import HaliteStates


class Files:
    directory =""
    file =""


    def __init__(self, relativeDirectory):
        self.directory = os.path.dirname(os.path.realpath(__file__)) + relativeDirectory


    def accessFile(self, file):
        bytearray = open(self.directory + file, "rb");
        # probably have to import HaliteStates so that pickle knows which class the bytes belong to
        object = pickle.load(bytearray)
        return object


    def saveState(self, file, haliteState):
        fileSystem  = open(self.directory + file, "wb");
        pickle.dump(haliteState, fileSystem);



    # automatically create filename for the state
    # def saveState(self, haliteState):
