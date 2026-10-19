import pandas as pd
df = pd.read_csv("restaurant_data.csv")
print(df["Restaurant Name"].value_counts().head(10))

chain_ratings = df.groupby("Restaurant Name")["Aggregate rating"].mean()
print(chain_ratings.sort_values(ascending=False).head(10))
chain_popularity = df["Restaurant Name"].value_counts().head(10)
print("Most popular restaurant chains:")
print(chain_popularity)
print("Observations:")
print("Restaurant chains with more outlets appear more frequently in the dataset.")
print("The analysis also shows that restaurant chains have different average ratings.")