from flask import Blueprint, jsonify

proxy_bp = Blueprint("proxy", __name__)


@proxy_bp.route("/api/proxy", methods=["POST"])
def proxy():
    # Securely call your external API here
    return jsonify({"message": "Proxy endpoint is working!"})
