from flask import Blueprint, jsonify, request
from openai import OpenAI
from pydantic import BaseModel

keywords_bp = Blueprint("keywords", __name__)

client = OpenAI()

@keywords_bp.route("/keywords", methods=["POST"])
def keywords():
    # Accept either JSON payload {"text": "..."} / {"content": "..."} or raw text body
    posted_text = None
    if request.is_json:
        data = request.get_json(silent=True) or {}
        posted_text = data.get("text") or data.get("content")
    else:
        posted_text = request.get_data(as_text=True)

    if not posted_text or not posted_text.strip():
        return jsonify({"error": "No text provided. Send raw text or JSON with 'text' or 'content'."}), 400

    class KeywordArray(BaseModel):
        keywords: list[str]

    try:
        response = client.responses.parse(
            model="gpt-5-nano",
            input=[
                {
                    "role": "system",
                    "content": "Analyze the text and extract the best keywords to use for search engine optimization (SEO)",
                },
                {"role": "user", "content": posted_text},
            ],
            text_format=KeywordArray,
        )
        parsed = response.output_parsed
        # Ensure JSON serializable
        return jsonify(parsed.model_dump() if hasattr(parsed, "model_dump") else parsed), 200
    except Exception as exc:  # pragma: no cover
        return jsonify({"error": "Failed to extract keywords", "message": str(exc)}), 500
