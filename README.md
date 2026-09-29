FitBuddy – AI Fitness Plan Generator using Gemini Models

FitBuddy is an AI-powered web application that generates personalized 7-day fitness plans and nutrition/recovery tips based on a user's fitness goal, age, weight, and preferred workout intensity.

The application uses Google Gemini AI models, FastAPI, Jinja2, and SQLite to provide an interactive and personalized fitness planning experience.

 Features

- Personalized 7-day workout plan generation
- Supports goals such as weight loss, muscle gain, and general wellness
- Uses Gemini AI for intelligent workout generation
- AI-generated nutrition and recovery tips
- Update workout plans using user feedback
- Store user details and workout plans using SQLite
- Admin dashboard to view users and their plans
- Interactive HTML interface using Jinja2
- FastAPI backend with API documentation

 Technologies Used

- Python
- FastAPI
- Google Gemini AI
- Gemini 1.5 Pro
- Gemini Flash
- Jinja2
- HTML & CSS
- SQLAlchemy
- SQLite
- Uvicorn
- Git & GitHub

 Project Architecture

User
  ↓
HTML / Jinja2 Interface
  ↓
FastAPI Backend
  ↓
Google Gemini AI
  ├── Gemini Pro → Workout Plan
  └── Gemini Flash → Nutrition Tip
  ↓
SQLite Database

 Project Structure

FitBuddy/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── gemini_generator.py
│   ├── gemini_flash_generator.py
│   └── updated_plan.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── all_users.html
│
├── static/
│   └── images/
│
├── requirements.txt
└── README.md

 Installation

1. Clone the Repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd FitBuddy

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

If you don't have a "requirements.txt" file, install the required libraries:

pip install fastapi uvicorn jinja2 sqlalchemy python-multipart google-generativeai

 Gemini API Key

The application requires a Google Gemini API key.

Create an environment variable:

GOOGLE_API_KEY=your_gemini_api_key_here

Do not upload your actual API key to GitHub.

You can store it in a ".env" file if your project uses environment variables.

 Run the Application

Start the FastAPI server:

uvicorn app.main:app --reload

Then open:

http://127.0.0.1:8000

FastAPI API documentation is available at:

http://127.0.0.1:8000/docs

 How It Works

1. Enter User Details

The user provides:

- Name
- User ID
- Age
- Weight
- Fitness Goal
- Workout Intensity

2. Generate Workout Plan

The information is sent to the FastAPI backend.

Gemini Pro generates a structured 7-day workout plan containing warm-ups, exercises, sets/repetitions, and cooldown or recovery guidance.

3. Get Nutrition Tip

Gemini Flash generates a short nutrition or recovery recommendation related to the user's fitness goal.

4. Give Feedback

Users can submit feedback such as:

Add more cardio
Include more rest days
Add yoga exercises

The application sends the original plan and feedback to Gemini Pro and generates an updated plan.

5. Admin View

The admin page allows viewing:

- User information
- Original workout plans
- Updated workout plans
- Fitness goals
- Workout intensity

 Main Routes

Route| Purpose
"/"| Home page and user input form
"/generate-workout"| Generates workout and nutrition plan
"/submit-feedback"| Updates workout plan using feedback
"/view-all-users"| Displays users and their plans
"/docs"| FastAPI interactive API documentation

 AI Models

Gemini 1.5 Pro

Used for:

- Personalized 7-day workout plans
- Workout plan updates
- Feedback-based customization

Gemini Flash

Used for:

- Fast nutrition tips
- Recovery recommendations

 Database

FitBuddy uses SQLite with SQLAlchemy ORM to store:

- User ID
- Name
- Age
- Weight
- Fitness goal
- Workout intensity
- Original workout plan
- Updated workout plan

 Use Cases

FitBuddy can be used by:

- Individuals looking for personalized workout plans
- Fitness beginners
- Coaches and trainers
- Educational institutions
- Developers learning AI integration with FastAPI

 Future Improvements

Possible future enhancements include:

- User authentication and login
- Progress tracking
- Workout history
- Exercise images/videos
- Mobile application
- Cloud database integration
- Cloud deployment
- More advanced AI personalization
- Health and activity tracking integration

 Disclaimer

FitBuddy provides AI-generated fitness and nutrition suggestions for general informational purposes. Users should consult a qualified fitness or healthcare professional for personalized medical or fitness advice.

Project

Project Name: FitBuddy – AI Fitness Plan Generator using Gemini Models

Category: AI / Health-Tech / Web Application

Backend: FastAPI

AI: Google Gemini

Database: SQLite

Frontend: HTML, CSS & Jinja2
