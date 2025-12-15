pub fn authorize(token: Option<&str>) -> bool {
    match token {
        Some(t) if t == "qrce-dev-token" => true,
        _ => false,
    }
}
