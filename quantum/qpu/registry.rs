use std::collections::HashMap;

#[derive(Clone)]
pub struct QPUInfo {
    pub id: String,
    pub url: String,
    pub max_qubits: usize,
    pub noise: f64,
    pub cost: f64,
}

#[derive(Clone)]
pub struct QPURegistry {
    inner: HashMap<String, QPUInfo>,
}

impl QPURegistry {
    pub fn new() -> Self {
        Self { inner: HashMap::new() }
    }

    pub fn register(&mut self, qpu: QPUInfo) {
        self.inner.insert(qpu.id.clone(), qpu);
    }

    pub fn list(&self) -> Vec<QPUInfo> {
        self.inner.values().cloned().collect()
    }
}
