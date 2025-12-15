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
    povm = POVM([np.diag([1,0]), np.diag([0,1])])
    regulator = QuantumRegulator(0.2)
    agent = QuantumAgent([np.eye(2), np.eye(2)])

    phi = QuantumReflexiveOperator(channel, povm, regulator, agent)
    result = iterate(phi.phi, rho0)

    assert result["converged"]
