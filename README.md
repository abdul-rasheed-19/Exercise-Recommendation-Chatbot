# 🏋️ Exercise Recommendation Chatbot

An intelligent **Machine Learning-powered Exercise Recommendation Chatbot** built with **Python**, **Scikit-learn**, and **Streamlit**. The chatbot interacts with users in a conversational way, collects fitness information, calculates BMI, and recommends a suitable exercise based on a trained Decision Tree model.

---

## 🚀 Live Demo

🔗 **Try the App:**  
https://exercise-recommendation-chatbot.streamlit.app/

📂 **GitHub Repository:**  
https://github.com/abdul-rasheed-19/Exercise-Recommendation-Chatbot

---

## 📌 Project Overview

This project demonstrates how Machine Learning can be integrated into a conversational web application to provide personalized exercise recommendations.

Instead of filling out a traditional form, users interact with the chatbot by answering simple questions. The chatbot processes the information, calculates the user's BMI, and predicts the most suitable exercise using a trained Decision Tree Classifier.

---

## ✨ Features

- 💬 Conversational chatbot interface
- 📊 Calculates Body Mass Index (BMI)
- 🤖 Machine Learning-based exercise recommendation
- 🧠 Decision Tree Classifier
- 📁 Saved ML model using Joblib
- 🌐 Interactive Streamlit web application
- 🚀 Deployed online with Streamlit Community Cloud

---

## 🖥️ Chatbot Workflow

```text
Start
   │
   ▼
Welcome User
   │
   ▼
Ask Age
   │
   ▼
Ask Gender
   │
   ▼
Ask Height
   │
   ▼
Ask Weight
   │
   ▼
Calculate BMI
   │
   ▼
Ask Fitness Goal
   │
   ▼
Ask Activity Level
   │
   ▼
Predict Exercise
   │
   ▼
Display Recommendation
```

---

## 🧠 Machine Learning Model

**Algorithm Used**

- Decision Tree Classifier

**Input Features**

- Age
- Gender
- BMI
- Fitness Goal
- Activity Level

**Output**

- Recommended Exercise

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

### Tools

- VS Code
- Git
- GitHub
- Streamlit Community Cloud

---

## 📂 Project Structure

```text
Exercise-Recommendation-Chatbot/
│
├── dataset/
│   └── exercise_dataset.csv
│
├── models/
│   ├── exercise_model.pkl
│   ├── gender_encoder.pkl
│   ├── goal_encoder.pkl
│   ├── activity_encoder.pkl
│   └── recommendation_encoder.pkl
│
├── app.py
├── chatbot.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/abdul-rasheed-19/Exercise-Recommendation-Chatbot.git
```

Move into the project directory

```bash
cd Exercise-Recommendation-Chatbot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

### 🏠 Home Screen

> *(Add a screenshot here)*

---

### 💬 Chatbot Conversation

> *(Add a screenshot here)*

---

### 🏋️ Exercise Recommendation

> *(Add a screenshot here)*

---

## 📈 Future Improvements

- AI-powered natural language conversation
- Personalized workout plans
- Exercise demonstration videos
- Diet recommendations
- User authentication
- Workout history
- Progress tracking dashboard
- Voice interaction
- Multi-language support

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Data preprocessing
- Label Encoding
- Decision Tree Classification
- Model serialization with Joblib
- BMI calculation
- Streamlit web application development
- Session state management
- Git & GitHub version control
- Deploying Machine Learning applications

---

## 👨‍💻 Author

**Abdul Rasheed**

🎓 B.E. Computer Science Engineering (Data Science)

🔗 GitHub:
https://github.com/abdul-rasheed-19

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

It motivates me to build more Machine Learning and Data Science projects.

---

## 📜 License

This project is licensed under the MIT License.
