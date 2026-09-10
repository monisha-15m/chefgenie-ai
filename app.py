import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from google import genai

from chatbot_config import CHATBOT_PROMPT

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PORT = int(os.getenv("PORT", "5000"))
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing. Add it to your .env file or Render Environment Variables.")

client = genai.Client(api_key=GEMINI_API_KEY)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "ChefGenie"})


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = str(data.get("message", "")).strip()

    if not user_message:
        return jsonify({
            "reply": "Please enter your ingredients or cooking request."
        }), 400

    if len(user_message) > 4000:
        return jsonify({
            "reply": "Please keep your request under 4000 characters."
        }), 400

    try:
        prompt = f"""{CHATBOT_PROMPT}

USER REQUEST:
{user_message}
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        reply = (response.text or "").strip()

        if not reply:
            reply = "Sorry, I could not create a recipe right now."

        return jsonify({"reply": reply})

    except Exception as exc:
        print(f"Gemini API error: {exc}")
        return jsonify({
            "reply": "Sorry, ChefGenie is temporarily unavailable. Please check the API key, model name, and deployment settings."
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
