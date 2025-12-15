use crate::persistence::Store;
use crate::scheduler::Queue;

#[derive(Clone)]
pub struct AppState {
    pub store: Store,
    pub queue: Queue,
}
