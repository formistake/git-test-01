# Stage 1: installazione delle dipendenze
FROM python:3.12-slim AS build
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: immagine finale
FROM python:3.12-slim
LABEL org.opencontainers.image.source="https://github.com/formistake/git-test-01"
WORKDIR /opt/devops-lab
COPY --from=build /install /usr/local
COPY app.py .

RUN useradd --uid 10001 --no-create-home appuser
USER 10001

ENV APP_ENV=sviluppo
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
