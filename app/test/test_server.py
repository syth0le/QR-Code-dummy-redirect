def test_get_generated_qr_code(client):
    response = client.get('/generate')

    assert response.status_code == 200
    assert response.content_type == 'image/gif'


def test_get_dummy_request_from_qr_code(client):
    response = client.get('/dummy_request')

    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
