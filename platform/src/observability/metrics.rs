use std::sync::atomic::{AtomicU64, Ordering};

static REQUESTS: AtomicU64 = AtomicU64::new(0);

pub fn inc_requests() {
    REQUESTS.fetch_add(1, Ordering::Relaxed);
}

pub fn snapshot() -> u64 {
    REQUESTS.load(Ordering::Relaxed)
}
