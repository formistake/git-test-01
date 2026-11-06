import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        messaggio="Ciao dal devops-lab! Sono contento di vederti.",
        ambiente=os.getenv("APP_ENV", "sviluppo"),
    )


@app.get("/health")
def health():
    return jsonify(status="ok")
