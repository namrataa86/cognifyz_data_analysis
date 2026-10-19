import pandas as pd
df = pd.read_csv("restaurant_data.csv")
delivery_counts = df["Has Online delivery"].value_counts()
print(delivery_counts)
total = len(df)
for delivery, count in delivery_counts.items():
    percentage = (count / total) * 100
    print(delivery, round(percentage, 2), "%")
average_rating = df.groupby("Has Online delivery")["Aggregate rating"].mean()
print("Average Rating: ")
print(average_rating.round(2))
