import numpy as np
from engine.state import State
from control.computability import detect_oscillation

def test_oscillation():
    s1 = State([1.0])
    s2 = State([-1.0])
    history = [s1, s2, s1, s2]
    assert detect_oscillation(history)
