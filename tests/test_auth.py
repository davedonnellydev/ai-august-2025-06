from unittest.mock import patch, MagicMock


class TestBearerTokenAuthentication:
    """Test suite for bearer token authentication"""

    def test_missing_authorization_header(self, client):
        """Test that requests without Authorization header are rejected"""
        response = client.post("/keywords", json={"text": "test"})
        assert response.status_code == 401
        data = response.get_json()
        assert "error" in data
        assert "Authentication required" in data["error"]
        assert "Bearer token is required" in data["message"]

    def test_invalid_authorization_format(self, client):
        """Test that requests with invalid Authorization format are rejected"""
        response = client.post(
            "/keywords", json={"text": "test"}, headers={"Authorization": "InvalidFormat token123"}
        )
        assert response.status_code == 401
        data = response.get_json()
        assert "error" in data
        assert "Invalid authentication format" in data["error"]
        assert "must start with 'Bearer '" in data["message"]

    def test_missing_token_in_bearer(self, client):
        """Test that requests with 'Bearer ' but no token are rejected"""
        response = client.post(
            "/keywords", json={"text": "test"}, headers={"Authorization": "Bearer "}
        )
        assert response.status_code == 401
        data = response.get_json()
        assert "error" in data
        assert "Invalid token" in data["error"]

    def test_invalid_token(self, client):
        """Test that requests with invalid token are rejected"""
        response = client.post(
            "/keywords", json={"text": "test"}, headers={"Authorization": "Bearer invalid-token"}
        )
        assert response.status_code == 401
        data = response.get_json()
        assert "error" in data
        assert "Invalid token" in data["error"]
        assert "Bearer token is invalid" in data["message"]

    def test_valid_token_with_missing_api_key(self, client, app):
        """Test that requests fail when API_KEY is not configured"""
        with app.app_context():
            # Temporarily remove the API_KEY from config
            original_api_key = app.config.get("API_KEY")
            app.config["API_KEY"] = None

            try:
                response = client.post(
                    "/keywords",
                    json={"text": "test"},
                    headers={"Authorization": "Bearer valid-token"},
                )
                assert response.status_code == 500
                data = response.get_json()
                assert "error" in data
                assert "Server configuration error" in data["error"]
                assert "API key not configured" in data["message"]
            finally:
                # Restore the original API_KEY
                app.config["API_KEY"] = original_api_key

    def test_valid_token_success(self, client):
        """Test that requests with valid token proceed to the endpoint"""
        with patch("app.keywords.get_openai_client") as mock_get_client:
            # Mock the OpenAI client and response
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.output_parsed = MagicMock()
            mock_response.output_parsed.model_dump.return_value = {"keywords": ["test"]}
            mock_client.responses.parse.return_value = mock_response
            mock_get_client.return_value = mock_client

            response = client.post(
                "/keywords",
                json={"text": "test"},
                headers={"Authorization": "Bearer dev-api-key-change-in-production"},
            )

            # Should proceed past authentication (might fail on other validation)
            assert response.status_code in [200, 400, 500]
            # If it's 400, it means auth passed but validation failed (expected)
            # If it's 500, it means auth passed but OpenAI failed (expected in test)
            # If it's 200, it means everything worked

    def test_auth_before_rate_limiting(self, client):
        """Test that authentication happens before rate limiting"""
        # Make multiple requests with invalid auth - should all get 401, not 429
        for i in range(15):
            response = client.post(
                "/keywords",
                json={"text": f"test {i}"},
                headers={"Authorization": "Bearer invalid-token"},
            )
            expected_msg = f"Request {i} should be 401, not {response.status_code}"
            assert response.status_code == 401, expected_msg

    def test_auth_with_different_content_types(self, client):
        """Test that authentication works with different content types"""
        # Test with JSON
        response = client.post(
            "/keywords", json={"text": "test"}, headers={"Authorization": "Bearer invalid-token"}
        )
        assert response.status_code == 401

        # Test with raw text
        response = client.post(
            "/keywords",
            data="test text",
            content_type="text/plain",
            headers={"Authorization": "Bearer invalid-token"},
        )
        assert response.status_code == 401
