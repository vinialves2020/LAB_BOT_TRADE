FROM python:3.12-slim AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /build
COPY pyproject.toml README.md ./
COPY src ./src
RUN python -m pip install --upgrade pip && \
    python -m pip wheel --wheel-dir /wheels ".[runtime]"

FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    BOTTRADE_CONFIG=/app/config/cloud.yaml

RUN groupadd --system bottrade && useradd --system --gid bottrade --home /app bottrade
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN python -m pip install --no-cache-dir /wheels/* && rm -rf /wheels
COPY config ./config
COPY dashboard ./dashboard
RUN mkdir -p /tmp/bottrade && chown -R bottrade:bottrade /app /tmp/bottrade
USER bottrade

ENTRYPOINT ["bottrade"]
CMD ["paper", "run", "signal", "--config", "/app/config/cloud.yaml"]
