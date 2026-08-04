import joblib

# Load model and encoders
model = joblib.load("models/exercise_model.pkl")
gender_encoder = joblib.load("models/gender_encoder.pkl")
goal_encoder = joblib.load("models/goal_encoder.pkl")
activity_encoder = joblib.load("models/activity_encoder.pkl")
recommendation_encoder = joblib.load("models/recommendation_encoder.pkl")

print("===== Exercise Recommendation Chatbot =====")

# Get user input
age = int(input("Enter your age: "))
gender = input("Enter gender (Male/Female): ")
height = float(input("Enter height (in meters): "))
weight = float(input("Enter weight (in kg): "))
goal = input("Enter goal (Weight Loss/Muscle Gain/Fitness): ")
activity = input("Enter activity level (Low/Medium/High): ")

# Calculate BMI
bmi = weight / (height ** 2)

# Encode text inputs
gender = gender_encoder.transform([gender])[0]
goal = goal_encoder.transform([goal])[0]
activity = activity_encoder.transform([activity])[0]

# Make prediction
prediction = model.predict([[age, gender, bmi, goal, activity]])

# Decode prediction
exercise = recommendation_encoder.inverse_transform(prediction)

print("\n===== Recommendation =====")
print(f"Your BMI: {bmi:.2f}")
print("Recommended Exercise:", exercise[0])