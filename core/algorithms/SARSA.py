




class SARSA:
    def __init__(self, policy, actionValueFunction, stateValueFunction, learningRate, epsilon, environment):
        self.policy = policy
        self.actionValueFunction = actionValueFunction
        self.stateValueFunction = stateValueFunction
        self.learningRate = learningRate
        self.epsilon = epsilon
        self.environment = environment


    def execute(self):
        self.actionValueFunction.init();
        state = self.environment.init();
        while not self.environment.terminated():
            action = self.policy.getEpsilonGreedyAction(state, actionValueFunction=self.actionValueFunction)
            nextState = self.environment.getNextState(action);
            reward = self.environment.getReward();
            self.actionValueFunction.update(state, action, nextState, self.stateValueFunction, self.learningRate);
            state = nextState;
            self.learningRate.decrease();
            self.epsilon.decrease();



