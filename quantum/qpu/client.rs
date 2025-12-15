use serde::{Deserialize, Serialize};

#[derive(Serialize)]
pub struct QPURequest {
    pub rho: Vec<Vec<f64>>,
    pub steps: usize,
}

#[derive(Deserialize)]
pub struct QPUResponse {
    pub final_rho: Vec<Vec<f64>>,
}

pub async fn execute(
    url: &str,
    req: QPURequest,
) -> QPUResponse {
    let client = reqwest::Client::new();
    let res = client
        .post(format!("{}/run", url))
        .json(&req)
        .send()
        .await
        .unwrap();

    res.json::<QPUResponse>().await.unwrap()
}
