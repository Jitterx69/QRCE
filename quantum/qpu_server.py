from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import uvicorn

from quantum.qpu_simulator import QPUSimulator

app = FastAPI()
sim = QPUSimulator()

class QPURequest(BaseModel):
    rho: list[list[float]]
    steps: int

class QPUResponse(BaseModel):
    final_rho: list[list[float]]

@app.post("/run", response_model=QPUResponse)
def run(req: QPURequest):
    rho = np.array(req.rho, dtype=complex)
    history = sim.execute(rho, req.steps)
    final = history[-1].rho
    return QPUResponse(final_rho=final.real.tolist())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9100)
