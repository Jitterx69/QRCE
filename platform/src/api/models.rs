use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
pub struct CreateExperiment {
    pub name: String,
    pub max_steps: usize,
}

#[derive(Serialize)]
pub struct ExperimentInfo {
    pub id: String,
    pub name: String,
    pub status: String,
}
