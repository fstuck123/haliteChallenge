import pickle
import os
import random
import datetime
from states.HaliteStates import HaliteStates



class Files:
    directory =""
    file =""


    def __init__(self, relativeDirectory):
        #self.directory = os.path.dirname(os.path.realpath(__file__)) + relativeDirectory
        self.directory =  relativeDirectory
        self.file = str(datetime.datetime.now()) + "_" + str(random.randint(0, 10));


    def accessFile(self, file):
        bytearray = open(self.directory + file, "rb");
        # probably have to import HaliteStates so that pickle knows which class the bytes belong to
        object = pickle.load(bytearray)
        bytearray.close()
        return object



    #automatically create filename for the state
    def saveStateRandom(self, haliteState):
        fileSystem = open(self.directory + self.file, "wb+");
        pickle.dump(haliteState, fileSystem);
        fileSystem.close()

    def saveState(self, haliteState, num):
        fileSystem = open(self.directory + self.file + str(num), "wb+");
        pickle.dump(haliteState, fileSystem);
        fileSystem.close()