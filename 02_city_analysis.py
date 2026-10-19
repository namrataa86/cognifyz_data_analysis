import pandas as pd
df = pd.read_csv("restaurant_data.csv")
city_counts = df["City"].value_counts()
print(city_counts.head(10))

# calculate average rating for each city
city_ratings = df.groupby("City")["Aggregate rating"].mean()
print(city_ratings)

#highest rated city
highest_rated_city = city_ratings.idxmax()
highest_rated = city_ratings.max()

print("City:", highest_rated_city)
print("Average Rating:", round(highest_rated,2))