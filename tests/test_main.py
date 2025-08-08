def test_hello_world(client):
    """Test the main hello world endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Flask Python Starter!" in response.data


def test_proxy_endpoint(client):
    """Test the proxy endpoint"""
    response = client.post("/api/proxy")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert "Proxy endpoint is working!" in data["message"]
