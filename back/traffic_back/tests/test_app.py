#!/usr/bin/env python
#coding=utf-8

import pytest
import json
from traffic_back import create_app

@pytest.fixture
def app():
    app = create_app()
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
