import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    """This should pass"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_divide_by_zero(client):
    """This will FAIL - expects error handling but code has no check"""
    response = client.get('/api/divide?a=10&b=0')

    # We expect proper error handling
    assert response.status_code == 400
    assert 'error' in response.json
    # But current code will crash with 500!

def test_divide_normal(client):
    """This should pass"""
    response = client.get('/api/divide?a=10&b=2')
    assert response.status_code == 200
    assert response.json['result'] == 5.0

def test_get_user_not_found(client):
    """This will FAIL - expects error handling but code will crash"""
    response = client.get('/api/users/999')

    # We expect 404
    assert response.status_code == 404
    assert 'error' in response.json
    # But current code will crash with KeyError!

def test_get_user_exists(client):
    """This should pass"""
    response = client.get('/api/users/1')
    assert response.status_code == 200
    assert response.json['name'] == 'Alice'