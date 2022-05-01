#!/usr/bin/env python
import os

import pytest
from flask_script import Manager, Shell

from app import create_app, db
from config import basedir

app = create_app(os.environ.get('FLASK_CONFIG', 'default'))
manager = Manager(app)
db.create_all(app=app)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def run_tests(tests_dir=None, verbosity=False):
    if tests_dir is None:
        tests_dir = os.path.join(basedir, 'tests')
    command = [tests_dir]
    if verbosity:
        command.append('-v')
    pytest.main(command)


if __name__ == "__main__":
    manager.run()
