import pandas as pd
df = pd.read_csv("restaurant_data.csv")
price_counts = df["Price range"].value_counts().sort_index()
print(price_counts)
total = len(df)
for price, count in price_counts.items():
    percentage = count / total * 100
    print(price, round(percentage, 2), "%")
import matplotlib.pyplot as plt
price_counts.plot(kind="bar")

plt.xlabel("Price range")
plt.ylabel("Number of restaurants")
plt.title("Distribution of Restaurants by Price Range")
plt.xticks(rotation=0)
plt.show()