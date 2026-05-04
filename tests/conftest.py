import pytest

from app import app


@pytest.fixture
def client():
    """Створює тестовий клієнт Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
