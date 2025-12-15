import numpy as np

class QuantumAgent:
    def __init__(self, unitaries):
        self.U = [np.asarray(U, dtype=complex) for U in unitaries]

    def act(self, branches):
        out = 0
        for U, rho in zip(self.U, branches):
            out += U @ rho @ U.conj().T
        return out
