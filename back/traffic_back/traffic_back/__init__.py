#!/usr/bin/env python
#coding=utf-8

import connexion
from flask_cors import CORS
from flask import Flask

def create_app(test_config=None):
    app = connexion.FlaskApp(__name__, specification_dir='./static')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        app.app.config.from_mapping(test_config)

    CORS(app.app)
    app.add_api('swagger.yaml', validate_responses=app.app.config.get('TESTING', False))


    from . import db
    db.init_app(app.app)

    return app.app
