from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv
import openai

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/process", methods=["POST"])
def process_message():
    data = request.get_json()
    user_message = data.get("message", "")

    # Run AI (OpenAI example)
    ai_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Respond to this SMS message: {user_message}",
        max_tokens=100
    )

    reply = ai_response.choices[0].text.strip()

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
