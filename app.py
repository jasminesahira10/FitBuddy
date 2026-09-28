import os
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    age = data.get('age')
    gender = data.get('gender')
    weight = data.get('weight')
    height = data.get('height')
    goal = data.get('goal')
    activity = data.get('activity')
    prompt = f"You are FitBuddy... Age: {age}, Gender: {gender}, Weight: {weight}kg, Height: {height}cm Goal: {goal}, Activity: {activity} - 7 day plan kudu"
    try:
        response = client.models.generate_content(model='gemini-2.0-flash', contents=prompt)
        return jsonify({"plan": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
