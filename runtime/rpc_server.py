from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from engine.state import State
from engine.engine import Engine

app = FastAPI()

class ExecuteExperiment(BaseModel):
    experiment_id: str
    steps: int
    initial_state: list[float]

class ExecutionResult(BaseModel):
    final_state: list[float]
    steps_executed: int
    diverged: bool

@app.post("/execute", response_model=ExecutionResult)
def execute(req: ExecuteExperiment):
    state = State(req.initial_state)

    # minimal default engine (can be parameterized later)
    engine = Engine.default()

    history = [state]
    diverged = False

    for _ in range(req.steps):
        state = engine.phi(state)
        history.append(state)
        if state.norm() > 1e6:
            diverged = True
            break

    return ExecutionResult(
        final_state=state.v.tolist(),
        steps_executed=len(history),
        diverged=diverged,
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
