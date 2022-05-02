from typing import Dict

from pydantic import BaseModel, validator

from . import db


class InputBody(BaseModel):
    questions_num: int

    @validator('questions_num')
    def validate_questions_num(cls, value):
        assert value > 0, 'value must be greater then 0'
        return value


class ToJSONMixin:

    def to_json(self) -> Dict[str, ...]:
        return {column.name: str(getattr(self, column.name)) for column in self.__table__.columns}


class QuizQuestion(db.Model, ToJSONMixin):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True, index=True)
    question = db.Column(db.String(5120), nullable=False)
    answer = db.Column(db.String(5120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return 'Question №%r' % self.question_id
