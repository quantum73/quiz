import datetime

import requests
from flask import jsonify, current_app, Response, request
from pydantic import ValidationError

from . import main
from .. import db
from ..models import InputBody, QuizQuestion


@main.route('/questions/', methods=['POST'])
def get_random_questions() -> Response:
    try:
        input_data = InputBody(**request.json)
    except ValidationError as validation_err:
        errors = validation_err.errors()
        response = jsonify(errors)
        response.status_code = 400
        return response

    questions_num = input_data.questions_num
    external_api_url = current_app.config.get('EXTERNAL_API_URL')
    question_objects = []

    while len(question_objects) != questions_num:
        response_from_external_api = requests.get(external_api_url)
        if response_from_external_api.status_code != 200:
            response = jsonify(
                {
                    'error': 'something is wrong with external api',
                    'details': [
                        {
                            'status': response_from_external_api.status_code,
                            'content': response_from_external_api.content,
                        }
                    ],
                }
            )
            response.status_code = 400
            return response

        json_data = response_from_external_api.json()[0]
        question_id = json_data.get('id')
        question_exists = QuizQuestion.query.filter_by(question_id=question_id).first()
        if question_exists is not None:
            continue

        question = json_data.get('question')
        answer = json_data.get('answer')
        created_at = json_data.get('created_at')
        created_at = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%fZ')

        question_obj = QuizQuestion(
            question_id=question_id,
            question=question,
            answer=answer,
            created_at=created_at,
        )
        question_objects.append(question_obj)

    db.session.add_all(question_objects)
    db.session.commit()

    response = jsonify(question_objects[-1].to_json())
    response.status_code = 201
    return response
