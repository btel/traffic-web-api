#!/usr/bin/env python
#coding=utf-8

import connexion

app = connexion.FlaskApp(__name__, specification_dir='./')
app.add_api('swagger.yaml')
app.run(port=8080, debug=True)
