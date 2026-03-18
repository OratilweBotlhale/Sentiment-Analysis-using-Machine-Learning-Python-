import pandas as pd
import re

# Load dataset
df = pd.read_csv("../data/McDonald_s_Reviews.csv")

# Convert rating text to numbers
def extract_rating(text):
    return int(re.search(r"\d+", text).group())

df["rating"] = df["rating"].apply(extract_rating)

# Map rating to sentiment
def map_sentiment(rating):
    if rating <= 2:
        return "negative"
    elif rating == 3:
        return "neutral"
    else:
        return "positive"

df["sentiment"] = df["rating"].apply(map_sentiment)

print(df["sentiment"].value_counts())

# Save labeled dataset
df.to_csv("../data/labeled_reviews.csv", index=False)