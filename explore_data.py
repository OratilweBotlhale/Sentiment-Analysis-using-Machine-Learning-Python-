import pandas as pd

#load dataset
# without encoding, youll get an
df = pd.read_csv("data/McDonald_s_Reviews.csv", encoding="latin1")

#preview the first 5 rows
print(df.head())

#dataset info
print("\nDataset Info:")
print(df.info())

#column name
print("\nColumn names:")
print(df.columns)

#check rating
print("\nRating Distribution: ")
print(df['rating'].value_counts())

