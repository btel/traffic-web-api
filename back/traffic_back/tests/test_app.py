#!/usr/bin/env python
#coding=utf-8

import pytest
import json
import os
from traffic_back import create_app
from traffic_back.db import init_db, get_db
import psycopg2 as pg

sql_file = os.path.join(os.path.dirname(__file__), 'data.sql')
with open(sql_file, 'rb') as f:
    _data_sql = f.read().decode('utf8')

DB_USER = os.environ.get("USER")

@pytest.fixture
def app():
    app = create_app({'DATABASE_URL' : 'postgresql://{}@localhost/traffictestdb'.format(DB_USER),
                      'TESTING': True})

    with app.app_context():
        init_db()
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute(_data_sql)

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_traffic(client):
    response = client.get('/api/traffic')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert len(data['data']) == 24

    response = client.get('/api/traffic?period=12')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['data']) == 12

    response = client.get('/api/traffic?period=2')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['data'][0]['timestamp'] == '2018-08-11T13:00:00'
    assert data['data'][1]['timestamp'] == '2018-08-11T12:00:00'
