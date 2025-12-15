import numpy as np

class LeakageConstraint:
    def __init__(self, epsilon):
        self.epsilon = float(epsilon)

    def satisfied(self, info_measure):
        return info_measure <= self.epsilon


class StabilityConstraint:
    def __init__(self, max_growth):
        self.max_growth = float(max_growth)

    def satisfied(self, growth):
        return growth <= self.max_growth
