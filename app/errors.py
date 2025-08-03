from flask import jsonify
import logging

logger = logging.getLogger(__name__)


def register_error_handlers(app):
    """Register error handlers for the application"""

    @app.errorhandler(400)
    def bad_request(error):
        logger.warning(f"Bad request: {error}")
        return jsonify({"error": "Bad request", "message": str(error)}), 400

    @app.errorhandler(404)
    def not_found(error):
        logger.warning(f"Not found: {error}")
        return (
            jsonify({"error": "Not found", "message": "The requested resource was not found"}),
            404,
        )

    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Internal server error: {error}")
        return (
            jsonify({"error": "Internal server error", "message": "An unexpected error occurred"}),
            500,
        )

    @app.errorhandler(Exception)
    def handle_exception(error):
        logger.error(f"Unhandled exception: {error}")
        return (
            jsonify({"error": "Internal server error", "message": "An unexpected error occurred"}),
            500,
        )
