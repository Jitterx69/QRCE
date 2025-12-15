import numpy as np

class BellmanRegulator:
    def __init__(self, gamma):
        self.gamma = float(gamma)

    def value(self, harm, future):
        return harm + self.gamma * future

    def select(self, harms, futures):
        values = [self.value(h, f) for h, f in zip(harms, futures)]
        return int(np.argmin(values))
