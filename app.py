#!/usr/bin/env python
#coding=utf-8

import connexion
from flask_cors import CORS

app = connexion.FlaskApp(__name__, specification_dir='./')
CORS(app.app)
app.add_api('swagger.yaml')
app.run(port=8080, debug=True)
