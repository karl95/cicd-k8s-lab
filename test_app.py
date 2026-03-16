import pytest
from app import app                    # Impordime meie Flask rakenduse

@pytest.fixture                        # Fixture = korduvkasutatav test setup
def client():
    app.config['TESTING'] = True       # Lülitab Flask'i test režiimi
    with app.test_client() as client:  # Loob test kliendi (ei käivita päris serverit)
        yield client                   # yield = annab kliendi testile, pärast koristab

def test_health(client):
    response = client.get('/health')   # Simuleerib GET /health päringut
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['version'] == '1.0.0'  # Kontrollib et versioon klapib
    assert 'message' in data           # Kontrollib et väli eksisteerib

def test_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    products = response.get_json()
    assert len(products) == 2          # Ootame täpselt 2 toodet

    for product in products:           # Ärireegli kontroll: hinnad peavad olema positiivsed
        assert product['price'] > 0, f"Hind peab olema positiivne! Leitud: {product['price']}"
