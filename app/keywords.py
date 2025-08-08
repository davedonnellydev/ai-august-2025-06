from flask import Blueprint, jsonify, request
from app.limiter import limiter
from openai import OpenAI
from pydantic import BaseModel
import os

keywords_bp = Blueprint("keywords", __name__)


def get_openai_client():
    """Get OpenAI client with API key from environment"""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is required")
    return OpenAI(api_key=api_key)


@keywords_bp.route("/keywords", methods=["POST"])
@limiter.limit("10 per hour")
def keywords():
    # Accept either JSON payload {"text": "..."} / {"content": "..."}
    # or raw text body
    posted_text = None
    if request.is_json:
        data = request.get_json(silent=True) or {}
        posted_text = data.get("text") or data.get("content")
    else:
        posted_text = request.get_data(as_text=True)

    if not posted_text or not posted_text.strip():
        error_msg = "No text provided. Send raw text or JSON with 'text' or 'content'."
        return jsonify({"error": error_msg}), 400

    class KeywordArray(BaseModel):
        keywords: list[str]

    try:
        client = get_openai_client()
        system_content = (
            "Analyze the text and extract the best keywords to use for "
            "search engine optimization (SEO)"
        )
        response = client.responses.parse(
            model="gpt-5-nano",
            input=[
                {
                    "role": "system",
                    "content": system_content,
                },
                {"role": "user", "content": posted_text},
            ],
            text_format=KeywordArray,
        )
        parsed = response.output_parsed
        # Ensure JSON serializable
        return jsonify(parsed.model_dump() if hasattr(parsed, "model_dump") else parsed), 200
    except ValueError as e:
        return jsonify({"error": "Configuration error", "message": str(e)}), 500
    except Exception as exc:  # pragma: no cover
        return jsonify({"error": "Failed to extract keywords", "message": str(exc)}), 500
