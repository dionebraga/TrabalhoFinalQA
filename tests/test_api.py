import requests

BASE_URL = "https://projetofinal.jogajuntoinstituto.org/api"

def test_create_product():
    payload = {
        "name": "TestProduct",
        "description": "Product Description",
        "price": 99.99,
        "image": "https://image.url"
    }
    response = requests.post(f"{BASE_URL}/products", json=payload)
    assert response.status_code == 201

def test_delete_product():
    product_id = 1  # Replace with actual ID
    response = requests.delete(f"{BASE_URL}/products/{product_id}")
    assert response.status_code == 204

