import numpy as np

class State:
    def __init__(self, vector):
        self.v = np.asarray(vector, dtype=float)

    def copy(self):
        return State(self.v.copy())

    def norm(self):
        return np.linalg.norm(self.v)

    def normalize(self):
        n = self.norm()
        if n > 0:
            self.v /= n
        return self
    
    def distance(self, other):
        return np.linalg.norm(self.v - other.v)

