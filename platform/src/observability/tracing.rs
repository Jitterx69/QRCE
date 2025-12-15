use uuid::Uuid;
use std::time::Instant;

pub struct Span {
    id: String,
    name: String,
    start: Instant,
}

impl Span {
    pub fn start(name: &str) -> Self {
        Self {
            id: Uuid::new_v4().to_string(),
            name: name.to_string(),
            start: Instant::now(),
        }
    }

    pub fn end(self) {
        let elapsed = self.start.elapsed().as_millis();
        println!(
            "{{\"trace_id\":\"{}\",\"span\":\"{}\",\"duration_ms\":{}}}",
            self.id, self.name, elapsed
        );
    }
}
