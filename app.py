import streamlit as st
import joblib

st.set_page_config(
    page_title="Exercise Recommendation Chatbot",
    page_icon="🏋️",
)

st.title("🏋️ Exercise Recommendation Chatbot")
# Load ML model
model = joblib.load("models/exercise_model.pkl")

gender_encoder = joblib.load("models/gender_encoder.pkl")
goal_encoder = joblib.load("models/goal_encoder.pkl")
activity_encoder = joblib.load("models/activity_encoder.pkl")
recommendation_encoder = joblib.load("models/recommendation_encoder.pkl")

# -------------------------
# Questions
# -------------------------

questions = [
    ("age", "👋 Hello! Let's get started.\n\n👉 What is your age?"),
    ("gender", "What is your gender? (Male/Female)"),
    ("height", "What is your height in meters? (Example: 1.75)"),
    ("weight", "What is your weight in kg?"),
    ("goal", "What is your fitness goal? (Weight Loss / Muscle Gain / Fitness)"),
    ("activity", "What is your activity level? (Low / Medium / High)")
]

# -------------------------
# Session State
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": questions[0][1]
        }
    ]

if "step" not in st.session_state:
    st.session_state.step = 0

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# -------------------------
# Display Chat
# -------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# Chat Input
# -------------------------

user_input = st.chat_input("Type your answer...")

if user_input:

    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Save answer
    key = questions[st.session_state.step][0]
    st.session_state.user_data[key] = user_input

    st.session_state.step += 1

    # Ask next question
if st.session_state.step < len(questions):

    next_question = questions[st.session_state.step][1]

    st.session_state.messages.append(
        {"role": "assistant", "content": next_question}
    )

    with st.chat_message("assistant"):
        st.markdown(next_question)

else:
    # Prediction starts here

    age = int(st.session_state.user_data["age"])
    gender = st.session_state.user_data["gender"]
    height = float(st.session_state.user_data["height"])
    weight = float(st.session_state.user_data["weight"])
    goal = st.session_state.user_data["goal"]
    activity = st.session_state.user_data["activity"]

    bmi = weight / (height ** 2)
    gender = gender.strip().title()
    gender_encoded = gender_encoder.transform([gender])[0]
    goal = goal.strip().title()
    goal_encoded = goal_encoder.transform([goal])[0]
    activity = activity.strip().title()
    activity_encoded = activity_encoder.transform([activity])[0]

    prediction = model.predict([[
        age,
        gender_encoded,
        bmi,
        goal_encoded,
        activity_encoded
    ]])

    exercise = recommendation_encoder.inverse_transform(prediction)[0]

    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal Weight"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    reply = f"""
## 🎉 Your Fitness Report

**BMI:** {bmi:.2f}

**Category:** {bmi_category}

### 🏋 Recommended Exercise

**{exercise}**
"""

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)