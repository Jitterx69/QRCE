import numpy as np

class Regulator:
    def __init__(self, leakage):
        self.leakage = float(leakage)

    def filter(self, prophecy):
        return (1.0 - self.leakage) * prophecy
