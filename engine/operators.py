import numpy as np
from .state import State

class LinearOperator:
    def __init__(self, matrix):
        self.M = np.asarray(matrix, dtype=float)

    def apply(self, s: State):
        return State(self.M @ s.v)
