import pytest

from app import create_app, db as _db


@pytest.fixture
def app():
    _app = create_app('testing')

    with _app.app_context():
        _db.create_all()

        yield _app

        _db.session.close()
        _db.drop_all()


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


@pytest.fixture
def db(app):
    with app.app_context():
        yield _db
