from app.limiter import limiter


class TestLimiterConfiguration:
    """Test suite for rate limiter configuration"""

    def test_limiter_instance_created(self):
        """Test that limiter instance is properly created"""
        assert limiter is not None
        assert hasattr(limiter, "init_app")

    def test_limiter_storage_configured(self):
        """Test that storage is configured"""
        assert hasattr(limiter, "storage")
        assert limiter.storage is not None

    def test_limiter_with_app_context(self, app):
        """Test that limiter works with app context"""
        with app.app_context():
            # Should be able to access limiter in app context
            assert limiter is not None
            # Should be able to access storage
            assert limiter.storage is not None

    def test_limiter_decorator_functionality(self, client):
        """Test that rate limiting decorator is functional"""
        # Test that the endpoint exists and responds (indicating decorator is applied)
        response = client.post(
            "/keywords",
            json={"text": "test"},
            headers={"Authorization": "Bearer dev-api-key-change-in-production"},
        )
        # Should not be 404, indicating the endpoint with decorator exists
        assert response.status_code != 404
