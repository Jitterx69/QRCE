use serde::{Deserialize, Serialize};

#[derive(Serialize)]
pub struct ExecuteExperiment {
    pub experiment_id: String,
    pub steps: usize,
    pub initial_state: Vec<f64>,
}

#[derive(Deserialize)]
pub struct ExecutionResult {
    pub final_state: Vec<f64>,
    pub steps_executed: usize,
    pub diverged: bool,
}

pub async fn execute_on_worker(
    worker_url: &str,
    req: ExecuteExperiment,
) -> ExecutionResult {
    let client = reqwest::Client::new();
    let res = client
        .post(format!("{}/execute", worker_url))
        .json(&req)
        .send()
        .await
        .unwrap();

    res.json::<ExecutionResult>().await.unwrap()
}
