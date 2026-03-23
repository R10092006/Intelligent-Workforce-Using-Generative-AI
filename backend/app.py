from flask import Flask, request, jsonify
from flask_cors import CORS
CORS(app)
app = Flask(__name__)

@app.route('/')
def home():
    return "Backend Running"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    task = data.get("task")
    return jsonify({"result": f"AI Suggestion for {task}"})

if __name__ == '__main__':
    app.run()
