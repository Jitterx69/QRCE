import numpy as np
from quantum.povm import POVM

def test_measurement_disturbance():
    rho = np.array([[0.5,0.5],[0.5,0.5]], dtype=complex)
    povm = POVM([np.diag([1,0]), np.diag([0,1])])
    probs = povm.measure(rho)
    assert abs(sum(probs) - 1.0) < 1e-8
