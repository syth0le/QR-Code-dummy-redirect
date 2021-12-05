import pytest

from app.server import app


@pytest.fixture
def create_app():
    return app


@pytest.fixture
def client(create_app):
    return create_app.test_client()
