from core.implementations.AlgorithmStateImpl import, AlgorithmStateImpl
from core.wrapper.Action import Action
from persistence.Files import Files


class SARSA:
    def __init__(self, policy, actionValueFunction, stateValueFunction, learningRate, epsilon, environment, experimentID):
        self.policy = policy
        self.actionValueFunction = actionValueFunction
        self.stateValueFunction = stateValueFunction
        self.learningRate = learningRate
        self.epsilon = epsilon
        self.environment = environment
        self.filename = experimentID


    def execute(self):
        sampleAction = Action();
        state = self.environment.init();
        self.actionValueFunction.init(state, sampleAction);
        while not self.environment.terminated():
            action = self.policy.getEpsilonGreedyAction(state, actionValueFunction=self.actionValueFunction)
            nextState = self.environment.getNextState(action);
            reward = self.environment.getReward();
            self.actionValueFunction.update(state, action, nextState, self.stateValueFunction, self.learningRate);
            state = nextState;
            self.learningRate.decrease();
            self.epsilon.decrease();

        algState = AlgorithmStateImpl().createSnapshot();
        Files().saveObject(algState, self.filename)

