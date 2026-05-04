def test_hello_status_code(client):
    """GET / повертає статус 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_hello_message(client):
    """GET / повертає правильне повідомлення."""
    response = client.get("/")
    data = response.get_json()
    assert data["message"] == "Hello, DevOps!"


def test_health_status_code(client):
    """GET /health повертає статус 200."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_response(client):
    """GET /health повертає JSON зі статусом healthy."""
    response = client.get("/health")
    data = response.get_json()
    assert "status" in data
    assert data["status"] == "healthy"


def test_info_default_values(client):
    """GET /info повертає значення за замовчуванням."""
    response = client.get("/info")
    assert response.status_code == 200
    data = response.get_json()
    assert data["version"] == "1.0.0"
    assert data["environment"] == "development"


def test_info_custom_env(client, monkeypatch):
    """GET /info читає змінні оточення."""
    monkeypatch.setenv("APP_VERSION", "2.5.0")
    monkeypatch.setenv("ENVIRONMENT", "production")
    response = client.get("/info")
    data = response.get_json()
    assert data["version"] == "2.5.0"
    assert data["environment"] == "production"


def test_not_found(client):
    """Неіснуючий endpoint повертає 404."""
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_method_not_allowed(client):
    """POST на GET-only endpoint повертає 405."""
    response = client.post("/")
    assert response.status_code == 405


def test_greet_success(client):
    """Успішний запит з ім'ям"""
    response = client.get("/api/greet/anna")
    assert response.status_code == 200
    data = response.get_json()
    assert data["greeting"] == "Hello, Anna!"
    assert data["name_length"] == 4


def test_greet_capitalize(client):
    """Ім'я у нижньому регістрі — має бути capitalize"""
    response = client.get("/api/greet/ivan")
    assert response.status_code == 200
    data = response.get_json()
    assert data["greeting"] == "Hello, Ivan!"


def test_greet_missing_name(client):
    """Запит на /api/greet/ без імені -> 404"""
    response = client.get("/api/greet/")
    assert response.status_code == 404
