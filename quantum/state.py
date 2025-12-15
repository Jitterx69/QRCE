import numpy as np

class DensityState:
    def __init__(self, rho):
        self.rho = np.asarray(rho, dtype=complex)
        self._validate()

    def _validate(self):
        assert self.rho.shape[0] == self.rho.shape[1]
        assert abs(np.trace(self.rho) - 1.0) < 1e-8

    def copy(self):
        return DensityState(self.rho.copy())

    def distance(self, other):
        diff = self.rho - other.rho
        eigs = np.linalg.eigvalsh(diff.conj().T @ diff)
        return 0.5 * sum(eigs**0.5)

    def entropy(self):
        eigs = np.linalg.eigvalsh(self.rho)
        eigs = eigs[eigs > 0]
        return -sum(eigs * np.log(eigs))
