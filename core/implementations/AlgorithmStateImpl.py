from core.wrapper.AlgorithmState import AlgorithmState


class AlgorithmStateImpl(AlgorithmState):

    def createSnapshot(self, ActionvalueFunction, StateValueFunction, LearningRate, Epsilon):
        self.actionValueFunction = ActionvalueFunction;
        self.stateValueFunction = StateValueFunction
        self.learningRate = LearningRate
        self.epsilon = Epsilon

