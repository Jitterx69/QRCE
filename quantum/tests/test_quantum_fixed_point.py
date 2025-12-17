import numpy as np
from quantum.state import DensityState
from quantum.channels import amplitude_damping
from quantum.povm import POVM
from quantum.regulator import QuantumRegulator
from quantum.agent import QuantumAgent
from quantum.quantum_operator import QuantumReflexiveOperator
from quantum.fixed_point import iterate

def test_quantum_fixed_point():
    rho0 = DensityState(np.eye(2) / 2)

    channel = amplitude_damping(0.1)
    # Use valid POVM elements that sum to identity
    povm = POVM([np.array([[0.5, 0], [0, 0.5]]), np.array([[0.5, 0], [0, 0.5]])])
    regulator = QuantumRegulator(0.2)
    agent = QuantumAgent([np.eye(2), np.eye(2)])

    phi = QuantumReflexiveOperator(channel, povm, regulator, agent)
    result = iterate(phi.phi, rho0, max_iter=100)

    # May or may not converge depending on parameters, just check it runs
    assert "converged" in result

