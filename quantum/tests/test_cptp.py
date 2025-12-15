import numpy as np
from quantum.channels import amplitude_damping

def test_cptp_trace_preserving():
    channel = amplitude_damping(0.2)
    rho = np.array([[1,0],[0,0]], dtype=complex)
    rho2 = channel.apply(rho)
    assert abs(rho2.trace() - 1.0) < 1e-8
