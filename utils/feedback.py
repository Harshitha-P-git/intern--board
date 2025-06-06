import pandas as pd

def load_feedback(csv_path="data/mentor_feedback.csv"):
    return pd.read_csv(csv_path)
