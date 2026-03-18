import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

# Load labeled dataset
df = pd.read_csv("../data/labeled_reviews.csv")

# Keep only needed columns
df = df[["review", "sentiment"]]

# Remove missing values
df = df.dropna()

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

df["clean_review"] = df["review"].apply(clean_text)

print(df.head())

# Save cleaned dataset
df.to_csv("../data/clean_reviews.csv", index=False)