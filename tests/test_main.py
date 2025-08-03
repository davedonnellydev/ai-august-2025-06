def test_hello_world(client):
    """Test the main hello world endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Flask Python Starter!" in response.data
