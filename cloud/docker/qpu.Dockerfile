FROM python:3.11-slim
WORKDIR /app
COPY quantum ./quantum
RUN pip install fastapi uvicorn numpy
CMD ["python", "-m", "quantum.qpu_server"]
