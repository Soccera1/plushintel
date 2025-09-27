import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Make sure GEMINI_API_KEY is set in your environment variables
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

app = Flask(__name__)

# Simple memory for this session (reset on server restart)
chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"reply": "I can't hear you, Labubu!"})

    system_instruction = (
        "You are PlushIntel: a helpful assistant designed specifically for Labubu, "
        "a mischievous plush toy. Give clear, toy-friendly, playful advice, "
        "fun facts, or collection tips."
    )

    gemini_history = []
    for entry in chat_history:
        role = 'user' if entry['role'] == 'user' else 'model'
        gemini_history.append({'role': role, 'parts': [entry['content']]})

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=system_instruction
    )
    
    chat_session = model.start_chat(history=gemini_history)
    
    response = chat_session.send_message(user_message)
    
    reply = response.text

    # Save conversation to memory
    chat_history.append({"role": "user", "content": user_message})
    chat_history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
