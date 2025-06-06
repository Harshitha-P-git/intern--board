import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime, timedelta

# --- Page config ---
st.set_page_config(page_title="Intern Spotlight Board", layout="centered")

# --- Colorful background CSS ---
page_bg = """
<style>
/* Full page gradient background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
    min-height: 100vh;
}

/* Content panel with slight white translucent background */
.stApp {
    background: rgba(255, 255, 255, 0.85);
    min-height: 100vh;
    padding: 2rem 3rem;
    border-radius: 10px;
    color: #333333;
}

/* Headings color override */
h1, h2, h3, h4 {
    color: #4a148c !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Helper functions ---

def get_github_events(username, token):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Authorization": f"token {token}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()
    return []

def load_feedback(path="data/mentor_feedback.csv"):
    return pd.read_csv(path)

def calculate_score(events, feedback_score):
    pr_count = sum(1 for e in events if e["type"] == "PullRequestEvent")
    issue_count = sum(1 for e in events if e["type"] == "IssuesEvent")
    return pr_count * 2 + issue_count + feedback_score * 5

def get_current_week_range():
    today = datetime.now()
    start = today - timedelta(days=today.weekday())  # Monday
    end = start + timedelta(days=6)  # Sunday
    return start.strftime("%b %d"), end.strftime("%b %d")

# --- Main app ---

st.title("📣 Intern Spotlight Board")

# Show current week range
week_start, week_end = get_current_week_range()
st.markdown(f"### Week of **{week_start} – {week_end}**")

# Load data
feedback_df = load_feedback()
with open("assets/interns.json") as f:
    intern_data = json.load(f)

token = st.secrets["GITHUB_TOKEN"]
interns = list(intern_data.keys())
scores = []

# Calculate scores for all interns
for username in interns:
    events = get_github_events(username, token)
    feedback = feedback_df[feedback_df["username"] == username]
    feedback_score = feedback["score"].mean() if not feedback.empty else 0
    quote = feedback["quote"].iloc[0] if not feedback.empty else "No feedback yet."
    total_score = calculate_score(events, feedback_score)
    scores.append((username, total_score, quote))

# Sort descending by total score
scores.sort(key=lambda x: x[1], reverse=True)
top_intern = scores[0][0]

# Spotlight intern section with clickable GitHub username
info = intern_data[top_intern]
st.subheader("🏆 Intern of the Week")
st.markdown(f"""
### {info['name']} ([{top_intern}](https://github.com/{top_intern}))  
**Total Score:** {scores[0][1]:.1f}  
💬 _"{scores[0][2]}"_  
🎉 **Fun Fact**: {info['fun_fact']}
""", unsafe_allow_html=True)

# Leaderboard section with clickable GitHub usernames
st.subheader("📋 Leaderboard")
for i, (uname, sc, _) in enumerate(scores):
    st.markdown(f"**{i+1}. {intern_data[uname]['name']}** ([{uname}](https://github.com/{uname})) — {sc:.1f} pts", unsafe_allow_html=True)

# Last updated timestamp
last_updated = datetime.now().strftime("%b %d, %Y %H:%M:%S")
st.markdown(f"*Last updated: {last_updated}*")
