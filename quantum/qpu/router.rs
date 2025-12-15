use super::registry::QPUInfo;

pub struct QPURouter;

impl QPURouter {
    pub fn select(qpus: &[QPUInfo]) -> Option<QPUInfo> {
        qpus.iter()
            .min_by(|a, b| {
                let sa = a.noise + a.cost;
                let sb = b.noise + b.cost;
                sa.partial_cmp(&sb).unwrap()
            })
            .cloned()
    }
}
