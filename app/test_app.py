from app import app


def test_health():
    client = app.test_client()
    risposta = client.get("/health")
    assert risposta.status_code == 200
    assert risposta.get_json() == {"status": "ok"}


def test_ambiente_di_default():
    client = app.test_client()
    risposta = client.get("/")
    assert risposta.get_json()["ambiente"] == "sviluppo"
