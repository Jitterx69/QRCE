from engine.state import State
from runtime.experiment import Experiment

def test_experiment_creation():
    s0 = State([0.0])
    exp = Experiment("test", s0, 10)
    assert exp.max_steps == 10
