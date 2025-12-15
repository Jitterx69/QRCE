use axum::{Router};
use tower_http::cors::CorsLayer;

mod api;
mod persistence;
mod security;
mod scheduler;
mod state;

use state::AppState;

#[tokio::main]
async fn main() {
    let state = AppState {
        store: persistence::Store::new(),
        queue: scheduler::Queue::new(),
    };

    let app = Router::new()
        .merge(api::router())
        .with_state(state)
        .layer(CorsLayer::permissive());

    axum::Server::bind(&"0.0.0.0:8080".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
