
import os
from flask import Blueprint, render_template, request, jsonify
from openai import OpenAI

views = Blueprint("views", __name__)
@views.route("/")
def home():
    return render_template("chat.html")


@views.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Please enter a message."}), 400

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return jsonify({
            "error": "AI API key is not configured yet."
        }), 503

    try:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions=(
                "You are Tuk_Tuk"
            ),
            input=message.strip()
        )

        return jsonify({"reply": response.output_text})

    except Exception:
        # Keep API credentials and internal error details private.
        return jsonify({
            "error": "Sorry, I could not get an AI response. Please try again."
        }), 502
