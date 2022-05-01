from app.models import ShortURL


def test_create_row_in_short_url_model(db):
    obj = ShortURL(
        original='https://example.com/',
        url_id='superHardID12',
    )
    db.session.add(obj)
    db.session.commit()

    db_query = db.session.query(ShortURL)
    assert obj.id is not None
    assert db_query.count() == 1
    assert repr(obj) == "'superHardID12'"
    assert obj.to_json() == {'id': '1', 'original': 'https://example.com/', 'url_id': 'superHardID12'}
