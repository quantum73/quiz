from unittest.mock import patch

from flask import current_app

from app.utils import get_base_url


@patch('app.utils.id_generator')
def test_id_generator(mocked_id_generator_func):
    expected = 'aAbBcCdD1234'
    mocked_id_generator_func.side_effect = lambda: expected
    actual = mocked_id_generator_func()
    assert actual == expected


def test_get_base_url_with_base_https_port(app):
    app.config['PORT'] = 443
    expected = 'https://127.0.0.1'
    actual = get_base_url()
    assert actual == expected


def test_get_base_url_with_base_http_port(app):
    app.config['PORT'] = 80
    expected = 'http://127.0.0.1'
    actual = get_base_url()
    assert actual == expected


def test_get_base_url_with_another_port(app):
    app.config['PORT'] = 5555
    expected = 'http://127.0.0.1:5555'
    actual = get_base_url()
    assert actual == expected
