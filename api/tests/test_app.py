from app.models import QuizQuestion


def test_get_random_questions_with_valid_data(client, db):
    valid_data = {'questions_num': 3}
    response = client.post('/questions/', json=valid_data)
    response_json_data = response.json

    db_query = db.session.query(QuizQuestion)
    last_obj = db_query.get(3)

    assert response.status_code == 201
    assert db_query.count() == 3
    assert last_obj is not None
    assert last_obj.to_json() == response_json_data


def test_get_random_questions_with_invalid_data(client):
    invalid_data = {'questions_num': 'invalid'}
    response = client.post('/questions/', json=invalid_data)
    response_json_data = response.json

    assert response.status_code == 400
    assert response_json_data[0].get('loc')[0] == 'questions_num'
