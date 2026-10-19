import pandas as pd
df = pd.read_csv("restaurant_data.csv")
cuisine_counts = df["Cuisines"].value_counts().head(10)
print(cuisine_counts)
combination_ratings = df.groupby("Cuisines")["Aggregate rating"].mean()
print(combination_ratings.sort_values(ascending=False).head(10))
top_common = df["Cuisines"].value_counts().head(10).index
common_combination_ratings = df[df["Cuisines"].isin(top_common)].groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)
print(common_combination_ratings)
                                        