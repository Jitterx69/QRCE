use std::collections::HashMap;
use std::sync::{Arc, Mutex};

#[derive(Clone)]
pub struct Store {
    inner: Arc<Mutex<HashMap<String, String>>>,
}

impl Store {
    pub fn new() -> Self {
        Self {
            inner: Arc::new(Mutex::new(HashMap::new())),
        }
    }

    pub fn insert(&self, id: &str, name: &str) {
        self.inner.lock().unwrap().insert(id.into(), name.into());
    }

    pub fn list(&self) -> Vec<crate::api::models::ExperimentInfo> {
        self.inner
            .lock()
            .unwrap()
            .iter()
            .map(|(id, name)| crate::api::models::ExperimentInfo {
                id: id.clone(),
                name: name.clone(),
                status: "queued".into(),
            })
            .collect()
    }
}
