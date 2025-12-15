use axum::Router;

pub mod routes;
pub mod models;

pub fn router() -> Router {
    Router::new()
        .merge(routes::router())
}
