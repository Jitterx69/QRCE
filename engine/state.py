import numpy as np

class State:
    def __init__(self, vector: np.ndarray):
        self.v = vector.astype(float)

    def copy(self):
        return State(self.v.copy())

    def norm(self):
        return np.linalg.norm(self.v)

    def normalize(self):
        n = self.norm()
        if n > 0:
            self.v /= n
        return self
