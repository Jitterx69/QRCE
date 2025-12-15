use axum::{
    extract::{State},
    routing::{get, post},
    Json, Router,
};
use uuid::Uuid;

use crate::state::AppState;
use crate::api::models::*;

pub fn router() -> Router<AppState> {
    Router::new()
        .route("/experiments", post(create_experiment))
        .route("/experiments", get(list_experiments))
}

async fn create_experiment(
    State(state): State<AppState>,
    Json(req): Json<CreateExperiment>,
) -> Json<ExperimentInfo> {

    let id = Uuid::new_v4().to_string();

    state.store.insert(&id, &req.name);
    state.queue.enqueue(&id);

    Json(ExperimentInfo {
        id,
        name: req.name,
        status: "queued".into(),
    })
}

async fn list_experiments(
    State(state): State<AppState>,
) -> Json<Vec<ExperimentInfo>> {

    let exps = state.store.list();
    Json(exps)
}
