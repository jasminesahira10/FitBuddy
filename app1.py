import streamlit as st

st.set_page_config(
    page_title="FitBuddy AI",
    page_icon="💪",
    layout="centered"
)

st.title("💪 FitBuddy")
st.subheader("AI Fitness Plan Generator")

st.write("Create your personalized fitness plan ✨")

with st.form("fitness_form"):

    name = st.text_input("Your Name")

    age = st.number_input(
        "Age",
        min_value=13,
        max_value=100,
        value=18
    )

    goal = st.selectbox(
        "Fitness Goal",
        [
            "General Fitness",
            "Strength",
            "Flexibility",
            "Healthy Lifestyle"
        ]
    )

    level = st.selectbox(
        "Fitness Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    days = st.slider(
        "Workout Days Per Week",
        1, 7, 3
    )

    equipment = st.selectbox(
        "Equipment",
        [
            "No Equipment",
            "Dumbbells",
            "Home Equipment",
            "Gym"
        ]
    )

    submit = st.form_submit_button("✨ Generate Plan")


if submit:

    st.success(f"Welcome {name}! Your FitBuddy plan is ready 💪")

    st.markdown("## 📅 Weekly Fitness Plan")

    exercises = [
        "Warm-up – 5 to 10 minutes",
        "Squats – 3 × 10",
        "Wall Push-ups – 3 × 10",
        "Glute Bridge – 3 × 12",
        "Plank – 3 × 20 seconds",
        "Cool-down – 5 minutes"
    ]

    for exercise in exercises:
        st.write("✅", exercise)

    st.markdown("## 🥗 Healthy Lifestyle Tips")

    st.write("💧 Stay hydrated throughout the day.")
    st.write("🥗 Include a variety of nutritious foods.")
    st.write("😴 Maintain a regular sleep schedule.")
    st.write("🚶 Take regular movement breaks.")

    st.info(
        "This is a general fitness plan for educational purposes. "
        "For medical or injury-related concerns, consult a qualified professional."
    )