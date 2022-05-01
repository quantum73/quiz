from pydantic import BaseModel

from . import db


class InputBody(BaseModel):
    questions_num: int


class ToJSONMixin:

    def to_json(self):
        return {column.name: str(getattr(self, column.name)) for column in self.__table__.columns}


class QuizQuestion(db.Model, ToJSONMixin):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True, index=True)
    question = db.Column(db.String(5120), nullable=False)
    answer = db.Column(db.String(5120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return 'Question №%r' % self.id
