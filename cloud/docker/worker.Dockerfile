FROM python:3.11-slim
WORKDIR /app
COPY engine ./engine
COPY quantum ./quantum
COPY control ./control
COPY runtime ./runtime
COPY pyproject.toml .
RUN pip install numpy scipy networkx matplotlib pydantic
CMD ["python", "-c", "print('QRCE worker ready')"]
