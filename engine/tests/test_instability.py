import numpy as np
from engine import State, Engine, iterate
from engine.world import World
from engine.agent import Agent
from engine.prophecy import Prophecy
from engine.regulator import Regulator
from engine.metrics import detect_divergence

def test_divergence_detection():
    A = np.eye(1) * 1.2
    world = World(A)
    agent = Agent(gain=1.5)
    prophecy = Prophecy(noise=0.0)
    regulator = Regulator(leakage=0.0)

    engine = Engine(world, agent, prophecy, regulator)

    s0 = State([1.0])
    result = iterate(engine.phi, s0, max_iter=50)

    assert detect_divergence(result["history"])
