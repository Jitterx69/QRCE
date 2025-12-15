import numpy as np
from engine import State, Engine, iterate
from engine.world import World
from engine.agent import Agent
from engine.prophecy import Prophecy
from engine.regulator import Regulator

def test_convergent_fixed_point():
    A = np.eye(2) * 0.5
    world = World(A)
    agent = Agent(gain=0.2)
    prophecy = Prophecy(noise=0.0)
    regulator = Regulator(leakage=0.1)

    engine = Engine(world, agent, prophecy, regulator)

    s0 = State([1.0, -1.0])
    result = iterate(engine.phi, s0)

    assert result["converged"] is True
