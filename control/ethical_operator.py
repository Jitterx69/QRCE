class EthicalOperator:
    def __init__(
        self,
        phi,
        harm_fn,
        leakage_constraint,
        stability_constraint,
        bellman
    ):
        self.phi = phi
        self.harm_fn = harm_fn
        self.leakage_constraint = leakage_constraint
        self.stability_constraint = stability_constraint
        self.bellman = bellman

    def step(self, state, info_measure, growth, future_cost):
        if not self.leakage_constraint.satisfied(info_measure):
            return state

        if not self.stability_constraint.satisfied(growth):
            return state

        return self.phi(state)

    def evaluate_actions(self, states, harms, futures):
        idx = self.bellman.select(harms, futures)
        return states[idx]
