from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_deve_retornar_ola_html():
    client = TestClient(app)

    response = client.get('/exercicio-html')

    assert '<h1> Olá html </h1>' in response.text


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'carruda',
            'email': 'carlos@arruda.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
