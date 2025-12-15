import numpy as np
from .state import State

class World:
    def __init__(self, dynamics_matrix):
        self.A = np.asarray(dynamics_matrix, dtype=float)

    def step(self, s: State, action):
        return State(self.A @ s.v + action)
