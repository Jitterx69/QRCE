from control.constraints import LeakageConstraint

def test_leakage_constraint():
    c = LeakageConstraint(0.5)
    assert c.satisfied(0.4)
    assert not c.satisfied(0.6)
