import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("dataset/exercise_dataset.csv")

# Create LabelEncoder objects
gender_encoder = LabelEncoder()
goal_encoder = LabelEncoder()
activity_encoder = LabelEncoder()
recommendation_encoder = LabelEncoder()

# Encode categorical columns
df["Gender"] = gender_encoder.fit_transform(df["Gender"])
df["Goal"] = goal_encoder.fit_transform(df["Goal"])
df["ActivityLevel"] = activity_encoder.fit_transform(df["ActivityLevel"])
df["Recommendation"] = recommendation_encoder.fit_transform(df["Recommendation"])

# Features (Input)
X = df[["Age", "Gender", "BMI", "Goal", "ActivityLevel"]]

# Target (Output)
y = df["Recommendation"]

print("Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:", len(X_train))
print("Testing Data:", len(X_test))

# Create the model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

print("\n✅ Model trained successfully!")

# ==========================
# Step 26: Test the Model
# ==========================

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\n✅ Model Accuracy: {accuracy * 100:.2f}%")

# Display Actual vs Predicted
print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)

# ==========================
# Step 27: Save the Model
# ==========================

# Save the trained model
joblib.dump(model, "models/exercise_model.pkl")

# Save all encoders
joblib.dump(gender_encoder, "models/gender_encoder.pkl")
joblib.dump(goal_encoder, "models/goal_encoder.pkl")
joblib.dump(activity_encoder, "models/activity_encoder.pkl")
joblib.dump(recommendation_encoder, "models/recommendation_encoder.pkl")

print("\n✅ Model and encoders saved successfully!")

print("\nFiles saved inside the models folder:")
print("- exercise_model.pkl")
print("- gender_encoder.pkl")
print("- goal_encoder.pkl")
print("- activity_encoder.pkl")
print("- recommendation_encoder.pkl")