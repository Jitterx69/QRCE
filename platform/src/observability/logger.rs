use serde_json::json;
use chrono::Utc;

pub fn log(component: &str, event: &str, payload: serde_json::Value) {
    let record = json!({
        "timestamp": Utc::now().to_rfc3339(),
        "component": component,
        "event": event,
        "payload": payload
    });
    println!("{}", record);
}
