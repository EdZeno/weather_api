from api import create_app
import pytest

def test_data(client):
    assert client.get('/').data == b'Hello'

def test_api(client):
    assert client.get('/ping/').status_code == 200
