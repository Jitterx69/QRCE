class Runner:
    def __init__(self, operator):
        self.operator = operator

    def run(self, state, steps):
        history = [state.copy()]
        for _ in range(steps):
            state = self.operator(state)
            history.append(state.copy())
        return history
