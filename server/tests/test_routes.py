import pytest
from app import create_app
from config import ProductionConfig

@pytest.fixture
def client():
    app = create_app(ProductionConfig)
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_get_chapter(client):
    response = client.get('/api/gita/chapter/1')
    assert response.status_code == 200
    assert 'chapter_number' in response.json