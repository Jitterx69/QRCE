import shutil
from engine.state import State
from runtime.experiment import Experiment
from runtime.recorder import Recorder
from runtime.replay import Replay

def test_record_and_replay(tmp_path):
    s0 = State([1.0])
    exp = Experiment("test", s0, 3)

    history = [s0, State([2.0]), State([3.0])]

    rec = Recorder(tmp_path)
    rec.record(exp, history)

    rep = Replay(tmp_path)
    loaded = rep.load(exp.id)

    assert len(loaded) == len(history)
    assert loaded[-1].v[0] == 3.0
