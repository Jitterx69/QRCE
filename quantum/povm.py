import numpy as np

class POVM:
    def __init__(self, effects):
        self.E = [np.asarray(E, dtype=complex) for E in effects]
        acc = sum(self.E)
        assert np.allclose(acc, np.eye(acc.shape[0]), atol=1e-8)

    def measure(self, rho):
        probs = [np.real(np.trace(E @ rho)) for E in self.E]
        return probs

    def instrument(self):
        return [np.linalg.cholesky(E) for E in self.E]
