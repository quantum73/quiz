from app.models import ShortURL


def test_short_route_with_valid_data(client, db):
    input_json_data = {'url': 'https://valid-url.com/?query_param=42'}
    new_url_key = 'new_url'
    response = client.post('/short/', json=input_json_data)
    json_data = response.json

    assert response.status_code == 201
    assert new_url_key in json_data
    assert db.session.query(ShortURL).count() == 1


def test_short_route_with_invalid_data(client):
    input_json_data = {'url': 'invalid_data'}
    response = client.post('/short/', json=input_json_data)
    json_data = response.json
    assert response.status_code == 400
    assert json_data[0].get('loc')[0] == 'url'


def test_go_to_site_route_with_valid_id(client):
    valid_url = 'https://valid-url.com/?query_param=42'
    input_json_data = {'url': valid_url}
    r = client.post('/short/', json=input_json_data)
    new_url = r.json.get('new_url')
    new_url_id = new_url.split('/')[-1]

    response = client.get(f'/{new_url_id}/')
    original_url_from_response = response.headers.get('Location')

    assert response.status_code == 301
    assert original_url_from_response == valid_url


def test_go_to_site_route_with_wrong_id(client):
    message_key = 'message'
    not_exists_url_message = 'This URL does not exist'
    response = client.get('/someWrongID42/')
    json_data = response.json

    assert response.status_code == 400
    assert message_key in json_data
    assert json_data.get(message_key) == not_exists_url_message
