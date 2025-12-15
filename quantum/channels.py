import numpy as np

class CPTP:
    def __init__(self, kraus_ops):
        self.K = [np.asarray(K, dtype=complex) for K in kraus_ops]
        self._validate()

    def _validate(self):
        acc = sum(K.conj().T @ K for K in self.K)
        assert np.allclose(acc, np.eye(acc.shape[0]), atol=1e-8)

    def apply(self, rho):
        return sum(K @ rho @ K.conj().T for K in self.K)

def amplitude_damping(gamma):
    import numpy as np
    K0 = np.array([[1, 0], [0, (1-gamma)**0.5]])
    K1 = np.array([[0, gamma**0.5], [0, 0]])
    return CPTP([K0, K1])
