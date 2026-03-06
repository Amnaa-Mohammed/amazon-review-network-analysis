
import pandas as pd
import numpy as np

print("Loading dataset...")

# 1) --- Load the dataset ---
df = pd.read_csv("Reviews.csv", low_memory=False)

print("Original shape:", df.shape)


#  Remove rows with missing essential fields ---
df = df.dropna(subset=["UserId", "ProductId", "Text"])
df = df[df["UserId"].astype(str).str.strip() != ""]
df = df[df["ProductId"].astype(str).str.strip() != ""]


#  Remove duplicates (same user, product, and text) ---
df = df.drop_duplicates(subset=["UserId", "ProductId", "Text"])

print("After removing nulls & duplicates:", df.shape)



#- Remove extremely short reviews (spam-like) ---
df = df[df["Text"].str.len() > 5]


#  Convert types ---
df["UserId"] = df["UserId"].astype(str)
df["ProductId"] = df["ProductId"].astype(str)

if "Score" in df.columns:
    df["Score"] = pd.to_numeric(df["Score"], errors="coerce")


# 8) --- Final check ---
print("Final cleaned shape:", df.shape)
print(df.head())


# 9) --- Save cleaned dataset ---
df.to_csv("clean_reviews.csv", index=False)

print("Saved cleaned file as clean_reviews.csv")
