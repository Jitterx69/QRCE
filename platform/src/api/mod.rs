use axum::Router;

pub mod models;
pub mod routes;

use crate::state::AppState;

pub fn router() -> Router<AppState> {
    routes::router()
}
