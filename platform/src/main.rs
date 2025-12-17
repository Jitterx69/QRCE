use axum::Router;
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
        .layer(CorsLayer::permissive())
        .with_state(state);

    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080")
        .await
        .unwrap();
    
    println!("QRCE Platform listening on http://0.0.0.0:8080");
    
    axum::serve(listener, app)
        .await
        .unwrap();
}

