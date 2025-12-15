from control.bellman import BellmanRegulator

def test_bellman_selection():
    b = BellmanRegulator(gamma=0.9)
    idx = b.select([1.0, 0.5], [1.0, 2.0])
    assert idx == 0
