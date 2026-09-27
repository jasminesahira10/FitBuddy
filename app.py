import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

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

    prompt = f"""
    You are FitBuddy, an expert AI fitness coach.
    Create a personalized 7-day fitness plan for:
    Age: {age}, Gender: {gender}, Weight: {weight}kg, Height: {height}cm
    Goal: {goal}, Activity Level: {activity}
    
    Give output in clean sections:
    1. Summary & Daily Calorie Target
    2. 7-Day Workout Plan (with sets/reps)
    3. 7-Day Veg/Non-Veg Diet Plan (breakfast, lunch, dinner)
    4. Important Tips
    Make it beginner-friendly.
    """

    try:
        response = model.generate_content(prompt)
        return jsonify({"plan": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)