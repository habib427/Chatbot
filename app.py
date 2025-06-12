from flask import Flask, request, jsonify, render_template
from bot_logic import get_response, load_responses
import os
print("Template path:", os.path.abspath("templates"))

app = Flask(__name__)
responses = load_responses()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    bot_reply = get_response(user_input, responses)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
