import numpy as np

class Agent:
    def __init__(self, gain=1.0):
        self.gain = float(gain)

    def policy(self, prophecy):
        return self.gain * np.tanh(prophecy)
