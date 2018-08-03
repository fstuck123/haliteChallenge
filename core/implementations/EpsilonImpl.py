from core.wrapper.Epsilon import Epsilon


class EpsilonImpl(Epsilon):


    def __init__(self):
        self.value = 1.0
        self.proportialDecrease = 0.0001

    def decrease(self):
        self.value = self.value * self.proportialDecrease


    def getValue(self):
        return self.value
