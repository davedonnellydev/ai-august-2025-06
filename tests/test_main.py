def test_hello_world(client):
    """Test the main hello world endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    # Check for key elements of our new landing page
    assert b"Keyword Extractor API" in response.data
    assert b"AI August App-A-Day Challenge" in response.data
    assert b"View on GitHub" in response.data


def test_proxy_endpoint(client):
    """Test the proxy endpoint"""
    response = client.post("/api/proxy")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert "Proxy endpoint is working!" in data["message"]
