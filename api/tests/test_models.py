from datetime import datetime

from app.models import QuizQuestion


def test_create_row_in_short_url_model(db):
    created_at = datetime.utcnow()
    created_at_str = created_at.strftime('%Y-%m-%d %H:%M:%S.%f')
    obj = QuizQuestion(
        question_id=73,
        question="Some question",
        answer="Some answer",
        created_at=created_at,
    )
    db.session.add(obj)
    db.session.commit()

    db_query = db.session.query(QuizQuestion)
    assert obj.id is not None
    assert db_query.count() == 1
    assert repr(obj) == "Question №73"
    assert obj.to_json() == {
        'id': '1',
        'question_id': '73',
        'question': 'Some question',
        'answer': 'Some answer',
        'created_at': created_at_str,
    }
