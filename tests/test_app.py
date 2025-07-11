from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_deve_retornar_ola_html(client):
    response = client.get('/exercicio-html')

    assert '<h1> Olá html </h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'carruda',
            'email': 'carlos@arruda.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'carruda',
        'email': 'carlos@arruda.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'carruda',
                'email': 'carlos@arruda.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'caugustogarruda',
            'email': 'caugustog@arruda.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'caugustogarruda',
        'email': 'caugustog@arruda.com',
    }
