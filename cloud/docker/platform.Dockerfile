FROM rust:1.75 as builder
WORKDIR /app
COPY platform ./platform
WORKDIR /app/platform
RUN cargo build --release

FROM debian:bookworm-slim
WORKDIR /app
COPY --from=builder /app/platform/target/release/qrce-platform /usr/local/bin/qrce-platform
EXPOSE 8080
CMD ["qrce-platform"]
