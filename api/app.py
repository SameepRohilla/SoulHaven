from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyBDM2Bc_XK0y7RrtxsgsUEHzOjfkca-cNg")

# Initialize Flask app
app = Flask(__name__)

# Load the model
model = genai.GenerativeModel("tunedModels/conv-ai--nluypwvpm89y")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Call the API with the user's message
    response = model.generate_content(user_message)
    
    # Extract the text response
    reply = response.text
    
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(debug=True)

