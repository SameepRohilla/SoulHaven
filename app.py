from flask import Flask, request, jsonify
from flask import send_from_directory
import requests

app = Flask(__name__)

# Replace with your Gemini API credentials
GEMINI_API_KEY = 'AIzaSyBDM2Bc_XK0y7RrtxsgsUEHzOjfkca-cNg'

# API route for chatting
@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    headers = {
        'Authorization': f'Bearer {GEMINI_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'input': user_message,
        'parameters': {
            'max_tokens': 150,
            'temperature': 0.7
        }
    }

    response = requests.post('https://api.gemini.com/v1/chat', headers=headers, json=data)

    if response.status_code == 200:
        api_response = response.json()
        return jsonify({'response': api_response['choices'][0]['text']})
    else:
        return jsonify({'error': 'API call failed'}), 500

# Route for serving static frontend
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

# Expose the app as a Vercel handler
def handler(request, context):
    return app(request, context)
