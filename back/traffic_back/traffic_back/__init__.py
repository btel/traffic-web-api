#!/usr/bin/env python
#coding=utf-8

import connexion
from flask_cors import CORS
from flask import Flask

def create_app():
    app = connexion.FlaskApp(__name__, specification_dir='./static')
    CORS(app.app)
    app.add_api('swagger.yaml')

    return app.app
