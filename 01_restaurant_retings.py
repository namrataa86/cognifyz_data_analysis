import pandas as pd
df = pd.read_csv("restaurant_data.csv")
rating_counts = df["Aggregate rating"].value_counts().sort_index()
print(rating_counts)
reting_ranges = pd.cut(df["Aggregate rating"], bins=[0, 1, 2, 3, 4, 5], labels=["0-1", "1-2", "2-3", "3-4", "4-5"])
print(reting_ranges.value_counts().sort_index())
average_rating = df["Votes"].mean()
print("Average Votes:", round(average_rating, 2))
top_common = df["Cuisines"].value_counts().head(10).index
common_combination_ratings = df[df["Cuisines"].isin(top_common)].groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)
print(common_combination_ratings)