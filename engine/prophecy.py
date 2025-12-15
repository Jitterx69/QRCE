import numpy as np

class Prophecy:
    def __init__(self, noise):
        self.noise = float(noise)

    def measure(self, s):
        if self.noise == 0.0:
            return s.v.copy()
        return s.v + self.noise * np.random.randn(*s.v.shape)
