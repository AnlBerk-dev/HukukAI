from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()
api_key = os.getenv("Gemini_Api_Key")
if not api_key:
    raise ValueError("Gemini_Api_Key not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Message is empty'}), 400

    try:
        convo_history = [{
            "role": "user",
            "parts": [{"text": user_message}]
        }]
        
        convo = model.start_chat(history=convo_history)
        response = convo.send_message(user_message)
        bot_message = response.text.strip()
        
        return jsonify({
            'response': bot_message
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 