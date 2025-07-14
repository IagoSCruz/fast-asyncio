from fastapi.testclient import TestClient

from fast_asyncio.app import app


def test_root_deve_retornar_hello():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá, mundo!'}
