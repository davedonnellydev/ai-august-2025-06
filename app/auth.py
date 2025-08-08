import os
from functools import wraps
from flask import request, jsonify, current_app


def require_bearer_token(f):
    """Decorator to require valid bearer token authentication"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the Authorization header
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return (
                jsonify(
                    {
                        "error": "Authentication required",
                        "message": "Bearer token is required in Authorization header",
                    }
                ),
                401,
            )

        # Check if it's a Bearer token
        if not auth_header.startswith("Bearer "):
            return (
                jsonify(
                    {
                        "error": "Invalid authentication format",
                        "message": "Authorization header must start with 'Bearer '",
                    }
                ),
                401,
            )

        # Extract the token
        parts = auth_header.split(" ")
        if len(parts) != 2 or not parts[1]:
            return jsonify({"error": "Invalid token", "message": "Bearer token is invalid"}), 401

        token = parts[1]

        # Get the expected API key from config or environment
        try:
            expected_token = current_app.config.get("API_KEY") or os.environ.get("API_KEY")
        except RuntimeError:
            # Handle case where app context is not available
            expected_token = os.environ.get("API_KEY")

        if not expected_token:
            return (
                jsonify(
                    {
                        "error": "Server configuration error",
                        "message": "API key not configured on server",
                    }
                ),
                500,
            )

        # Validate the token
        if token != expected_token:
            return jsonify({"error": "Invalid token", "message": "Bearer token is invalid"}), 401

        # Token is valid, proceed with the request
        return f(*args, **kwargs)

    return decorated_function
