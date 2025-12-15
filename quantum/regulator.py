import numpy as np

class QuantumRegulator:
    def __init__(self, depolarization):
        self.p = depolarization

    def apply(self, rho):
        d = rho.shape[0]
        return (1 - self.p) * rho + self.p * np.eye(d) / d
