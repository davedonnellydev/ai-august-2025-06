from flask import Blueprint, jsonify
import logging

health_bp = Blueprint("health", __name__)
logger = logging.getLogger(__name__)


@health_bp.route("/health", methods=["GET"])
def health_check():
    """Basic health check endpoint"""
    logger.debug("Health check requested")
    return jsonify({"status": "healthy", "message": "Service is running"}), 200


@health_bp.route("/health/detailed", methods=["GET"])
def detailed_health_check():
    """Detailed health check with more information"""
    logger.debug("Detailed health check requested")
    return (
        jsonify(
            {
                "status": "healthy",
                "message": "Service is running",
                "version": "1.0.0",
                "timestamp": "2024-01-01T00:00:00Z",
            }
        ),
        200,
    )
