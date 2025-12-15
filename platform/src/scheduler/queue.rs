use std::collections::VecDeque;
use std::sync::{Arc, Mutex};

#[derive(Clone)]
pub struct Queue {
    inner: Arc<Mutex<VecDeque<String>>>,
}

impl Queue {
    pub fn new() -> Self {
        Self {
            inner: Arc::new(Mutex::new(VecDeque::new())),
        }
    }

    pub fn enqueue(&self, id: &str) {
        self.inner.lock().unwrap().push_back(id.into());
    }

    pub fn dequeue(&self) -> Option<String> {
        self.inner.lock().unwrap().pop_front()
    }
}
