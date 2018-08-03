from core.wrapper.LearningRate import LearningRate


class LearningRateImpl(LearningRate):

    def __init__(self):
        self.value = 1.0
        self.decreaseFactor = 0.0001



    def getValue(self):
        return self.value;


    def decrease(self):
        self.value = self.value * self.decreaseFactor