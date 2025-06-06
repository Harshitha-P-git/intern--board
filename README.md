# 🌟 Intern Spotlight Board

A Streamlit web app that automatically highlights top-performing interns each week based on GitHub activity and mentor feedback.

---

## 🚩 Problem

Intern achievements often go unnoticed unless manually announced.  
This app solves that by:

- Automatically detecting top contributors from GitHub stats
- Using mentor feedback scores to evaluate impact
- Generating fun weekly “Spotlight Intern” cards

---

## 🛠️ Features

- 📊 Fetch GitHub activity of interns
- 📝 Parse mentor feedback from CSV
- 🏆 Score and rank interns
- 🎨 Display spotlight cards with names, quotes, and scores

---

## 🚀 How to Run Locally

1. Clone this repo:

git clone https://github.com/your-username/intern-board.git
cd intern-spotlight

2. Install dependencies:

pip install -r requirements.txt

3. Create the secrets file:

# .streamlit/secrets.toml
GITHUB_TOKEN = "your_github_token_here"

4. Run the app:

streamlit run app.py

👥 Contributors
P Harshitha
P Rama Krishna Sai Prasad

